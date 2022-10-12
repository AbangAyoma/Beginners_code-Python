# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail. The program
# creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. After 
# the dictionary is produced, the program reads through the 
# dictionary using a maximum loop to find the most prolific 
# committer.

mostFrequentWord = None
totalNumberOfTimes = 0
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
sender = dict()
handle = open(name)
for line in handle :
    if not line.startswith('From '):
        continue
    pos = line.split()
    posr = pos[1]
    if not posr in sender:
        sender[posr] = 1
    else:
        sender[posr] = sender[posr] + 1
    for k,v in sender.items():
        if v > totalNumberOfTimes:
            totalNumberOfTimes = v
            mostFrequentWord = k
print( mostFrequentWord, totalNumberOfTimes)
