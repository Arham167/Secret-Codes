# SECRET CODES #
#### Video Demo: <https://youtu.be/9UOk1ht8G5A> ####
#### Description: ####

This is a program that can take **English** input and convert it to **Morse Code** and also take **Morse Code** and convert it to **English**. It can also do **Caesar's Cipher** and shift the input according to the key provided by the user.

I wanted to make a GUI application so I looked through many different libraries. First I used *PySimpleGUI* but it didn't feel right so I decided on using *Tkinter*. I also wanted to add options for voice input and output so I installed the *pyttsx3* library. But in the end I could only manage the output bit. I couldn't figure out how to test voice input because my microphone was not working.

I also used the built-in library *functools* for the function *partial* so I could make buttons that took arguments for additional functionality.

The whole code is around *400 lines* long and contains *14 functions* apart from the "main function". Some of those functions are fundamentally the same with just a few changes. And I had to add three extra functions, *process_eng, process_mor* and *process_plain* to make the tests for this project.

In the first few lines, I initialized the tkinter window and the pyttsx3 engine. On lines 8 & 9, I accessed the width and height of the window and used that information further ahead in my code to make sure that the window always opened in full screen.

In the main function, I displayed some starting texts and two buttons. At first, there was only 1 button for Morse Code but I decided a few days later to also add Caesar's Cipher. So I added the second button after that.

The first function after the main function is the ***back*** Function. It is a very short one, but it was very useful. It takes two arguments, the window currently open and the one that was previously open. It then hides the current one and opens the previous one. 

The second function is called ***morse*** and it is called if the user clicks the button called *Morse Code* in the main window. This function opens a new window, with two more buttons, named *English To Morse Code* & *Morse Code To English*. If the user clicks Englush To Morse Code then the function ***encrypt*** is called and if Morse Code To English is clicked then the function ***decrypt***. Both of these functions open a new window which are fundamentally the inverse of each other.

The *encrypt* function opens a window and displays two text boxes labelled input and output. When the user types in the input text box and clicks the *Convert* button, the function called ***process_eng*** is called. This function only has one useful line which takes the input from the text box and assigns it to a variable. I had to add this so I could pass this variable as an argument to the ***entomor*** function, because I had to make tests for this function and I had to pass arguments. This line of code that took input and assigned it to the variable was originally in the *entomor* function itself.

After the *process_eng* function takes input and assigns it, it calls the *entomor* function. In this function, there is a library that has key-value pairs of English letters and numbers and their corresponding Morse Code values. I used the idea of splitting or joining lists and decided to use the .join() method. It takes the input as a list and then adds a "," after each element of the list, namely each letter of the word that was given. After this, I used a *for loop* to go over each letter, check it against the dictionary and if a match is found, assign it to the variable. Then I inserted that variable to the text box and thus the input is converted into Morse Code.

The *decrypt* function is basically the same as the *encrypt* one; it opens a window with input and output areas, when the *Convert* button is clicked, calls the function ***process_mor***. This function is also basically the same and was made so I could do tests. Then the function ***mortoen*** is called, which has a similar dictionary with Morse Code keys and their English or numeric values. But this function does not join a "," after each letter. It splits the input on every blank space it encounters and makes a list. Then I declared an empty string, used a similar *for loop* to iterate over the list and then added the answer to the string. After that the string is inserted to the output text box.

Then there is a function called ***speakeng*** that is called if the user clicks the button called *Speak* after the Morse Code has been converted to English, and it just speaks the English by using the *Pyttsx3* library.

All of these functions were called if the user clicks the button called *Morse Code* in the starting window. But if the user clicks the button *Caesar's Cipher*, then the function ***caesar*** is called.

This function opens a new window and first displays an input area for the user to input a *key*; which is the number by which they want to shift the input. After giving the key and clicking the button named *Enter*, the function ***inpt*** is called. This function takes the key and converts it into an *int* and displays input and output areas.

After the user gives input and clicks the *Shift* button, the function called ***process_plain*** is called. This is also pretty straight-forward; just takes input from the text box and passes it as an argument for the function ***shift***.

The *shift* function takes two arguments, the input user provided and the key. It first declares an empty string and then iterates over the input using a *for loop*. Then it checks if the input letter is uppercase or lowercase or a special character, in order to preserve the order and case. Then I used the chr() and ord() methods to convert the input to an *int* and back again to do operations such as adding the key and others. After this the resulting character is added to the empty string and then the string is inserted to the output box.

After that, a button called *Speak* is displayed that calls the function called ***speakcipher*** that is the same as *speakenf*; it speaks the shifted output by using the *pyttsx3* library.

That was a summary of my program, with a brief breakdown of each function. 
