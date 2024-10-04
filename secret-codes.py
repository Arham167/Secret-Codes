import pyttsx3, tkinter as tk
from functools import partial

# Create main window
root = tk.Tk()

# Get info about the height and width of device screen and always open the app in full screen
width = root.winfo_screenwidth() 
height = root.winfo_screenheight()

# Initialize instances for pyttsx3 
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 100)

def main():
    root.title("Secret Codes")
    root.geometry("%dx%d" % (width, height))
    root.state("zoomed")


    # Display the starting texts
    label1 = tk.Label(root, 
                    text="WELCOME ",
                    foreground="azure4",
                    font=("Helvetica",100)
                    )
    label1.pack()
    label2 = tk.Label(root,
                    text="What Do You Want To Do Today?",
                    foreground="cadetblue3",
                    font=("Helvetica",75)
                    )
    label2.pack()

    backbutton = tk.Button(root,
                       text = "Close",
                       command = root.quit
                       )
    backbutton.config(font = ("Helvetica", 15))
    backbutton.place(x = 1, y = 1)

    # Display the starting buttons
    button1 = tk.Button(root,
                        text="Morse Code",
                        command = morse
                        )
    button1.config(font =("Helvetica", 50))
    button1.place(x = 250, y = 375)

    button2 = tk.Button(root,
                        text="Caesar's Cipher",
                        command = caesar
                        )
    button2.config(font =("Helvetica", 50))
    button2.place(x = 750, y = 375)

    root.mainloop()

# Function to go back to the previous window
 
def back(this, previous):
    this.withdraw()
    previous.deiconify()
    previous.state("zoomed")

# Open the window if user clicks morse code
# From here to line 258, all the stuff is of morse code    

def morse():
    # Make a new window and destroy previous one
    global new
    new = tk.Tk()
    root.withdraw()
    new.title("Secret Codes")
    new.geometry("%dx%d" % (width, height))
    new.state("zoomed")

    # Display starting text and new buttons
    label3 = tk.Label(new,
                      text = "Do You Want To Translate English To Morse Code, Or Morse Code To English?",
                      foreground = "aquamarine4",
                      font = ("Helvetica", 30)
                      )
    label3.pack()

    button3 = tk.Button(new,
                        text = "English To Morse Code",
                        command = encrypt
                        )
    button3.config(font =("Helvetica", 50))
    button3.place(x = 400, y = 100)

    button4 = tk.Button(new,
                        text = "Morse Code To English",
                        command = decrypt
                        )
    button4.config(font =("Helvetica", 50))
    button4.place(x = 400, y = 500)

    button5 = tk.Button(new,
                       text = "Back",
                       command = partial(back, new, root)
                       )
    button5.config(font = ("Helvetica", 15))
    button5.place(x = 1, y = 1)

def encrypt():
    # Make a new window and destroy previous one
    global enwindow 
    enwindow = tk.Tk()
    new.withdraw()
    enwindow.title("Secret Codes")
    enwindow.geometry("%dx%d" % (width, height))
    enwindow.state("zoomed")    

    # Display starting text and input area
    label4 = tk.Label(enwindow,
                      text = " Alright, Enter The Text You Want To Convert!",
                      foreground = "thistle4",
                      font = ("Helvetica", 30)
                      )
    label4.pack()
    label5 = tk.Label(enwindow,
                      text = "Input: ",
                      foreground = "gray23",
                      font = ("Helvetica", 25)
                      )
    label5.place(x = 50, y = 100)
    
    global inp
    inp = tk.Text(enwindow,
                  height = 2,
                  width = 70,
                  font = ("Helvetica", 20)
                   )
    inp.place(x = 151, y = 103)

    # Create new button to call a function to convert english to morse
    button6 = tk.Button(enwindow,
                        text = "Convert",
                        command = process_eng
                        )
    button6.config(font =("Helvetica", 20))
    button6.place(x = 600, y = 400)

    # Area for output
    label6 = tk.Label(enwindow,
                      text = "Output: ",
                      foreground = "gray23",
                      font = ("Helvetica", 25)
                      )
    label6.place(x = 40, y = 300)

    global out
    out = tk.Text(enwindow,
                  height = 2,
                  width = 70,
                  font = ("Helvetica", 20)
                )
    out.place(x = 155, y = 303)

    button7 = tk.Button(enwindow,
                       text = "Back",
                       command = partial(back, enwindow, new)
                       )
    button7.config(font = ("Helvetica", 15))
    button7.place(x = 1, y = 1)

def process_eng():
    eng = inp.get("1.0", "end")
    entomor(eng)

def entomor(input):   
    # Dictionary with all the alphabets and numbers and their morse values
    eng_chart = {"a": "._", "b": "_...", "c": "_._.", "d": "_..",
        "e": ".", "f": ".._.", "g": "__.", "h": "....",
        "i": "..", "j": ".___", "k": "_._", "l": "._..",
        "m": "__", "n": "_.", "o": "___", "p": ".__.",
        "q": "__._", "r": "._.", "s": "...", "t": "_",
        "u": ".._", "v": "..._", "w": ".__", "x": "_.._",
        "y": "_.__", "z": "__..", "1": ".____", "2": "..___",
        "3": "...__", "4": "...._", "5": ".....", "6": "_....", 
        "7": "__...", "8": "___..", "9": "____.", "0": "_____"
            }
    
    # Get input and split it into individual letters
    english = ",".join(input.lower())

    # Iterate over each letter and print its morse value with an added space for aesthetics
    for e in reversed(english):
        if e in eng_chart:
            m = eng_chart[e]
            out.insert("1.0", m + " ")

def decrypt():
    # Make a new window and destroy previous one
    global morwindow 
    morwindow = tk.Tk()
    new.withdraw()
    morwindow.title("Secret Codes")
    morwindow.geometry("%dx%d" % (width, height))  
    morwindow.state("zoomed")  

    # Display starting text and input area
    label7 = tk.Label(morwindow,
                      text = "Alright, Enter The Text You Want To Convert!",
                      foreground = "thistle4",
                      font = ("Helvetica", 30)
                      )
    label7.pack()
    label8 = tk.Label(morwindow,
                      text = "(With A Space After Each Letter!)",
                      foreground = "thistle4",
                      font = ("Helvetica", 20))
    label8.place(x = 500, y = 70)

    label9 = tk.Label(morwindow,
                      text = "Input: ",
                      foreground = "gray23",
                      font = ("Helvetica", 25)
                      )
    label9.place(x = 50, y = 100)
    
    global inp
    inp = tk.Text(morwindow,
                  height = 2,
                  width = 70,
                  font = ("Helvetica", 20)
                   )
    inp.place(x = 151, y = 103)

    # Create new button to call function to convert morse to english
    button8 = tk.Button(morwindow,
                        text = "Convert",
                        command = process_mor
                        )
    button8.config(font =("Helvetica", 20))
    button8.place(x = 600, y = 400)

    # Area for output
    label10 = tk.Label(morwindow,
                      text = "Output: ",
                      foreground = "gray23",
                      font = ("Helvetica", 25)
                      )
    label10.place(x = 40, y = 300)

    global out
    out = tk.Text(morwindow,
                  height = 2,
                  width = 70,
                  font = ("Helvetica", 20)
                )
    out.place(x = 155, y = 303)

    button9 = tk.Button(morwindow,
                       text = "Back",
                       command = partial(back, morwindow, new)
                       )
    button9.config(font = ("Helvetica", 15))
    button9.place(x = 1, y = 1)

def process_mor():
    mor = inp.get("1.0", "end")
    mortoen(mor)

def mortoen(input):
    # Dictionary with all morse values with their alphabets and numbers
    mor_chart = {"._": "a", "_...": "b", "_._.": "c", "_..": "d",
        ".": "e", ".._.": "f", "__.": "g", "....": "h",
        "..": "i", ".___": "j", "_._": "k", "._..": "l",
        "__": "m", "_.": "n", "___": "o", ".__.": "p",
        "__._": "q", "._.": "r", "...": "s", "_": "t",
        ".._": "u", "..._": "v", ".__": "w", "_.._": "x",
        "_.__": "y", "__..": "z", "._____": "1", "..___": "2",
        "...__": "3", "...._": "4", ".....": "5", "_....": "6", 
        "__...": "7", "___..": "8", "____.": "9", "_____": "0"
            }
    # Get input and split it into individual letters
    morse = input.split(" ")
    e = ""
    
    # Iterate over each letter and print its english value with an added space for aesthetics
    for m in morse:
        if m in mor_chart:
            e += mor_chart[m]
    
    out.insert("end", e)

    # Button for speaking the english
    button10 = tk.Button(morwindow, 
                         text = "Listen",
                         command = partial(speakeng, e)          
                        )
    button10.config(font =("Helvetica", 26))
    button10.place(x = 1250, y = 300)

# Function for speaking the english values
def speakeng(e):
    engine.say(e)
    engine.runAndWait()

# Open the window if user clicks caesar's cipher
# Now from here to the end is all of Caesar's cipher
    
def caesar():
    # Make a new window and destroy previous one
    global new
    new = tk.Tk()
    root.withdraw()
    new.title("Secret Codes")
    new.geometry("%dx%d" % (width, height))
    new.state("zoomed")

    # Display starting text and input area
    label11 = tk.Label(new,
                      text = "How Much Do You Want To Shift The Letters?",
                      foreground = "aquamarine4",
                      font = ("Helvetica", 30)
                      )
    label11.place(x = 400, y = 50)

    global n
    n= tk.Entry(new, 
                width = 8,
                font = ("Helvetica", 20)
                )
    n.place(x = 650, y = 110)
    
    # Create new button to call a function to shift with the given key
    button11 = tk.Button(new,
                        text = "Enter",
                        command = inpt
                        )
    button11.config(font =("Helvetica", 15))
    button11.place(x = 800, y = 110)

    button12 = tk.Button(new,
                       text = "Back",
                       command = partial(back, new, root)
                       )
    button12.config(font = ("Helvetica", 15))
    button12.place(x = 1, y = 1)

def inpt():
    # Display starting text and input area
    label12 = tk.Label(new,
                      text = " Alright, Enter The Text You Want To Convert!",
                      foreground = "thistle4",
                      font = ("Helvetica", 30)
                      )
    label12.place(x = 400, y = 200)

    global key
    key = n.get()
    key = int(key)

    label13 = tk.Label(new,
                      text = "Plaintext: ",
                      foreground = "gray23",
                      font = ("Helvetica", 22)
                      )
    label13.place(x = 100, y = 300)

    global inpu
    inpu = tk.Text(new,
                  height = 1,
                  width = 70, 
                  font = ("Helvetica", 20)
                  )
    inpu.place(x = 250, y = 300)

    # Create new button to call a function to shift with the given key
    button14 = tk.Button(new,
                        text = "Shift",
                        command = process_plain
                        )
    button14.config(font =("Helvetica", 17))
    button14.place(x = 700, y = 500)

    label14 = tk.Label(new,
                      text = "Ciphertext: ",
                      foreground = "gray23",
                      font = ("Helvetica", 22))
    label14.place(x = 100, y = 400)

    global outp
    outp = tk.Text(new,
                  height = 1,
                  width = 70,
                  font = ("Helvetica", 20)
                )
    outp.place(x = 250, y = 400)

def process_plain():
    original = inpu.get("1.0", "end") 
    shift(original, key)

def shift(original, key): 
    shifted = ""

    for i in range(len(original)):
        ch = original[i]
        if (ch.isupper()):
            shifted += chr((ord(ch) + int(key) - 65) % 26 + 65)
        elif (ch.islower()):
            shifted += chr((ord(ch) + int(key) - 97) % 26 + 97)
        else:
            shifted += ch

    outp.insert("1.0", shifted)

    button15 = tk.Button(new,
                        text = "Listen",
                        command = partial(speakcipher, shifted)
                        )
    button15.config(font =("Helvetica", 15))
    button15.place(x = 1350, y = 400)


def speakcipher(shifted):
    engine.say(shifted)
    engine.runAndWait()
    
if __name__ == "__main__":
    main()