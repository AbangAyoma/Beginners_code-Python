# 7.2 Write a program that prompts for a file name, then opens that file and
#  reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute 
# the average of those values and produce an output as shown below. Do not use the sum() function 
# or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are
#  testing below enter mbox-short.txt as the file name

userInput = input('Please Enter a text, Eg mbox-short.txt: ')
userInputOpened = open(userInput)
sumOfNumbers = 0
numberOfLines = 0
for line in userInputOpened:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    numberOfLines = numberOfLines  +1
    findDelimeter = line.find(":")
    floatOfNumber = float(line[findDelimeter + 2 : ])
    sumOfNumbers = sumOfNumbers + floatOfNumber
    print(numberOfLines, floatOfNumber, sumOfNumbers,)
average = numberOfLines / sumOfNumbers
print(average)
print("Done")
