# Write a Python program to check the sum of three elements 
# (each from an array) from three arrays is equal to a target value. 
# Print all those three-element combinations.

def check_sum():
    a=list()
    b=list()
    c=list()
    n1= int(input('Enter number of element 1st array'))
    for i in range(0,n1):
        inp=input()
        a.append(inp)
    
    n2= int(input('Enter number of element 2nd array'))
    for i in range(0,n2):
        inp=input()
        b.append(inp)
    
    n3= int(input('Enter number of element 3rd array'))
    for i in range(0,n3):
        inp=input()
        c.append(inp)
        
    n=int(input("Enter the target value"))
    
    for i in range(0,n1):
        for j in range(0,n2):
            for k in range(0,n3):
                if(int(a[i])+int(b[j])+int(c[k]) == n):
                    print("Sum of number yielding 70 is",a[i],b[j],c[k])
                    print("\n")


if __name__=='__main__':
    check_sum()    