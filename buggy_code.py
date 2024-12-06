"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
# SyntaxError: invalid syntax / missing space between def and name of function
def extract_and_rearrange(string):
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
# AttributeError: 'str' object has no attribute 'splt'. Did you mean: 'split'?
    str_2 = "".join(string[6:13].split('ro'))
# NameError: name 'join' is not defined
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17]))
    str_4 = "".join(string[21:29].split(string[23:28]))
# SyntaxError: invalid syntax / missing + sign
    return str_1 + " " + str_2 + " " + str_3 + " " + str_4
# SyntaxError: expected ':' / missing  ":" and 
def ultra_extract_and_rearrange(string):
    first_transform = extract_and_rearrange(string)
    return first_transform
# SyntaxError: unterminated string literal (detected at line 19) / extra (")
print(ultra_extract_and_rearrange("egthb quirock nwoGrb forijmpxv"))

