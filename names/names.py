import time

from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
bst = BinarySearchTree()

# Insert names into instance of bst
for name_1 in names_1:
    bst.insert(name_1)

# find and append duplicates
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

"""
Pre-optimized code:
  Time complexity: O(n^2)
  Run-time: 4.928653 seconds

Optimized code using a binary search tree:
  Time complexity: 
  
  Searching: worst case complexity of O(n).
  Insertion: worst case complexity of O(n). 
  Deletion:  worst case complexity of O(n). 

  Run-time: 0.05270957946777344 seconds
  """
  

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

"""
Optimized code using Python's built-in 'set' data structure (see code below):
  Time complexity: O(n)
  Run-time: 0.0020346641540527344 seconds"""

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops with python's "set"
# and store duplicates as lists for stretch goal perameters. 
duplicates = list(set(names_1) & set(names_2))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# just for fun, checking out how I would do it with pandas:

start_time = time.time()

import pandas as pd 

header_list = ["Name"]

#  create pandas dataframe loaded with names on first text file

names_1_df = pd.read_csv("names_1.txt", names=header_list)


#  create pandas dataframe loaded with names on second text file
names_2_df = pd.read_csv("names_2.txt", names=header_list)

#  create new dataframe that contains names from 2nd which are found in 1st
duplicates_df = names_2_df[names_2_df['Name'].isin(names_1_df['Name'])]

dup_list = duplicates_df['Name']

#  print the list of duplicates
print('Just for fun, duplicates using pandas')

print('Using pandas took this long:')

end_time = time.time()
print (f"{len(dup_list)} duplicates:\n\n{', '.join(dup_list)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# using pandas is a LOT slower than my BST or python's built in set and list functions. 