#!/usr/bin/python

## Strong Password Detection Project

import re

def strongPassword(password):
  ## Define a strong password as one that:
  ## -has at least 8 characters
  ## -contains at least one uppercase character
  ## -contains at least one lowercase character
  ## -contains at least one digit

  ## Return True if password meets requirements.
  ## Otherwise, return False.

  ## Check that there are at least 8 characters:
  check_1 = re.compile(r'[a-zA-Z0-9]{8,}')
  if(check_1.search(password) == None):
    return False


  ## Check that there is at least one uppercase character:
  check_2 = re.compile(r'[A-Z]+')
  if(check_2.search(password) == None):
    return False

  
  ## Check that there is at least one lowercase character:
  check_3 = re.compile(r'[a-z]+')
  if(check_3.search(password) == None):
    return False


  ## Check that there is at least one digit character:
  check_4 = re.compile(r'[0-9]+')
  if(check_4.search(password) == None):
    return False


  return True




## Test the function:
## ok:
print(strongPassword('Password123'))

## not ok:
print(strongPassword('Pa123'))

print(strongPassword('assword123'))

print(strongPassword('Password'))






