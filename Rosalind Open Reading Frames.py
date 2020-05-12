#!/usr/bin/env python
# coding: utf-8

# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
# 
# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
# 
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# 
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# Okay, this looks pretty simple, the most complicated part is probably just reading in the codon table correctly.  The basic strategy: read in the DNA, create the reverse complement, then create two extras for each, one missing the first nucleotide and the other missing the first two nucleotides.
# I think the reason it's been failing is the possibility of multiple starts, each of which can become it's own amino acid chain.
# This was a fucking ordeal!

# In[47]:


import os, ast, re
from textwrap import wrap

testDNAstring = 'rosalind_orf_new2.txt'
notebookpath = os.path.abspath('Rosalind Open Reading Frames.ipynb')
codonpath = os.path.join(os.path.dirname(notebookpath), 'RNA_codon_table.txt')
baseDNApath = os.path.join(os.path.dirname(notebookpath), '%s' % testDNAstring)

DNA = ''

with open(codonpath) as file:
    for line in file:
        codons = ast.literal_eval(line)
        
with open(baseDNApath) as file2:
    for line in file2:
        if line.startswith('>Ros'):
            continue
        else:
            DNA += line.rstrip()

#print('These are the codons')
#print(codons)
#print('This is the DNA')
#print(DNA)
            
def reverse_complement(DNA):
    pairings = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
    
    reverse_DNA = DNA[::-1]
    reversed_complement = []
    for n in reverse_DNA:
        r = pairings[n]
        reversed_complement.append(r)
    return ''.join(reversed_complement)

def transcriber(DNA):
    RNA = []
    for n in DNA:
        if n == 'T':
            r = 'U'
        else:
            r = n
        RNA.append(r)
    return ''.join(RNA)

def possible_proteins(DNA):
    DNA_strands = []
    Forward1 = DNA
    Forward2 = DNA[1:]
    Forward3 = DNA[2:]
    
    Reverse1 = reverse_complement(Forward1)
    Reverse2 = Reverse1[1:]
    Reverse3 = Reverse1[2:]
    #Reverse2 = reverse_complement(Forward2)
    #Reverse3 = reverse_complement(Forward3)
    
    DNA_strands.append(Forward1)
    DNA_strands.append(Forward2)
    DNA_strands.append(Forward3)
    DNA_strands.append(Reverse1)
    DNA_strands.append(Reverse2)
    DNA_strands.append(Reverse3)
    
    RNA_strands = []
    for D in DNA_strands:
        RNA = transcriber(D)
        RNA_strands.append(RNA)
                
    amino_acid_strings = []
    for R in RNA_strands:
        #print('Starting new strand...')
        codonlist = wrap(R, 3)
        startindices = []
        stopindices = []
        start = False
        stop = False
        for i,c in enumerate(codonlist):
            #print('Codon: %s' % c)
            if c == 'AUG':
                startindices.append(i)
                start = True            
            if start:
                if c == 'UAA' or c == 'UAG' or c == 'UGA':
                    stopindices.append(i)
                    start = False
        for s in startindices:
            if len(stopindices) == 0:
                continue
            for t in stopindices:
                if t > s:
                    nextstop = t
                    break
            if s > max(stopindices):
                continue
                    
            finalcodonlist = codonlist[s:nextstop]
            amino_acid_string = ''
            for f in finalcodonlist:
                amino_acid_string += codons[f]        
            amino_acid_strings.append(amino_acid_string)
    protein_set = set(amino_acid_strings)
    for p in protein_set:
        print(p)
        
        
    return
                
print('Commencing test fire...')
possible_proteins(DNA)


# MLLGSFRLIPKETLIQVAGSSPCNLS
# MGMTPRLGLESLLE
# MTPRLGLESLLE
