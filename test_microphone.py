import openai
import pyttsx3
import speech_recognition as sr

#set OpenAI API Key
openai.api_key = "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"

# Initialize the text to speech engine 
engine=pyttsx3.init()

def main():
    while True:
        #Waith for user say "genius"
        print("Say 'Javis' to start recording your question")
        with sr.Microphone() as source:
            recognizer=sr.Recognizer()
            audio=recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                print("you said:", text)
            except sr.UnknownValueError:
                print("Sorry, I didn't understant that!")
            except sr.RequestError:
                print("Sorry, I couldn't request results from the speech recognition server; {0}".format(e))
            except Exception as e:
                print("An error ocurred : {0}".format(e))
                
if __name__=="__main__":
    main()
