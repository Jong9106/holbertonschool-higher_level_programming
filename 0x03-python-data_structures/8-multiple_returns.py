#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        c = sentence[0]
        return (length, c)
    return (length, None)
