#!/usr/bin/python
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# print(type(Belgium))
# 1. Printing a line of hyphens using len function to get the length of string Belgium
print('-' * len(Belgium))
# 2. using the replace method to change the separator from , to :
# print(Belgium.replace(",",":"))
# or using the splitting of the string to create a list
population = Belgium.split(',')
print(population)
Belgium = ':'.join(population)
print(Belgium)
# 3. Two ways to calculate the population of Belgium
# One - using f string to create the sentence, but then using the indexes to locate the part of the string
# Using the function int to change the output from a string to an integer that can be added together
print(f"The population of Belgium is {int(Belgium[8:16])+int(Belgium[26:32])}")
# Two - within the list created with split() using the index to locate the values for adding
# using the int function to turn the string into an integer that can be added together
total = int(population[1]) + int(population[3])
# using the f string to print the outcome from the variable total in the sentence
print(f"The population of Belgium is {total}")

print(Belgium.index(''))