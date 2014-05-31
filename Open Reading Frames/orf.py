'''
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''

d = {
'UUU': 'F',
'UUC': 'F',
'UUA': 'L',
'UUG': 'L',
'UCU': 'S',
'UCC': 'S',
'UCA': 'S',
'UCG': 'S',
'UAU': 'Y',
'UAC': 'Y',
'UAA': 'Stop',
'UAG': 'Stop',
'UGU': 'C',
'UGC': 'C',
'UGA': 'Stop',
'UGG': 'W',
'CUU': 'L',
'CUC': 'L',
'CUA': 'L',
'CUG': 'L',
'CCU': 'P',
'CCC': 'P',
'CCA': 'P',
'CCG': 'P',
'CAU': 'H',
'CAC': 'H',
'CAA': 'Q',
'CAG': 'Q',
'CGU': 'R',
'CGC': 'R',
'CGA': 'R',
'CGG': 'R',
'AUU': 'I',
'AUC': 'I',
'AUA': 'I',
'AUG': 'M',
'ACU': 'T',
'ACC': 'T',
'ACA': 'T',
'ACG': 'T',
'AAU': 'N',
'AAC': 'N',
'AAA': 'K',
'AAG': 'K',
'AGU': 'S',
'AGC': 'S',
'AGA': 'R',
'AGG': 'R',
'GUU': 'V',
'GUC': 'V',
'GUA': 'V',
'GUG': 'V',
'GCU': 'A',
'GCC': 'A',
'GCA': 'A',
'GCG': 'A',
'GAU': 'D',
'GAC': 'D',
'GAA': 'E',
'GAG': 'E',
'GGU': 'G',
'GGC': 'G',
'GGA': 'G',
'GGG': 'G'
}

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

q = [ [x for x in read_fasta( open('in.txt') )][0][1] ]
# reverse complement
q.append( q[0][::-1].replace('A', 't').replace('G', 'c').replace('C', 'g').replace('T', 'a').upper() )
ans = set()
for s in q:
    # transcription
    s = s.replace('T', 'U')
    i = 0
    while i < len(s):    
        if s[i:i + 3] == 'AUG': # start codon
            j = i
            found = False
            r = ''
            while not found and j < len(s):
                if d[ s[j:j + 3] ] == 'Stop':
                    found = True
                if not found:
                    r += d[ s[j:j + 3] ]
                j += 3
            if found:
                ans.add(r)
        i += 1
for a in ans:
    print a
