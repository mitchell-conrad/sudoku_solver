
import sys
import csv
from numpy import array

solution = [1,2,3,4,5,6,7,8,9]

def rotate(puzzle):

    temp = zip(*puzzle[::-1])
    return [list(element) for element in temp]

def decompose(puzzle):
    decomposed_puzzle = []

    for element in rotate(puzzle):
        decomposed_puzzle.append(element)

    for element in puzzle:
        decomposed_puzzle.append(element)
    
    decomposed_puzzle.append(puzzle[:3,   :3].flatten())
    decomposed_puzzle.append(puzzle[3:6,  :3].flatten())
    decomposed_puzzle.append(puzzle[6:10, :3].flatten())

    decomposed_puzzle.append(puzzle[:3,  3:6].flatten())
    decomposed_puzzle.append(puzzle[3:6, 3:6].flatten())
    decomposed_puzzle.append(puzzle[6:10,3:6].flatten())

    decomposed_puzzle.append(puzzle[:3,  6:10].flatten())
    decomposed_puzzle.append(puzzle[3:6, 6:10].flatten())
    decomposed_puzzle.append(puzzle[6:10,6:10].flatten())
    
    return decomposed_puzzle

def check(puzzle):
    return all(elmement in puzzle for elmement in solution)

#Check the entire puzzle
def full_check(puzzle):
    #Decompose the puzzle into its 27 individual 1-9 elements
    decomposed_puzzle = decompose(puzzle)
    for element in decomposed_puzzle:
        #break out early if we hit an invalid case
        if not check(element):
            return False

    #puzzle is complete
    return True

puzzle = []

with open('column.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [int(i) for i in row]
        puzzle.append(temp)

puzzle = array(puzzle)



for x in range(1,70000):
    full_check(puzzle)

if full_check(puzzle):
    print("true")
else:
    print("false")

