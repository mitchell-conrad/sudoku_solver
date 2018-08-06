
import sys
import csv
import numpy


solution = [1,2,3,4,5,6,7,8,9]
call_count = 0

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

def accept(puzzle_element):
    return all(elmement in puzzle_element for elmement in solution)

#Check the entire puzzle
def full_accept(puzzle):
    #Decompose the puzzle into its 27 individual 1-9 elements
    decomposed_puzzle = decompose(puzzle)
    for element in decomposed_puzzle:
        #break out early if we hit an invalid case
        if not accept(element):
            return False

    #puzzle is complete
    return True

def reject(puzzle_element):
    for test in solution:
        if list(puzzle_element).count(test) > 1:
            return True
    return False

def full_reject(puzzle):
    for element in decompose(puzzle):
        if reject(element):
            return True
    return False


def next(insert_val, puzzle):
    index = numpy.where(puzzle==0)

    if len(index) == 1:
        return

    mutated = puzzle
    row = index[0][0]
    col =  index[1][0]
    mutated[ row, col ] = insert_val

    return mutated

def solver(puzzle):
    global call_count
    call_count+=1
    if call_count % 10000 == 0:
        print(call_count)
    
    if full_reject(puzzle):

        return False
    if full_accept(puzzle):
        print(puzzle)
        return True
    
    
    for i in range(1,10):
        next_p = next(i, puzzle.copy())
        solver(next_p)

puzzle = []

with open('hard_test.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = [int(i) for i in row]
        puzzle.append(temp)

puzzle = rotate(puzzle)
puzzle = rotate(puzzle)

puzzle = numpy.array(puzzle)
print(puzzle)


solver(puzzle)
