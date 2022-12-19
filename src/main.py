import time
import whisper
import pyautogui
import sounddevice as sd
from scipy.io.wavfile import write, read
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from pynput.keyboard import Controller

keyboard = Controller()



metinler = ["türe"]

# Define the frequency of the recording
freq = 88200

# Create a flag to track whether the recording is in progress
recording_in_progress = False

# Create a variable to store the start time of the recording
recording_start_time = 0

def detect_special_characters(string):
    special_characters = []
    for char in string:
        # Check if the character is a special character
        if ord(char) > 127:
            # If it is, add it to the list of special characters
            special_characters.append(char)
    return special_characters



def trim_audio(input_file, output_file, duration):
    # Read the recorded audio from the file
    sampling_rate, audio = read(input_file)

    # Calculate the number of samples in the recording
    num_samples = int(duration * sampling_rate)

    # Trim the audio to the number of samples in the recording
    trimmed_audio = audio[:num_samples]

    # Save the trimmed audio to a new file
    write(output_file, sampling_rate, trimmed_audio)

# Get the list of special characters
special_characters = detect_special_characters(metinler[-1])




def mesaj():
    keyboard.type(metinler[-1])
    time.sleep(1)
    pyautogui.press("enter")
    
def ses():
    model = whisper.load_model("small")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("recording0.wav")
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    metin = str(result.text)
    metinler.append(metin)
    print(metin)

# Create a function that will be called when the "Start recording" button is clicked
def start_recording():
    # Start the recording
    global recording
    recording = sd.rec(int(30*freq), samplerate=freq, channels=2)

    # Set the flag to indicate that the recording is in progress
    global recording_in_progress
    recording_in_progress = True

    # Store the start time of the recording
    global recording_start_time
    recording_start_time = time.time()




def stop_recording():
    # Stop the recording
    sd.stop()

    # Set the flag to indicate that the recording is not in progress
    global recording_in_progress
    recording_in_progress = False

    # Calculate the duration of the recording
    global recording_start_time
    duration = time.time() - recording_start_time

    # Save the recorded audio to a file
    global recording
    write("recording0.wav", freq, recording)
    trim_audio("recording0.wav", "trimmed_recording.wav", duration)
    ses()
    mesaj()



# Create a QApplication and a QWidget
# Create a QApplication and a QWidget
app = QApplication([])
window = QWidget()
# Create a QPushButton and set its text and on-click action
button_start = QPushButton("Start recording")
button_start.clicked.connect(start_recording)

button_stop = QPushButton("Stop recording", clicked=stop_recording)
button_stop.clicked.connect(stop_recording)
button_stop.clicked.disconnect(stop_recording)

# Create a vertical layout and add the buttons to it
layout = QVBoxLayout()
layout.addWidget(button_start)
layout.addWidget(button_stop)

# Set the layout of the window and show it
window.setLayout(layout)
window.show()

# Run the application
app.exec_()



