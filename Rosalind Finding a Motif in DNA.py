#!/usr/bin/env python
# coding: utf-8

# Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).
# 
# The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].
# 
# A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
# 
# The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).
# 
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# 
# Return: All locations of t as a substring of s.

# Alright, this doesn't look too difficult, but there are at least 7 new problems which become available upon solving it so I have incentive to do it now. Doesn't Python have a built-in function for this that I used yesterday for a different problem?  Yeah, the word concatenation Daily Coding Problem was essentially this, except arguably more difficult because it used a whole list of words instead of just one.

# In[7]:


import re, os

testfile = 'rosalind_subs.txt'
notebookpath = os.path.abspath('Rosalind Finding a Motif in DNA.ipynb')
testpath = os.path.join(os.path.dirname(notebookpath), '%s' % testfile)

with open(testpath, 'r') as file:
    lines = file.readlines()
    for i,line in enumerate(lines):
        if i==0:
            gene = line.rstrip()
        else:
            motif = line.rstrip()

def Motif_Finder(s,t):
    base_indices = [m.start() for m in re.finditer('(?=%s)' % t, s)]
    final_indices = [x+1 for x in base_indices]
    return final_indices

#gene = 'GATATATGCATATACTT'
#motif = 'ATAT'
print('The start positions for the motif are: ')
print(Motif_Finder(gene, motif))


# This can be solved much more efficiently using precomputed hashes, as in the Pattern Matching Problem from DSA Course 2.  I probably won't upgrade this script, just making a note for future reference.
