## Fantasy Game Inventory

def displayInventory(inventory):
  item_total = 0
  
  print('Inventory:')
  for k, v in inventory.items():
    print(v,k)
    item_total += v

  print('Total number of items:', str(item_total), '\n')



items = {'rope': 1, 'torch': 6, 'gold coin': 42,
         'dagger': 1, 'arrow': 12}

displayInventory(items)






## List to Dictionary Function for Fantasy Game Inventory

def addToInventory(inventory, addedItems):

  for item in addedItems:
    inventory.setdefault(item, 0)
    inventory[item] += 1

  return(inventory)



dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

new_inventory = addToInventory(items, dragonLoot)

displayInventory(new_inventory )





