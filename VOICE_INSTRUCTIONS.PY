import pyttsx3
import os
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.runAndWait()
print("...")
engine.say("Welcome!!!")
print("")
print("\n\t 1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.GOOGLE CHROME \n\t 5.VLC PLAYER \n\t 6.NOTEPAD  \n\n\t\t     0. FOR EXIT")
pyttsx3.speak("Welcome to my tools")
print("")
pyttsx3.speak("chat with me with your requirements")
while True:
    print("    CHAT WITH ME WITH YOUR REQUIREMENTS : ", end='')
    p = input()
    p = p.upper()
    print(p)
    if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        pyttsx3.speak("Type Again")
        continue
    elif ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or ("4" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("GOOGLE CHROME")
        os.system("chrome")
 
    elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("9" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("NOTEPAD")
        os.system("Notepad")
 
    elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p) or ("5" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("VLC PLAYER")
        os.system("VLC")
 
    elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p) or ("3" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT EXCEL")
        os.system("excel")
 
    elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p) or ("2" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT POWERPOINT")
        os.system("powerpnt")
 
    elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("MICROSOFT WORD")
        os.system("winword")
    elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
        pyttsx3.speak("Exiting")
        break
    else:
        pyttsx3.speak(p)
        print("Is Invalid,Please Try Again")
        pyttsx3.speak("is Invalid,Please try again")
        print(".")
        print(".")