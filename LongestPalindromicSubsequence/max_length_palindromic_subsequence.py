# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq
import numpy as np
from collections import deque


def calc_subsequence_lengths(sequence):
    n = len(sequence)

    # Create a table to store results of subproblems
    palindrome_lengths = np.zeros((n, n))

    # Strings of length 1 are palindrome of length 1
    np.fill_diagonal(palindrome_lengths, 1)

    for substr_length in range(2, n + 1):
        for i in range(n - substr_length + 1):
            j = i + substr_length - 1
            if sequence[i] == sequence[j] and substr_length == 2:
                palindrome_lengths[i][j] = 2
            elif sequence[i] == sequence[j]:
                palindrome_lengths[i][j] = palindrome_lengths[i + 1][j - 1] + 2
            else:
                palindrome_lengths[i][j] = max(palindrome_lengths[i][j - 1], palindrome_lengths[i + 1][j])
    return palindrome_lengths


def restore_palindrome(length_matrix, sequence):
    palindrome_left = deque()
    palindrome_right = deque()
    middle = ''
    n, n = np.shape(length_matrix)
    # start in the north-eastern corner of the matrix
    substr_length, end = n - 1, n-1
    # traceback
    while substr_length > 0 and end > 1:
        start = end - substr_length
        # add the arbitrary char from the middle
        if length_matrix[start][end] == 1:
            middle = sequence[start]
        # if possible, go left
        if length_matrix[start][end] == (length_matrix[start][end - 1]):
            substr_length -= 1
            end -= 1
        # the left cell == current - 2, but the lower is the same as current, go down
        elif length_matrix[start][end] == (length_matrix[start + 1][end]):
            substr_length -= 1
        # both left and lower == current - 2, go south-west
        else:
            palindrome_left.append(sequence[start])
            palindrome_right.appendleft(sequence[start])
            substr_length -= 2
            end -= 1
    result = ''.join(palindrome_left) + middle + ''.join(palindrome_right)
    return result, int(length_matrix[0][n-1])

if __name__ == '__main__':
    seq = 'geeks for geeks'
    matrix = calc_subsequence_lengths(seq)
    palindrome, length = restore_palindrome(matrix, seq)
    print('Longest palindromic subsequence is \'{0}\' of length {1}'.format(palindrome, length))
