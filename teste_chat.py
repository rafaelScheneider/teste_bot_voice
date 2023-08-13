import speech_recognition as sr
import pyttsx3
import subprocess
r = sr.Recognizer()
 
def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     

atender = False

while(1):   
    if atender == False:
        try:
            # Microfone
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                audio2 = r.listen(source2)
                
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
    
                print("Did you say ",MyText)
                if 'okay' in MyText:
                    atender = True
                    speak_text('Did you called me?')
                
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")
            
    else:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                audio2 = r.listen(source2)
                
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                if 'open' in MyText:
                    subprocess.call(["C:/Users/gabri/Desktop/Opera_GX_Rafael.lnk"], shell=True)
                    speak_text('Opening Opera GX')
                    atender = False
                elif 'vegas' in MyText:
                    subprocess.call(["C:/Users/gabri/Desktop/Fallout New Vegas.url"], shell=True)
                    speak_text('Opening Fallout New Vegas')
                    atender = False
                else:
                    speak_text('Could you repeat?')
                    
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")