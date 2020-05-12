#!/usr/bin/env python
# coding: utf-8

# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# 
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# 
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
# 
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# 
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# This shouldn't be too difficult.  Probably the trickiest parts will be: correctly reading in the data, and stating the answer with the appropriate precision.

# In[20]:


import os
from operator import itemgetter

testname = 'rosalind_gc.txt'
notebookpath = os.path.abspath('Rosalind Computing GC Content.ipynb')
testpath = os.path.join(os.path.dirname(notebookpath), '%s' % testname)

def GC_content(testpath):
    
    IDs = []
    genes = []
    with open(testpath, 'r') as file:
        linecount = 0
        lines = file.readlines()
        for i,line in enumerate(lines):
            if line.startswith('>Ros'):
                if linecount != 0:
                    genes.append(gene)
                IDs.append(line.rstrip())
                linecount = 0
            elif linecount == 0:
                gene = line.rstrip()
                linecount += 1
                if i == len(lines)-1:
                    genes.append(gene)
            else:
                gene += line.rstrip()
                linecount += 1
                if i == len(lines)-1:
                    genes.append(gene)
    ID_content = zip(IDs, genes)
    ID_proportions = []
    for g in ID_content:
        Gs = [s for s in g[1] if s=='G']
        Cs = [s for s in g[1] if s=='C']
        GC_count = len(Gs) + len(Cs)
        GC_proportion = GC_count/len(g[1])
        #print('ID: %s' % g[0])
        #print('Proportion: %f' % GC_proportion)
        #print('Gene: %s' % g[1])
        ID_proportion = (g[0], GC_proportion)
        ID_proportions.append(ID_proportion)
    
    ordered_proportions = sorted(ID_proportions, key=itemgetter(1), reverse=True)
    print('The string ID with the highest GC content is: ')
    print(ordered_proportions[0])
    
GC_content(testpath)


# In[ ]:




