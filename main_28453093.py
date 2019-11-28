#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 15:48
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : main_28453093.py
# @Software: PyCharm
# @LastModi: 2018/5/3 15:42
# @Instructions: This python file contains the main function. It creates instances for four classes(a decoder,
#                a character analyser, a word analyser, and a sentence analyser). Users can input multiple Morse
#                code sequences and select which level of analysis is intended by a menu.

from decoder_28453093 import Decoder
from character_28453093 import CharacterAnalyser
from word_28453093 import WordAnalyser
from sentence_28453093 import SentenceAnalyser

def main():
    decoder = Decoder()
    character = CharacterAnalyser()
    word = WordAnalyser()
    sentence = SentenceAnalyser()
    # Define a list user_input to record Morse code sequence.
    user_input = []
    user_input.append(input("Please input your Morse code sequence: "))
    # Loop while is used in case that users wish to input more than one sequence.
    while True:
        temp_seq = input("Sequence recorded. Do you wish to continue inputting? [Y]Yes [N]No: ").upper()
        if temp_seq == 'Y':
            user_input.append(input("Continue inputting your sequence: "))
            continue
        elif temp_seq == 'N':
            print("Recorded sentences are: ")
            for i in range(len(user_input)):
                print(str(i+1) + ": " + user_input[i])
            break
        else:
            # If recorded input is not Y/N, remind the user.
            print("I don't understand what you input. Please input Y/N.")
            continue

    # The list decoded_sequence_all is to record decoded sequences.
    decoded_sequence_all = []
    for j in range(len(user_input)):
        decoded_sequence_all.append(decoder.decode(user_input[j]))
        # If input is valid, analyse decoded sequences after decoding.
        if decoder.is_valid:
            character.analyse_characters(decoded_sequence_all[j])
            word.analyse_words(decoded_sequence_all[j])
            sentence.analyse_sentences(decoded_sequence_all[j])

    # Display all decoded sequences.
    print("All decoded sequences are as follows: ")
    for k in range(len(decoded_sequence_all)):
        print(str(k+1) + ": " + decoded_sequence_all[k])

    # A menu that let users select which level of analysis is intended.
    print("Analysis section(invalid sequences will not be analysed): ")
    while True:
        action = input("Please select the level of analysis: [1]character [2]word [3]sentence [4]display all [5]quit: ")
        if action not in "12345" or len(action) != 1:
            print("Invalid input.")
            continue
        elif action == "1":
            print("The total number of occurrences for each of the letters and numerals "
                  "appeared in all the decoded sequences: ")
            print(character.__str__())
        elif action == "2":
            print("The total number of occurrences for each word: ")
            print(word.__str__())
        elif action == "3":
            print("Each sentence type encountered in all the decoded sequences: ")
            print(sentence.__str__())
        elif action == "4":
            print("The total number of occurrences for each of the letters and numerals "
                  "appeared in all the decoded sequences: ")
            print(character.__str__())
            print("The total number of occurrences for each word: ")
            print(word.__str__())
            print("Each sentence type encountered in all the decoded sequences: ")
            print(sentence.__str__())
        elif action == "5":
            print("Quit successfully.")
            break

if __name__ == '__main__':
    main()
