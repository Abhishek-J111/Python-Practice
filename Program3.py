# Write a Python program to create the combinations of 3 digit combo
# Solution:
from itertools import permutations
# Using Permutation Module
def combination_digit():
    n=list((input("Enter the Number for Combination ")))
    a=list(permutations(n,3))
    for i in a:
        print(i)

# Using Looping 
def combination_looping():
     n=list((input("Enter the Number for Combination ")))
     length= len(n)
     for i in range(length):
        for j in range(length):
            for k in range(length):
                if(i!=j & j!=k & k!=i):
                    print(n[i],n[j],n[k])
    
if __name__=="__main__":
    combination_digit()
    combination_looping()