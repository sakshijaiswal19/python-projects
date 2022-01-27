import pyttsx3

f=open('audiotext.txt','r')

engine=pyttsx3.init()
engine.setProperty('rate',300)
voices=engine.getProperty('voices')

#female voice
engine.setProperty('voice',voices[1].id)

#male voice
# engine.setProperty('voice',voices[0].id)

engine.save_to_file(f.read(),'book.mp3')
engine.runAndWait()
engine.stop()
