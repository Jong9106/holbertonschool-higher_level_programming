#!/usr/bin/python3
"""
function that prints a text with 2 new lines after
each of thesecharacters: . ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after
    each of thesecharacters: . , ? and :, and raise errors
    for some edge cases
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for o in text:
        if o in [".", "?", ":"]:
            while i + 1 < len(text) and text[i+1] == " ":
                text = text[:i+1] + text[i+2:]
        else:
            i += 1
    new_text = text.strip()

    for t in new_text:
        print(t, end="")
        if t == '.':
            print("\n")
        if t == '?':
            print("\n")
        if t == ':':
            print("\n")
