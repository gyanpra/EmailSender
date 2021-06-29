import speech_recognition as sr 
import yagmail

recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise...Please wait')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording')

try:
    print('Printing your message...Please wait')
    text=recognizer.recognize_google(recordedaudio,language='en-US')
    print('Your Message:{}',format(text))

except Exception as ex:
    print(ex)

#Mail Autamation
reciever='gyanp008@gmail.com'
message=text
sender=yagmail.SMTP('pgyan666@gmail.com')
sender.send(to=reciever,subject='This is voice translated mail',contents=message)