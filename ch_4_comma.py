## Comma Code

def commaFun(useList):
  if len(useList) == 0:
    return useList
  
  ret = ''
  for i in range((len(useList) - 1)):
    ret += useList[i] + ', '

  ret += 'and ' + useList[len(useList) - 1]
  return ret


spam = ['apples', 'bananas', 'tofu', 'cats']

#print(commaFun(spam))

#print(commaFun(['a', 'b', 'c', 'd']))

#print(commaFun([]))





## Character Picture Grid

def gridFun(gridList):
  nrow = len(gridList)
  ncol = len(gridList[0])

  for c in range(ncol):
    for r in range(nrow):
      print(grid[r][c], end = '')
      if r == (nrow - 1):
        print()

  return None


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

gridFun(grid)




