'''
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3

Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''

n = int(open('in.txt', 'r').readline().strip())
r = [[1]]
for k in range(2, n+1):
    b = []
    for e in r:
        for i in range(len(e)+1):
            b.append( e[:i] + [k] + e[i:] )
    r = b
f = open('out.txt', 'w')
f.write( str(len(r)) + '\n')
for k in r:
    for c in k:
        f.write( str(c) + ' ' )
    f.write('\n')
f.close()
