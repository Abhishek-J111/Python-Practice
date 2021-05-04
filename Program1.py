# Write a Python function that takes a sequence of numbers and determines whether all the 
# numbers are different from each other.
# Solution:
    
def func_number():
    n=input("Enter Numbers with space in between number:")
    number = n.split()
    if(len(number)==len(set(number))):
        print("All Different Numbers")
    else:
        print("Similar number")
        
if __name__ == '__main__':
    func_number()