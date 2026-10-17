
import speech_recognition as sr

recognizer = sr.Recognizer()

try:
    # Use the default microphone first
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Speak now...")
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)

    print("Recognizing speech...")

    text = recognizer.recognize_google(audio)
    print("You said:", text)

except sr.WaitTimeoutError:
    print("No speech detected within the timeout.")

except sr.UnknownValueError:
    print("Sorry, I couldn't understand the audio.")

except sr.RequestError as e:
    print(f"Speech recognition service error: {e}")

except (OSError, AttributeError) as e:
    print(f"Microphone error: {e}")
    print("Check your microphone device and Windows permissions.")
