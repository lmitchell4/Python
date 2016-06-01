#!/usr/bin/python

## tableprinter.py - Display a list of lists of strings as a
## well-organized table.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
  n = len(data)
  m = len(data[0])

  max_len = [5] * n
  for i in range(n):    
    for j in range(m):
      max_len[i] = max(len(data[i][j]),max_len[i])

  for j in range(m):
    line = ''
    
    for i in range(n):
      line += data[i][j].rjust(max_len[i] + 3)

    print(line)



printTable(tableData)
