#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 15:25
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : word_28453093.py
# @Software: PyCharm
# @LastModi: 2018/5/3 15:10
# @Instructions: This python file defines the class 'WordAnalyser', which contains the method
#                of analysing words from decoded sequences.

class WordAnalyser:

    # The constructor, initializes a dictionary to record the occurrences of each word.
    def __init__(self):
        self.wordDictionary = {}

    # Redefined function __str__() returns a formatted string of word dictionary.
    def __str__(self):
        temp = ""
        for item in self.wordDictionary:
            temp += (item + ": " + str(self.wordDictionary[item]) + "\n")
        return temp

    # Function analyse_words() analyses decodes sequence and records the occurrences of each
    # word to the dictionary.
    def analyse_words(self, decoded_sequence):
        temp_sequence = decoded_sequence.split(" ")
        for words in temp_sequence:
            if words != "." and words != "," and words != "?":
                if words not in self.wordDictionary:
                    self.wordDictionary[words] = 1
                else:
                    self.wordDictionary[words] += 1