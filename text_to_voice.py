import tkinter as tk
import pyttsx3
import speech_recognition as sr



root = tk.Tk()
root.geometry("900x900")
root.title("Text-To-Speech App")

h = tk.Label(root, text="Enter text-to-speech below.")
h.pack()

a = tk.Entry(root)
a.pack()

def submit():
    user = a.get()
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(user)
    engine.runAndWait()

b = tk.Button(root, command=submit, text="Submit")
b.pack()

def respond():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
    try:
      text = recognizer.recognize_google(audio)
      print("You said:", text)
    except sr.UnknownValueError:
       print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
       print(f"API error: {e}")



x = tk.Button(root, command=respond, text="Respond")
x.pack()

def quit_():
    root.destroy()


quit = tk.Button(root, command=quit_, text="Exit")
quit.pack()

root.mainloop()
