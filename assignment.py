#!python3
# Volume Calculator
# Feel free to rename your variables

import math
shape=''
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
    # Author: Naomi, John
    # Modified: (number 2 - John)
    print("===========")
    print("HOW TO USE: ")
    print("===========")
    print('1. Choose any of the "shape" options given to you\n')
    print("2. Once you have chosen your shapes we will ask you to enter ")
    print("   numbers based on the parametres needed for the chosen shape.\n")
    print("3. Once you have entered all of the parametres the volume of your ")
    print("   shape will be calculated and rounded to the nearset tenth.\n")
    print("The shapes:\n -cube\n -cylinder\n -cone\n -rectangular prism\n -sphere\n -triangular prism\n -pyramid\n")
    
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    # Author: John
    
    
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

def getInputs(shape):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    #Author: Jeremy
    
    
    questions=getParams(shape)
    print(questions)
    numInd=len(questions)
    meList=[]
    num1=0
    for i in range(0,numInd):
        num1=float(input("Enter dimension "+str(i+1)+": "))
        meList.insert(i,num1)
    measurements=meList    
    
    return measurements

def calc(lis):
    #Author: John and Jeremy
    li2=lis
    if shape=="cube":
        # Formula: V = L^3
        side=li2[0]
        answer=side**3
        answer=round(answer,2)
        return answer
    if shape=="cylinder":
        # Formula: V = πr^2h
        r=li2[0]
        he=li2[1]
        answer=(math.pi * (r**2))*he
        answer=round(answer,2)
        return answer
    if shape=="cone":
        # Formula: V = πr^2(h/3)
        r=li2[0]
        h=li2[1]
        num1=(h/3)
        num2=math.pi*(r**2)
        answer=num1*num2
        answer=round(answer,2)
        return answer
    if shape=="rectangular prism":
        # Formula: V = whL
        l=li2[0]
        w=li2[1]
        h=li2[2]
        answer=l*w*h
        answer=round(answer,2)
        return answer
    if shape=="sphere":
        # Formula: V = (4/3)πr^3
        r=li2[0]
        num1=4/3
        answer=num1*math.pi*(r**3)
        answer=round(answer,2)
        return answer
    if shape=="triangular prism":
        # Formula: V = (1/2)bhL
        base = li2[0]
        height = li2[1]
        length = li2[2]

        answer = 0.5*base*height*length
        answer = round(answer,2)
        return answer
        
    if shape=="pyramid":
        # Formula: V = (Lwh)/3
        length = li2[0]
        width = li2[1]
        height = li2[2]

        answer = (length*width*height)/3
        answer = round(answer,2)
        return answer
    



def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    
    shape=input("Enter the shape you want to calculate the volume of: ")

    lis=getInputs(shape)
    num=calc(lis)
    num = print(num)
    return num



main()

