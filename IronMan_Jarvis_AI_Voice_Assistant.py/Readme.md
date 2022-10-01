# Iron Man Jarvis AI Desktop Voice Assistant using Python.

What can this A.I. assistant do for you?
It can send emails on your behalf.
It can play music for you.
It can do Wikipedia searches for you.
It is capable of opening websites like Google, Youtube, etc., in a web browser.
It is capable of opening your code editor or IDE with a single voice command.

# Enough talks! Let's start building our own J.A.R.V.I.S.

- Defining Speak Function:
The first and foremost thing for an A.I. assistant is that it should be able to speak. To make our J.A.R.V.I.S. talk, we will make a function called speak(). This function will take audio as an argument, and then it will pronounce it.
- Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made. We are going to install a module called pyttsx3.
- Writing Our speak() Function :
We made a function called speak() at the starting of this tutorial. Now, we will write our speak() function to convert our text to speech.
- Creating Our main() function: 
We will create a main() function, and inside this main() Function, we will call our speak function.
- Defining Wish me Function :
Now, we will make a wishme() function that will make our J.A.R.V.I.S. wish or greet the user according to the time of computer or pc. To provide current or live time to A.I., we need to import a module called datetime. 
- Defining Take command Function :
The next most important thing for our A.I. assistant is that it should take command with the help of the microphone of the user's system. So, now we will make a takeCommand() function.  With the help of the takeCommand() function, our A.I. assistant will return a string output by taking microphone input from the user.

 Before defining the takeCommand() function, we need to install a module called speechRecognition.
-  Coding logic of Jarvis
 Now, we will develop logic for different commands such as Wikipedia searches, playing music, etc.
 - Defining Task 1: To search something on Wikipedia -
 To do Wikipedia searches, we need to install and import the Wikipedia module into our program.
 - Defining Task 2: To open YouTube site in a web-browser -
 To open any website, we need to import a module called webbrowser. It is an in-built module, and we do not need to install it with a pip statement; we can directly import it into our program by writing an import statement.
 Code: 

     elif 'open youtube' in query:
            webbrowser.open("youtube.com")

Here, we are using an elif loop to check whether Youtube is in the user's query. Let' suppose the user gives a command as "J.A.R.V.I.S., open youtube." So, open youtube will be in the user's query, and the elif condition will be true.

- Defining Task 3: To open Google site in a web-browser -
Code:
elif 'open google' in query:
            webbrowser.open("google.com")

-  Defining Task 4: To play music -
To play music, we need to import a module called os. Import this module directly with an import statement.
- Defining Task 5: To know the current time
Code:
  elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

In the above, code we are using the datetime() function and storing the current or live system time into a variable called strTime. After storing the time in strTime, we are passing this variable as an argument in speak function. Now, the time string will be converted into speech.
-  Defining Task 6: To open the VS Code Program
 elif 'open code' in query:
            codePath = "C:\Users\paman\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)
To open the VS Code or any other application, we need the code path of the application.

- Defining Task 7: To send Email
To send an email, we need to import a module called smtplib.

What is smtplib?

Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and route emails between mail servers. An instance method called sendmail is present in the SMTP module. This instance method allows us to send an email.  It takes 3 parameters:
- The sender: Email address of the sender.
- The receiver: T Email of the receiver.
- The message: A string message which needs to be sent to one or more than one recipient.

- Defining Send email function :
We will create a sendEmail() function, which will help us send emails to one or more than one recipient.
code:
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
In the above code, we are using the SMTP module, which we have already discussed above.
Note: Do not forget to 'enable the less secure apps' feature in your Gmail account. Otherwise, the sendEmail function will not work properly.

Calling sendEmail() function inside the main() function: 
code:   
 elif 'email to aman' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")  

We are using the try and except block to handle any possible error while sending emails.

# Is it an A.I.?
Many people will argue that the virtual assistant that we have created is not an A.I, but it is the output of a bunch of the statement. But, if we look at the fundamental level, the sole purpose of A.I develop machines that can perform human tasks with the same effectiveness or even more effectively than humans.

It is a fact that our virtual assistant is not a very good example of A.I., but it is an A.I.!

# With this, we have successfully made our very first virtual assistant. 






























