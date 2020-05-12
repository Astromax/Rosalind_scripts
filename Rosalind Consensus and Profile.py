#!/usr/bin/env python
# coding: utf-8

# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
# 
# Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
# 
# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
# 
# A T C C A G C T
# G G G C A A C T
# A T G G A T C T
# DNA Strings	A A G C A A C C
# T T G G A A C T
# A T G C C A T T
# A T G G C A C T
# A   5 1 0 0 5 5 0 0
# Profile	C   0 0 1 4 2 0 6 1
# G   1 1 6 3 0 1 0 0
# T   1 5 0 0 0 1 1 6
# Consensus	A T G C A A C T
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# This shouldn't be too difficult...
# 

# In[13]:


import os, re

testgenes = 'rosalind_cons.txt'
notebookpath = os.path.abspath('Rosalind Consensus and Profile.ipynb')
testpath = os.path.join(os.path.dirname(notebookpath), '%s' % testgenes)

def proper_output(lst):
    newlist = [str(i) for i in lst]
    return ' '.join(newlist)

def consensus_and_profile(testpath):
    IDs = []
    genes = []
    with open(testpath, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith('>'):
                IDs.append(line.rstrip())
                linecount = 0
            elif linecount == 0:
                gene = line.rstrip()
                linecount += 1
            else:
                gene += line.rstrip()
            if lines[i] == lines[-1] or lines[i+1].startswith('>'):
                genes.append(gene)
    print('The data has been moved into the lists')
    basecount = len(genes[0])
    avec = ['A:']
    cvec = ['C:']
    gvec = ['G:']
    tvec = ['T:']
    consensus = ''
    for j in range(basecount):
        acount = 0
        ccount = 0
        gcount = 0
        tcount = 0
        for g in genes:
            #print('The first nucleotide is: ')
            #print(g[0])
            #print('j is: %i' % j)
            if g[j] == 'A':
                acount += 1
            elif g[j] == 'C':
                ccount += 1
            elif g[j] == 'G':
                gcount += 1
            elif g[j] == 'T':
                tcount += 1
        avec.append(acount)
        cvec.append(ccount)
        gvec.append(gcount)
        tvec.append(tcount)
        if acount >= ccount and acount >= gcount and acount >= tcount:
            consensus += 'A'
        elif ccount > acount and ccount >= gcount and ccount >= tcount:
            consensus += 'C'
        elif gcount > acount and gcount > ccount and gcount >= tcount:
            consensus += 'G'
        elif tcount > acount and tcount > ccount and tcount > gcount:
            consensus += 'T'
    print(consensus)
    print(proper_output(avec))
    print(proper_output(cvec))
    print(proper_output(gvec))
    print(proper_output(tvec))
    
    return

consensus_and_profile(testpath)


# In[ ]:





# In[ ]:




