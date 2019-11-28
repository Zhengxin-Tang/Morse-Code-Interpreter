# Morse Code Interpreter
 9133 Assignment2

**The Morse Code System**

As we have seen in the first assignment, the current International Morse Code system encodes
a range of characters, including the ISO basic Latin alphabets (A–Z), some additional Latin
letter representing accents, the Arabic numerals (0–9), and a small set of punctuations and
procedural signals (known as prosigns).

https://en.wikipedia.org/wiki/Morse_code

Each character represented by the Morse Code system is separated by a single space, and each
word (i.e. a combination of multiple characters) is separated by three spaces.

The following is an example that includes a punctuation character (the question mark) at the
end of the Morse Code sequence. (Note that the punctuation is cosidered as a single word
with a single character.)
- Sentence : WHO AM I ?
- Morse Sequence : .__ . . . . ___ ._ __ . . . .__. .

**How Morse Code is represented**

The ‘dots’ are represented by the digit
0 and the ‘dashes’ are represented by the digit 1. As for the spaces, they are represented by
the character ‘*’.
Note that our representation of Morse Code encodes the standard 26 letters (i.e. ‘A’ to ‘Z)
and the 10 numerals (i.e. ‘0’ to ‘9’), with three additional punctuation characters (i.e. the
period ‘.’; the comma ‘,’; and the question mark ‘?’).

Character Morse Code Character Morse Code Character Morse Code
- A 01 N 10 0 11111
- B 1000 O 111 1 01111
- C 1010 P 0110 2 00111
- D 100 Q 1101 3 00011
- E 0 R 010 4 00001
- F 0010 S 000 5 00000
- G 110 T 1 6 10000
- H 0000 U 001 7 11000
- I 00 V 0001 8 11100
- J 0111 W 011 9 11110
- K 101 X 1001 . 010101
- L 0100 Y 1011 , 110011
- M 11 Z 1100 ? 001100

For the same example given earlier, our Morse code sequence should read as below:
- Sentence : WHO AM I ?
- Morse Sequence : 011*0000*111***/01*/11***/00***/001100

Also note that, we assume the Morse code sequences to be decoded in this assignment represent
proper words and sentences in English. Each Morse code sequence should represent a sentence
in English.
