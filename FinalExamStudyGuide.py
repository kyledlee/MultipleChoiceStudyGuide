# Kyle Lee
# Multiple Choice Program to help study for CS112 Final
# 5/31/18
import random

# Input file format:
# Line 1: Question
# Line 2: Answer (A)
# Line 3: Answer (B)
# Line 4: Answer (C)
# Line 5: Answer (D)
# Line 6: Correct answer letter (a, b, c, d)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For longer questions, use '\n' to indicate a new line


filename = 'questions.txt'
with open(filename) as f:
    Questions = f.readlines()

print('[%s]' % ', '.join(map(str, Questions)))

if(len(Questions)%6 != 0):
    print("ERROR: input file not formatted correctly! Questions are not organized in groups of 6!")
    print("Exiting...")
    exit()

'''
def printQuestion(i, Questions):
    splitQuestions = Questions[i].split("\\n")
    print('\n'.join(map(str, splitQuestions)))

#main
#make random order mode, and normal order mode.
print("Welcome to the Multiple Choice Study Program for CS112.")
inputtingMode = True

while inputtingMode:
    mode = input("Enter 'n' for normal order operation, and 'r' for random order operation.\n")
    if (mode == 'r' or mode == 'n'):
        inputtingMode = False
    else:
        print("Please respond with either 'n' or 'r'.")

testing = True
numAttempted = 0
numCorrect = 0

i = 0
while testing:
    if(mode == 'r'):
        i = (random.randint(1,len(Questions)-1))
        i2 = (i % 6)
        i = i-i2
    if(testing):
        '''
        print(Questions[i])
        '''

        printQuestion(i, Questions)

        for j in range(1,5):
            print('('+chr(64+j)+") "+Questions[i+j])

        answer = input()
        if(answer == 'e'):
            testing = False
        elif (str(answer) == str(Questions[i+5]).rstrip()):
            print("Correct! The answer is " + Questions[i+(ord(str(Questions[i+5]).rstrip()[0])-96)].rstrip() + ". \n")
            numAttempted += 1
            numCorrect += 1
        else:
            print("Wrong! The answer is " + Questions[i+(ord(str(Questions[i+5]).rstrip()[0])-96)].rstrip() + ". \n" )
            numAttempted += 1
        if(mode == 'n'):
            i = i + 6
        if(i>(len(Questions)-1)):
            testing = False


print("Exiting...")

if(numAttempted > 0):
    print("You got " + str(numCorrect) + " out of " + str(numAttempted) + " correct! (" + str((numCorrect/numAttempted)*100) + "%)")

