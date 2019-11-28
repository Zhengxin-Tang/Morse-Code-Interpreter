#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 15:03
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : character_28453093.py
# @Software: PyCharm
# @LastModi: 2018/5/3 14:59
# @Instructions: This python file defines the class 'CharacterAnalyser', which contains the method
#                of analysing characters from decoded sequences.

class CharacterAnalyser:

    # The constructor, initializes a list that contains all valid characters and a dictionary to
    # record the occurrences of each character.
    def __init__(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.items = []
        count = []
        for character in alphabet:
            self.items.append(character)
            count.append(0)
        self.characterDictionary = dict(list(zip(self.items, count)))

    # Redefined function __str__() returns a formatted string of character dictionary.
    def __str__(self):
        temp = ""
        for item in self.characterDictionary:
            temp += (item + ": " + str(self.characterDictionary[item]) + "\n")
        return temp

    # Function analyse_characters() analyses decodes sequence and records the occurrences of each
    # character to the dictionary.
    def analyse_characters(self, decoded_sequence):
        for character in decoded_sequence:
            if character in self.items:
                self.characterDictionary[character] += 1
