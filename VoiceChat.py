import openai
import pyttsx3
import speech_recognition as sr

#set OpenAI API Key
openai.api_key = "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"
model_id = "gpt-3.5-turbo"

print("gpt version:", openai.api_version)

# Initialize the text to speech engine 
engine=pyttsx3.init()
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate-50)

#voices = engine.getProperty('voices')

'''
这段代码定义了一个名为 transcribe_audio_to_text 的函数，用于将音频文件转录为文本。它使用
SpeechRecognition 库创建一个 Recognizer 对象，然后使用该对象打开音频文件并记录音频。接下来，
它尝试使用支持中文（繁体）和英语语言的Google语音识别API来转录音频。如果在转录过程中出现错误，
函数会打印一条消息，指示它正在跳过未知错误。该函数返回转录的文本。
'''
def transcribe_audio_to_text(filename):
    recogizer=sr.Recognizer()
    with sr.AudioFile(filename)as source:
        audio=recogizer.record(source) 
    try:
        return recogizer.recognize_google(audio, language="zh-TW, en-US")
    except:
        print("skipping unkown error")

'''
这段代码定义了一个名为 generate_response 的函数，用于生成OpenAI的文本回复。
它使用OpenAI的API创建一个 Completion 对象，并传入一个提示作为参数。然后，它
使用该对象的 create 方法来生成一个文本回复。该函数返回回复的文本。
'''
def generate_response(prompt):
    response= openai.Completion.create(
        engine="text-davinci-003",
#        engine="text-curie-001",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response["choices"][0]["text"]
#    return response.choices[0].message.content

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
'''
def main():
    while True:
        #Waith for user say "genius"
        print("請說'媽寶' 開始記錄你的對話, '結束'關閉應用程序")
        with sr.Microphone() as source:
            recognizer=sr.Recognizer()
            audio=recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language="zh-TW")
                print("你說:", command)
                if command.lower()=="媽寶":
                    #record audio
                    filename ="input.wav"
                    print("你想問什麼?")
                    with sr.Microphone() as source:
                        recognizer=sr.Recognizer()
                        source.pause_threshold=5
                        audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)
                        with open(filename,"wb")as f:
                            f.write(audio.get_wav_data())
                        
                    #transcript audio to test 
                    text=transcribe_audio_to_text(filename)
                    if text:
                        print(f"你說: {text}")
                        
                        #Generate the response
                        response = generate_response(text)
                        print(f"ChatGPT-3 說: {response}")
                            
                        #read resopnse using GPT3
                        speak_text(response)
                else: 
                    if command.lower()=="結束":
                        print("關閉應用程序")
                        exit()
            except sr.UnknownValueError as e:
                print("Sorry, I didn't understant that!")
            except sr.RequestError as e:
                print("Sorry, I couldn't request results from the speech recognition server; {0}".format(e))
            except Exception as e:
                print("An error ocurred : {}".format(e))
'''                
def main():
    while True:
        #Wait for user say "genius"
        print("請說'康寶' 開始記錄你的對話, '結束'關閉應用程序")
        with sr.Microphone() as source:
            recognizer=sr.Recognizer()
            audio=recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio, language="zh-TW")
                print("你說:", command)
                if command.lower()=="康寶":
                    while True:
                        #record audio
                        filename ="input.wav"
                        print("你想問什麼?")
                        with sr.Microphone() as source:
                            recognizer=sr.Recognizer()
                            source.pause_threshold=5
                            audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)
                            with open(filename,"wb")as f:
                                f.write(audio.get_wav_data())
                            
                        #transcript audio to text 
                        text=transcribe_audio_to_text(filename)
                        if text:
                            print(f"你說: {text}")
                            if text =="停止":
                                speak_text("停止目前對話")
                                break
                               
                            #Generate the response
                            response = generate_response(text)
                            print(f"ChatGPT-3 說: {response}")
                                
                            #read resopnse using GPT3
                            speak_text(response)
                else: 
                    if command.lower()=="結束":
                        print("關閉應用程序")
                        speak_text("感謝您, 再見")
                        exit()
            except sr.UnknownValueError as e:
                print("Sorry, I didn't understant that!")
            except sr.RequestError as e:
                print("Sorry, I couldn't request results from the speech recognition server; {0}".format(e))
            except Exception as e:
                print("An error ocurred : {}".format(e))

if __name__=="__main__":
    main()
