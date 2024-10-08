#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars_to_check = [".", "?", ":"]
    new_text = ""
    
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in chars_to_check:
            new_text += "\n\n"
            # Skip spaces after the punctuation marks
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    
    # Strip leading and trailing spaces from final text and print
    print(new_text.strip())
