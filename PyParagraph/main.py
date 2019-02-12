'''
PyParagraph
main.py
Ramamurthy Sundar

This script uses the regular expression library from python
in order to parse a paragraph in a given text file.  This
program will analyze the text file by counting the number of sentences,
words, and calculates the average letter/word count and average sentence
length. 
'''
import re

# initialize key counter variables
word_count = 0
sentence_count = 0
letter_count = 0

# open the input file stream
path = "./paragraph_1.txt"
with open(path, 'r') as f:
    # reads in the entire line (which is a paragraph in this script)
    for paragraph in f:
        # split up the paragraph up into sentences
        for sentence in re.split("(?<=[.!?]) +", paragraph):
            # find the number of words in the sentence
            word_count += len(sentence.split())
            
            # letter count tries to keep out as many special charachters as possible from the count
            letter_count += len(sentence) -\
            (sentence.count(' ') + sentence.count(',') + sentence.count('(') + sentence.count(')') + sentence.count('-'))
            
            # the structure of this loop divides the paragraph up into sentences
            sentence_count += 1

    # calculate the summary data, now that the totals have been found
    avg_letter_count = letter_count / word_count
    avg_sentence_length = word_count / sentence_count

# print the results to terminal
print("Paragraph Analysis")
print("---------------------")
print("Approximate Word Count: " + str(word_count))
print("Approximate Sentence Count: " + str(sentence_count))
print("Average Letter Count: " + str(round(avg_letter_count,1)))
print("Average Sentence Length: " + str(avg_sentence_length))

# print the results to a text file
output_file = open('paragraph_analysis.txt','w')
output_file.write('Paragraph Analysis' + "\n")
output_file.write("---------------------" + "\n")
output_file.write("Approximate Word Count: " + str(word_count)+ "\n")
output_file.write("Approximate Sentence Count: " + str(sentence_count)+ "\n")
output_file.write("Average Letter Count: " + str(round(avg_letter_count,1)) + "\n")
output_file.write("Average Sentence Length: " + str(avg_sentence_length) + "\n")

# close
output_file.close()
    

