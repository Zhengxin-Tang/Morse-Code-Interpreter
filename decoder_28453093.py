#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 14:25
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : decoder_28453093.py
# @Software: PyCharm
# @LastModi: 2018/5/3 15:39
# @Instructions: This python file defines the class 'Decoder', which contains the method of decoding
#                a given Morse sequence.

class Decoder:

    # The constructor, initializes a Morse code dictionary and a boolean variable isValid.
    def __init__(self):
        self.morseDictionary = {
            '01': 'A',
            '1000': 'B',
            '1010': 'C',
            '100': 'D',
            '0': 'E',
            '0010': 'F',
            '110': 'G',
            '0000': 'H',
            '00': 'I',
            '0111': 'J',
            '101': 'K',
            '0100': 'L',
            '11': 'M',
            '10': 'N',
            '111': 'O',
            '0110': 'P',
            '1101': 'Q',
            '010': 'R',
            '000': 'S',
            '1': 'T',
            '001': 'U',
            '0001': 'V',
            '011': 'W',
            '1001': 'X',
            '1011': 'Y',
            '1100': 'Z',
            '11111': '0',
            '01111': '1',
            '00111': '2',
            '00011': '3',
            '00001': '4',
            '00000': '5',
            '10000': '6',
            '11000': '7',
            '11100': '8',
            '11110': '9',
            '010101': '.',
            '110011': ',',
            '001100': '?'
        }
        self.is_valid = True

    # Redefined function __str__() returns a formatted string of Morse code dictionary.
    def __str__(self):
        temp = ""
        for item in self.morseDictionary:
            temp += (item + ": " + self.morseDictionary[item]+ "\n")
        return temp

    # Function decode() analyses user's input and try to decode it. It returns a decoded sequence
    # if decodes successfully, otherwise it will return error and set the variable isValid to False.
    def decode(self, morse_code_sequence):
        # This split() will split sequence by "***", which represents space in Morse code.
        list1 = morse_code_sequence.split("***")
        decoded_sequence = ""
        self.is_valid = True
        for i in range(len(list1)):
            # This split() will split sequence into a list of single Morse code.
            list2 = list1[i].split("*")
            for seq in list2:
                if seq in self.morseDictionary:
                    decoded_sequence += self.morseDictionary[seq]
                else:
                    self.is_valid = False
                    return "Error. Invalid input."
            # This 'if' construction is used to transfer "***" into space.
            if i < len(list1) - 1:
                decoded_sequence += " "
        # The sequence must end with a punctuation.
        if decoded_sequence[len(decoded_sequence)-1] not in '.,?':
            self.is_valid = False
            return "Error. Sequence must end with a punctuation."
        return decoded_sequence
