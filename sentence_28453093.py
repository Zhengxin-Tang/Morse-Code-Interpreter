#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/29 15:39
# @Author  : Zhengxin Tang 28453093
# @Mail    : ztan0030@student.monash.edu
# @File    : sentence_28453093.py
# @Software: PyCharm
# @LastModi: 2018/5/3 15:21
# @Instructions: This python file defines the class 'SentenceAnalyser', which contains the method
#                of analysing sentence type from decoded sequences, including clauses(indicated
#                by the comma), complete sentences (indicated by the period), and questions
#               (indicated by the question mark).

class SentenceAnalyser:

    # The constructor, initializes a dictionary to record the occurrences of each sentence type.
    def __init__(self):
        self.sentenceDictionary = {
            "Clauses": 0,
            "Sentences": 0,
            "Questions": 0
        }

    # Redefined function __str__() returns a formatted string of sentence type dictionary.
    def __str__(self):
        temp = ""
        for item in self.sentenceDictionary:
            temp += (item + ": " + str(self.sentenceDictionary[item]) + "\n")
        return temp

    # Function analyse_sentences() analyses decodes sequence and records the occurrences of each
    # sentence type to the dictionary.
    def analyse_sentences(self, decoded_sequence):
        for item in decoded_sequence:
            if item == ".":
                self.sentenceDictionary["Sentences"] += 1
            elif item == "?":
                self.sentenceDictionary["Questions"] += 1
            elif item == ",":
                self.sentenceDictionary["Clauses"] += 1
