#!/usr/bin/python

## pw.py - An insecure password locker program.

import sys, pyperclip


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
  print('Usage: python pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1]   # first command line arg is the account name


if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print('Password for ' + account + ' copied to clipboard.')
else:
  print('There is no account named ' + account)

  


##def displayInventory(inventory):
##  item_total = 0
##  
##  print('Inventory:')
##  for k, v in inventory.items():
##    print(v,k)
##    item_total += v
##
##  print('Total number of items:', str(item_total), '\n')
##
##
##
##items = {'rope': 1, 'torch': 6, 'gold coin': 42,
##         'dagger': 1, 'arrow': 12}
##
##displayInventory(items)
##
##
##
##
##
##
#### List to Dictionary Function for Fantasy Game Inventory
##
##def addToInventory(inventory, addedItems):
##
##  for item in addedItems:
##    inventory.setdefault(item, 0)
##    inventory[item] += 1
##
##  return(inventory)
##
##
##
##dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
##
##new_inventory = addToInventory(items, dragonLoot)
##
##displayInventory(new_inventory )





