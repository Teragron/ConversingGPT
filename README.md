# ConversingGPT
A script for communicating with the ChatGPT language model using audio recording and transcription


This repository contains a script that allows you to communicate with a language model using audio recording and transcription. The script includes a GUI that allows you to start and stop the recording, and the transcribed text is sent to the target application.

## Dependencies

- Python 3
- [whisper](https://github.com/openai/whisper)
- [pyautogui](https://pyautogui.readthedocs.io/)
- [sounddevice](https://python-sounddevice.readthedocs.io/)
- [scipy](https://www.scipy.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pynput](https://pynput.readthedocs.io/)

## Usage

To use the script, clone the repository and install the dependencies:

```bash
git clone https://github.com/USERNAME/conversing-with-language-model.git
bashcd conversing-with-language-model
pip install -r requirements.txt
```


Then run the script:


```python src/main.py```


This will open the GUI, which includes buttons for starting and stopping the recording. When the "Start recording" button is clicked, the script will start recording audio. When the "Stop recording" button is clicked, the script will stop the recording, save the recorded audio to a file, transcribe the audio to text, and send the transcribed text to the target application.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
- [whisper](https://github.com/mozilla/whisper)
- [pyautogui](https://pyautogui.readthedocs.io/)
- [sounddevice](https://python-sounddevice.readthedocs.io/)
- [scipy](https://www.scipy.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [pynput](https://pynput.readthedocs.io/)

# Demo
[![Watch the video](https://i.imgflip.com/604ad4.jpg)]([https://www.youtube.com/watch?v=tM6KFKM0MS0](https://youtu.be/GKOf6Nyi6zk))
