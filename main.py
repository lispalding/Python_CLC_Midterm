# PROGRAM NAME: main.py
# PROGRAM PURPOSE: To run the midterm test
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 12-03-2020
# PYTHON VER. USED: 3.8

# Imports
import sys
from datetime import datetime

# Functions
def openFile(fileName,mode):
    """ Opens and returns an open file with the given permissions. To Use: openFile(fileName,mode) """

    # Try block for errors
    try:
        # Opening a file...
        file = open("assets/test_files/"+fileName,mode)
    except IOError as e:
        # Only runs if there is an IO Error
        print("Unable to open the file",fileName+". Ending program... \n",e)
        try:
            time = datetime.now()
            errorTime = time.strftime("%m/%d/%Y %H:%M:%S")

            file = open("assets/errors_log/error_log.txt","a")
            file.write(str(e)+" "+str(errorTime)+"\n")
            input("\n\n Presss the enter key to exit.")
            sys.exit()
        except:
            sys.exit()

    return file

def main():
    file = openFile("example.txt","r")

# Main
main()
