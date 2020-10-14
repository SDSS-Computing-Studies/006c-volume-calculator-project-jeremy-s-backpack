#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Naomi
    # Modified:
    print("  ____________________________________ ")
    print(" |                                    |")
    print(" | ================================== |")
    print(" |  WELCOME TO THE VOLUME CALCULATOR  |")
    print(" | ================================== |")
    print(" |    ___     ___     ___     ____    |")
    print(" |   |_(_|   |_)_|   |_%_|   |_AC_|   |")
    print(" |                                    |")
    print(" |    ___     ___     ___     ___     |")
    print(" |   |_7_|   |_8_|   |_9_|   |_/_|    |")
    print(" |                                    |")
    print(" |    ___     ___     ___     ___     |")
    print(" |   |_4_|   |_5_|   |_6_|   |_*_|    |")
    print(" |                                    |")
    print(" |    ___     ___     ___     ___     |")
    print(" |   |_1_|   |_2_|   |_3_|   |_-_|    |")
    print(" |                                    |")
    print(" |    ___     ___     ___     ___     |")
    print(" |   |_0_|   |_._|   |_=_|   |_+_|    |")
    print(" |                                    |")
    print(" |____________________________________|")
    
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Naomi
    # Modified:
    print("==================")
    print("HOW TO USE: ")
    print("==================")
    print('1. Choose any of the "shape" options given to you')
    print("2. The calculator ")
    print("")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()

main()