#!/usr/bin/python3
"""a function that prints a text with 2 new lines
    after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these
    characters . ? :
    args:
        text: the text to be checked
    raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    r = ""
    flag = False
    for c in text:
        if c in (".", "?", ":"):
            r += c + "\n\n"
            flag = True
        else:
            r += c
            flag = False
    r = r.rstrip("\n")
    print(r)
