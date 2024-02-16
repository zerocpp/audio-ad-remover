# 需要安装speech_recognition库
# pip install SpeechRecognition
import speech_recognition as sr

wav_path = './audio/001.wav'

# 初始化识别器
r = sr.Recognizer()

# 从音频文件中加载音频数据
with sr.AudioFile(wav_path) as source:
    audio_data = r.record(source)

# 使用Google Web Speech API进行识别
text = r.recognize_google(audio_data, language="en-US")

print(text)
