import sys
import numpy as np

_min = sys.maxsize


def load_file():
    matrix = []
    with open('file.txt') as file:
        lines = file.readlines()
        for line in lines:
            new_line = line.split()
            row = []
            for element in new_line:
                row.append(int(element))
            matrix.append(row)
    return matrix


def load_file_2():
    matrix = np.zeros((1000, 50), dtype=np.int)

    with open('file.txt', 'r') as f:
        for index, line in enumerate(f):
            pole = np.asarray(line.strip().split(' '))
            matrix[index] = pole
    return matrix


def matrix_chain_iteratively_2():
    input = np.zeros((1000, 50), dtype=np.int)
    matrix_of_minuses = np.zeros((1000, 50), dtype=np.int)
    kroky = np.zeros((1000, 50), dtype=np.int)
    indexes = []
    with open('file.txt', 'r') as f:
        for index, line in enumerate(f):
            pole = np.asarray(line.strip().split(' '))
            input[index] = pole
            matrix_of_minuses[0] = input[0]

    for row_index in range(1, 1000):
        for column_index in range(0, 50):
            if column_index == 0:
                numbers = [matrix_of_minuses[row_index - 1][column_index],
                           matrix_of_minuses[row_index - 1][column_index + 1]]
            elif column_index == 49:
                numbers = [matrix_of_minuses[row_index - 1][column_index],
                           matrix_of_minuses[row_index - 1][column_index + -1]]
            else:
                numbers = [matrix_of_minuses[row_index - 1][column_index - 1],
                           matrix_of_minuses[row_index - 1][column_index],
                           matrix_of_minuses[row_index - 1][column_index + 1]]
            x = min(numbers)
            ind = numbers.index(x)
            kroky[row_index][column_index] = column_index - 1 + ind
            matrix_of_minuses[row_index][column_index] = input[row_index][column_index] + x
    print(matrix_of_minuses[999])
    print(min(matrix_of_minuses[999]))


def matrix_chain_iteratively():
    matrix_of_minuses = np.zeros((1000, 50), dtype=np.int)
    matrix = load_file_2()
    matrix_of_minuses[0] = matrix[0]

    for row in range(1, len(matrix)):
        for column in range(0, len(matrix[0])):
            count1 = sys.maxsize
            count2 = sys.maxsize
            count3 = sys.maxsize

            if column == 0:
                count1 = matrix[row][column] + matrix_of_minuses[row - 1][column]
                count2 = matrix[row][column] + matrix_of_minuses[row - 1][column + 1]
            elif column == 49:
                count1 = matrix[row][column] + matrix_of_minuses[row - 1][column]
                count2 = matrix[row][column] + matrix_of_minuses[row - 1][column - 1]
            else:
                count1 = matrix[row][column] + matrix_of_minuses[row - 1][column]
                count2 = matrix[row][column] + matrix_of_minuses[row - 1][column - 1]
                count3 = matrix[row][column] + matrix_of_minuses[row - 1][column + 1]
            counts = [count1, count2, count3]
            matrix_of_minuses[row][column] = min(counts)
    print(matrix_of_minuses[999])
    print(min(matrix_of_minuses[999]))


def main():
    matrix_chain_iteratively()



if __name__ == '__main__':
    main()
