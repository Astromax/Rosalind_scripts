#!/usr/bin/env python
# coding: utf-8

# A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
# 
# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".
# 
# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# 
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# Alright, this is more interesting.  First of all, I need to be able to correctly parse this FASTA format, I solved that issue on an earlier problem but it wasn't a pretty solution, although when push comes to shove it's fine.  
# This problem is an idea I had for my genetic algorithm experiments, though I never actually implemented it.
# This problem has a lot of combinatorial explosion potential, which means there's likely a clever way of solving it that will result in a raging brainer.  
# This problem is really pissing me off, I'm fucking tired of it.  I don't understand why they don't provide moderate sized examples to test on, instead of "so easy a caveman can do it" and then "fuck off".

# In[40]:


import os, re
from operator import itemgetter
from textwrap import wrap

testgenes = 'rosalind_lcsm2.txt'
notebookpath = os.path.abspath('Rosalind Finding a Shared Motif.ipynb')
testpath = os.path.join(os.path.dirname(notebookpath), '%s' % testgenes)

def shared_motif(testpath):
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
    lengths = [len(g) for g in genes]
    #print('The first ID is: %s' % IDs[0])
    #print('The first gene is: %s' % genes[0])
    triples = zip(IDs, genes, lengths)
    orderedtriples = sorted(list(triples), key=itemgetter(2))
    #for p in orderedtriples:
    #    print('The length of gene %s is %i' % (p[0], len(p[1])))
    
    testsource = orderedtriples[0][1]
    wrapsize = 276
    testroots = []
    for i in range(wrapsize):
        troots = wrap(testsource[i:], wrapsize)
        if i > 0:
            troots = troots[:-1]
        testroots += troots
    
    
    candidates = []
    
    for t in testroots:
        matchcount = 0
        #print('Testing: %s' % t)
        for j,g in enumerate(orderedtriples):
            #print('Testing: %s' % g[1])
            if t in g[1]:
                #print('Found a match in triple %i' % j)
                matchcount += 1
            else:
                break
        if matchcount < len(orderedtriples):
            matchcount = 0
            continue
        else:
            candidates.append(t)
            
    print('The number of candidates is: %i' % len(candidates))
    print('Candidate 0: %s' % candidates[0])
                
    return

def common_substring(st1, st2):
    print('This finds the substrings common to both inputs')

shared_motif(testpath)


# This problem is also reminiscent of the problems in DSA Course 2, and can in principle be solved with precomputed hashes, although searching for a shared motif in 100 sample texts is somewhat larger than the problem actually provided in DSA Course 2.  "Longest Common Subsequence 3" would be the closest analogue.

# In[ ]:




