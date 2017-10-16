# Stephen Randall
# 10/16/17
# Folder: Unit6Project File: unit6proj.py
# This program is a simple line, word, and character counter. It takes in a .txt file and counts how many lines the text
# doc is, how many words there are and how many characters. After it's done it prints it back to you.


def word_count(filecontents):
    """
    This function  counts the number of words in a file. Creates variable = 0 , for loop splits list into string counts
    how many in a list.
    :param filecontents: Reads in the file contents so that the program can start calculating the counts.
    :return: Returns the word count to the main function.
    """
    sum_word = 0
    for line in filecontents:
        words = line.split()
        sum_word = sum_word + len(words)
    return sum_word


def char_count(filecontents):
    """
    This function  counts the number of characters in a file. Creates variable = 0 , for loop adds the length of
    characters to variable sum_char.
    :param filecontents: Reads in the file contents so that the program can start calculating the counts.
    :return: Returns the character count to the main function.
    """
    sum_char = 0
    for character in filecontents:
        sum_char = sum_char + len(character)
    return sum_char


def main():
    myfile = open("sample.txt", "r")
    listoffilecontents = myfile.readlines()
    print("Lines:", len(listoffilecontents))
    len(listoffilecontents[0])
    num_word = word_count(listoffilecontents)
    print("Words:", num_word)
    num_char = char_count(listoffilecontents)
    print("Characters:", num_char)
    myfile.close()

main()
