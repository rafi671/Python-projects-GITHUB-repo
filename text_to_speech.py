import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

l = ["Leonard", "Ali", "George", "Bob"]

for name in l:
    shoutout = "Shout out to " + name
    speak.Speak(shoutout)