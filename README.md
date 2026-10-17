🎙️ Speech-to-Text Converter

A simple Python application that converts spoken words into text using a microphone and Google's Speech Recognition service. The application captures audio in real time, reduces the impact of background noise, and displays the recognized speech in the terminal.

✨ Features
🎤 Live Speech Input: Captures speech through the default microphone.
🔇 Background Noise Adjustment: Calibrates the microphone for ambient noise before recording.
🗣️ Speech Recognition: Converts spoken words into text using Google's speech recognition service.
⏱️ Timeout Handling: Stops waiting if speech does not begin within the specified time.
⚠️ Error Handling: Handles unrecognized speech, network or service errors, and microphone-related issues.
🖥️ Terminal Output: Displays the recognized text directly in the console.
🛠️ Technologies Used
Python – Core programming language.
SpeechRecognition – Captures and processes audio for speech recognition.
PyAudio – Provides microphone audio input for the SpeechRecognition library.
Google Speech Recognition – Recognizes spoken words and returns text.
📂 Project Structure
speech-to-text-converter/
│
├── main.py
├── requirements.txt
└── README.md

main.py – Main Python application.
requirements.txt – Lists the project dependencies.
README.md – Project documentation.
⚙️ Installation and Setup
1. Clone the Repository
git clone <your-repository-url>
cd speech-to-text-converter


Replace <your-repository-url> with your actual Git repository URL.

2. Create a Virtual Environment (Recommended)
python -m venv venv


Activate the environment:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3. Install Dependencies

Create a requirements.txt file with the following content:

SpeechRecognition
PyAudio


Install the dependencies:

pip install -r requirements.txt


Note: PyAudio installation may require additional system dependencies or a compatible prebuilt package, depending on your operating system and Python version.

4. Run the Application

Run the following command in your terminal:

python main.py


Make sure your microphone is connected and accessible before starting the application.

🚀 How It Works
Initialize Recognizer: Creates a Recognizer object to process audio.
Access Microphone: Opens the default microphone using sr.Microphone().
Adjust for Noise: Samples ambient noise for one second to calibrate recognition.
Capture Speech: Waits up to 10 seconds for speech to begin and records a phrase for up to 15 seconds.
Recognize Speech: Sends the captured audio to Google's speech recognition service.
Display Result: Prints the recognized text in the terminal.
Handle Errors: Displays helpful messages when speech is not detected, cannot be understood, the service fails, or microphone access is unavailable.
💻 Example Output

Successful recognition

Adjusting for background noise... Please wait.
Speak now...
Recognizing speech...
You said: Hello, how are you?


No speech detected

Adjusting for background noise... Please wait.
Speak now...
No speech detected within the timeout.


Unrecognized audio

Sorry, I couldn't understand the audio.

⚠️ Error Handling
Error	Description
WaitTimeoutError	No speech starts within the 10-second timeout.
UnknownValueError	The recorded audio could not be understood.
RequestError	The recognition service or network request fails.
OSError	A microphone or audio-device error occurs.
AttributeError	An attribute-related error occurs during microphone handling.
📋 Requirements
Python 3.9 or a compatible version supported by the installed dependencies.
A working microphone.
An active internet connection for Google's online speech recognition service.
Microphone permissions enabled in your operating system.
Compatible audio input drivers and PyAudio installation.
🔧 Troubleshooting
Microphone not detected: Check your microphone connection and operating system input settings.
Permission denied: Allow microphone access for your terminal or Python application.
PyAudio installation fails: Install a compatible PyAudio package or the required system audio dependencies.
Speech not recognized: Speak clearly, reduce background noise, and try again.
Service error: Check your internet connection and try again later.
🔮 Future Enhancements
Add support for multiple recognition languages.
Build a graphical interface using Streamlit or Tkinter.
Save recognized speech to a .txt file.
Support audio file uploads.
Add continuous speech recognition.
Display timestamps for recognized phrases.
Explore offline speech recognition engines.
👨‍💻 Author

Developed as a Python project to demonstrate real-time speech recognition and microphone input handling.

📄 License

This project is available for educational and personal use. Add an open-source license if you plan to distribute it under specific licensing terms.
