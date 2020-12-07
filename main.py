# PROGRAM NAME: main.py
# PROGRAM PURPOSE: To run the midterm test
# MADE BY: Lisette Spalding
# DATE CREATED: 12-03-2020
# DATE LAST MODIFIED: 12-07-2020
# PYTHON VER. USED: 3.8

# Imports
import sys
from datetime import datetime

################################## TEST VAR ###################################

file = "example_test.txt" # You will need to change this variable to match the file name you're using

##################################### FIN #####################################


################################## FUNCTIONS ##################################

# Defining a function to open the test file
def openFile(fileName,mode):
    """ Opens and returns an open file with the given permissions. To Use: openFile(fileName,mode) """

    # Try block for errors
    try:
        # Opening a file...
        file = open("assets/test_files/"+fileName,mode)
    except IOError as e:
        # Only runs if there is an IO Error
        print("Unable to open the file",fileName+". Ending program... \n",e)
        try: # Making the program check for errors
            time = datetime.now() # Getting the time
            errorTime = time.strftime("%m/%d/%Y %H:%M:%S") # Making the time format readable

            # Writing the error to error file
            file = open("assets/errors_log/error_log.txt","a")
            file.write(str(e)+" "+str(errorTime)+"\n")

            # Getting user input for the system exit
            input("\n\n Presss the enter key to exit.")
            sys.exit() # Exiting the program
        except: # If we get an unidentifiable error
            sys.exit() # Exiting the program

    return file

# Creating a function to get a good name
def getName():
    """ Gets a good name from the user as well as the users start time for the test. To use: getName() """
    
    time = datetime.now() # Getting the time
    testTime = time.strftime("%m/%d %H:%M") # Making the time format readable

    # Making sure that we get a good name...
    while True:
        name = input("Enter your first and last name.   ") # Getting user input

        # Setting up an if statement to check if the name is valid
        if len(name) >= 3 and " " in name:
            name = name.title() # Converting the name to title case
            return name, testTime # Returning valid name and test time
        else:
            print("That's not a good name! Try again.") # Shaming the user for putting in an invalid name

# Creating a function to make the file present all nice and pretty
def nextLine(file):
    """ Makes the text file with the test look nice. To use: nextLine(file) """
    
    try: # Trying to replace all / with an enter key
        line = file.readline()
        line = line.replace("/","\n")
        return line # Returning the line
    except: # This will happen if something goes wrong
        print("Something went wrong while reading a line from the file...")
        sys.exit() # Exiting the program

def questionBlock(file):
    """ Defines the question block """

    # Defining the question block variables
    category = nextLine(file) # Category is first so we'll call it first
    question = nextLine(file) # Question is second (in the file) so we'll call it second
    
    # Setting the choices to a list
    choices = []
    for i in range(4): # For four lines, the question choices will be read
        choices.append(nextLine(file)) # Appending the question choices to choices
    
    correct = nextLine(file) # Setting the correct
    if correct: # Making sure that there is a correct answer
        correct = correct[0]

    explination = nextLine(file) # Setting the explination

    return category,question,choices,correct,explination # Returning every variable in the question block

def welcome(name,title,time):
    """ Welcoming the test taker. To use: welcome() """

    print("Welcome, " + name + " to your Mid Term Exam!") # Printing test takers name, successfully welcoming them to the exam
    print("Your test was started at: " + time) # Telling them what time they started

# Defining a function to write to a file (Report card)
def reportCard(name,time,score,totalQuestions):
    """ Creating a report card for the test taker. To use: reportCard(name,score,totalQuestions) """
    
    # Using a try block for errors
    try:
        # Setting file variable
        file = openFile("assets/report_cards/"+name,"w")
        # Getting current time
        time = datetime.now() # Getting the time
        endTime = time.strftime("%m/%d/%Y %H:%M:%S") # Making the time format readable

        # Writing the file...
        file.write("Name: "+name)
        file.write("Time test was started: "+time)
        file.write("End Time: "+endTime)
        file.write("Score (Total correct): "+score)
        file.write("Total Questions: "+totalQuestions)

        # Creating my percent variable
        percent = score/totalQuestions*100
        # Determining letter grade
        if percent >=90:
            letter = "A"
        elif percent >= 80:
            letter = "B"
        elif percent >= 70:
            letter = "C"
        elif percent >= 60:
            letter = "D"
        else:
            letter = "F"

        # Writing to file...
        file.write("Percentage: "+percent)
        file.write("Letter grade: "+letter)
        
        file.close() # Closing file
    except:
        print("There was an error while writing the report card.")
        sys.exit() # Exiting the program

# Defining the main function
def main(file):
    """ The main entry point for the test. To use: main(file) """

    ########## MAIN VARIABLES ##########

    score = 0
    totalQuestions = 0
    
    name, time = getName() # Getting the name of the test taker
    file = openFile(file,"r") # Opening the file
    title = nextLine(file) # Getting the title
    welcome(name,title,time) # Welcoming the test taker
    category,question,choices,correct,explination =  questionBlock(file) # Getting a ton of variables

    #### TEST START ####

    while category: # Making sure that the category is up
        totalQuestions += 1 # Add one to total questions every time you get a new question

        # Printing stuff
        print("\t\t",category,"\n")
        print(question)

        # Making sure that we can print the choices
        for i in range(len(choices)):
            # Printing choices
            print(str.format("\t{}:     {}",i+1,choices[i]))

        answer = input("What is your answer?   ") # Getting an answer
        # Checking answer
        if answer == correct:
            print("\nRight!",end=" ")
            score += 1
        else:
            print("\nWrong.",end=" ")

        print(explination)
        print("Score:",score,"\n\n")

        category,question,choices,correct,explination =  questionBlock(file)

    ####### FIN #######

    # Closing the file
    file.close()

    # Finishing the game...
    print("That was the last question!")
    print("Your final score is: ",score)
    print("Your report card was created at the following location:")
    print("assets/report_cards/"+name+".txt")

    # Creating the report card
    reportCard(name,time,score,totalQuestions)

    ############### FIN ###############
    

##################################### FIN #####################################

# Main
main(file)
