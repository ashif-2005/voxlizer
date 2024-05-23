import streamlit as st
import speech_recognition as sr

# Function to transcribe audio from microphone
def transcribe_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
        st.write("Listening...")
        audio = r.listen(source, phrase_time_limit=5)  # Adjust phrase time limit as needed
    
    try:
        transcription = r.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Error: Could not request results; {0}".format(e)

def main():
    st.title("Speech Transcription")

    listening = False
    if st.button("Start Listening"):
        listening = True

    if listening:
        transcription = transcribe_audio()
        st.write("Transcription:")
        st.write(transcription)

        if st.button("Stop Listening"):
            listening = False

if __name__ == "__main__":
    main()
