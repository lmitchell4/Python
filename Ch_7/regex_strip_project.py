#!/usr/bin/python

## Regex Version of strip() - Project

import re

def regexStrip(text, remove_char='\s'):
    re_1 = re.compile(r'^(' + remove_char + '*)(.*?)(' + remove_char + '*)$')
    new_text = re_1.findall(text)[0][1]
    return new_text



## Test the function:
print(regexStrip('test_phrase    '))
print(regexStrip('4test_phrase', '4'))
print(regexStrip('4test_phrase4', '4'))
print(regexStrip('4test4ing4', '4'))
print(regexStrip('''
                 test_phrase

'''))
print(regexStrip('XXtestingX', 'X'))





