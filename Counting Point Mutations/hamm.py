'''
Problem
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
'''

with open('in.txt', 'r') as f:
    s = f.readline().strip()
    t = f.readline().strip()
    print len(filter(lambda (x, y): x!=y ,zip(s, t)))
