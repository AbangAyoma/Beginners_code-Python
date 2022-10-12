# Beginners_code-Python
This repository is mainly for beginners learning how to code in python language

 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
 Use the file words.txt to produce the output below.
 
  7.2 Write a program that prompts for a file name, then opens that file and
 reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute 
the average of those values and produce an output as shown below. Do not use the sum() function 
or a variable named sum in your solution.

8.4 Open the file romeo.txt and read it line by line. For each line, 
 split the line into a list of words using the split() method. The program 
 should build a list of words. For each word on each line check to see if the word is 
 already in the list and if not append it to the list. When the program completes, sort 
 and print the resulting words in python sort() order as shown in the desired output.
 
 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts
  with 'From ' like the following line:
 From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
 You will parse the From line using split() and print out the second word in the line 
 (i.e. the entire address of the person who sent the message). Then print out a count at 
 the end.
 Hint: make sure not to include the lines that start with 'From:'. Also look at the last 
 line of the sample output to see how to print the count.
 
 9.4 Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word
of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After  the dictionary is produced, the program reads through the 
dictionary using a maximum loop to find the most prolific committer.
