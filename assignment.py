#!python3
# Volume Calculator
# Feel free to rename your variables

import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts
    
    
    if shape == "cube":
        # Formula: V = L^3
        cubelist = ["Enter the length"]
        return cubelist

    if shape == "cylinder":
        # Formula: V = πr^2h
        cylinderlist = ["Enter the radius", "Enter the height"]
        return cylinderlist

    if shape == "cone":
        # Formula: V = πr^2(h/3)
        conelist = ["Enter the radius", "Enter the height"]
        return conelist

    if shape == "rectangular prism":
        # Formula: V = whL
        rectangularlist = ["Enter the length", "Enter the width", "Enter the height"]
        return rectangularlist

    if shape == "sphere":
        # Formula: V = (4/3)πr^3
        spherelist = ["Enter the radius"]
        return spherelist

    if shape == "triangular prism":
        # Formula: V = (1/2)bhL
        triangularlist = ["Enter the base", "Enter the height", "Enter the length"]
        return triangularlist

    if shape == "pyramid":
        # Formula: V = (Lwh)/3
        pyramid = ["Enter the length", "Enter the width", "Enter the height"]
        return pyramid

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