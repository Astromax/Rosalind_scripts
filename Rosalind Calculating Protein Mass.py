#!/usr/bin/env python
# coding: utf-8

# In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.
# 
# The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.
# 
# Given: A protein string P of length at most 1000 aa.
# 
# Return: The total weight of P. Consult the monoisotopic mass table.

# This looks pretty simple, just read in the string (and the amino acid table) and count the numbers.  The only real question is: what is the easiest/most elegant way to do this?

# In[10]:


import os

test = 'rosalind_prtm.txt'
notebookpath = os.path.abspath('Rosalind Calculating Protein Mass.ipynb')
amino_acid_path = os.path.join(os.path.dirname(notebookpath), 'amino_acid_weights.txt')
proteinpath = os.path.join(os.path.dirname(notebookpath), '%s' % test)

amino_acid_weights = {}
with open(amino_acid_path, 'r') as file:
    for line in file:
        (key, val) = line.split()
        amino_acid_weights[key] = float(val)
print('The amino acids have been retrieved')
#print(amino_acid_weights)

with open(proteinpath, 'r') as file2:
    for line in file2:
        protein = line.rstrip()
print('This is the protein: %s' % protein)

totalmass = 0
for a in protein:
    mass = amino_acid_weights[a]
    totalmass += mass
    #print('Amino Acid: %s, Mass: %f' % (a, mass))
print('The total mass is: %0.3f' % totalmass)


# In[ ]:




