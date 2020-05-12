#!/usr/bin/env python
# coding: utf-8

# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
# 
# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
# 
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# 
# Return: The protein string encoded by s.

# This one shouldn't be too difficult.  The main point of doing this one is to get to the more interesting problems which come later.  The point of Rosalind is to build up knowledge/skills from scratch, so it makes sense to require people to do simple problems first before hitting the big ones.

# In[24]:


import os, ast
from textwrap import wrap

notebook_path = os.path.abspath("Rosalind Translating RNA into Protein.ipynb")
codonpath = os.path.join(os.path.dirname(notebook_path), 'RNA_codon_table.txt')

with open(codonpath) as file:
    for line in file:
        #print('This is the line')
        #print(line)
        codons = ast.literal_eval(line)

#print('We have this codon dictionary')
#print(codons)
RNApath = os.path.join(os.path.dirname(notebook_path), 'rosalind_prot.txt')

with open(RNApath) as file:
    for line in file:
        RNA = '%s' % line

#start: AUG
#stop: UAA, UAG, UGA
start_index = RNA.find('AUG')
print('The start index is: %i' % start_index)
chopped_RNA = RNA[start_index:]

codon_list = wrap(chopped_RNA, 3)
#amino_acid_list = []
amino_acid_string = ''
for j,c in enumerate(codon_list):
    if c == 'UAA' or c == 'UAG' or c == 'UGA':
        final_codon_list = codon_list[:j]
        break
    amino_acid = codons[c]
    #amino_acid_list.append(amino_acid)
    amino_acid_string += amino_acid
    
#print('The original RNA strand is: ')
#print(RNA)

#print('The chopped RNA strand is: ')
#print(chopped_RNA)

#print('The protein-coding section is: ')
#print(final_codon_list)

print('The amino acid string is: ')
print(amino_acid_string)


# In[ ]:





# In[ ]:




