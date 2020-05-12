#!/usr/bin/env python
# coding: utf-8

# A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
# 
# Given: A positive integer n≤7.
# 
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

# Okay, first of all, how many permutations are there for a number n...it's just n!, because the first entry can be any of them, the second can be any except the first, the third any but the first two, and on down the chain.  Okay, calculating that term is trivial, the more obnoxious thing is printing out all of the combinations.  For n=7, the number of permutations is 5040, way too many to write out manually...and too many to erase the commas from the print out.  Hmmm...

# In[18]:


n = 3
def permutation_enumerator(n):
    nfactorial = 1
    for i in range(1, n+1):
        used_ints = [i]
        nfactorial *= i
    return nfactorial
print('n factorial is: %i' % permutation_enumerator(3))

def proper_output(lst):
    newlist = [str(i) for i in lst]
    return ' '.join(newlist)
    
lst = [1,2,3]
print(proper_output(lst))

n = 7
baselist = []
for i in range(1,n+1):
    baselist.append(i)
    
print('The permutations are: ')
#print(proper_output(baselist))
    
left = 0
right = n-1
def permute(baselist, left, right):    
    if left == right:
        print(proper_output(baselist))
    else:
        for i in range(left, right+1):
            baselist[left], baselist[i] = baselist[i], baselist[left]
            permute(baselist, left+1, right)
            baselist[left], baselist[i] = baselist[i], baselist[left]

permute(baselist, left, right)


# In[ ]:




