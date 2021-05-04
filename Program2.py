# Write a Python program to find unique triplets whose 
# three elements gives the sum of zero from an array of n integers
# Solution:

def check_triplet():
    n= (input("Enter numbers"))
    number = n.split()
    length_list=len(number)
    count=0
    for i in range(0,length_list-2):
        for j in range(i+1,length_list-1):
            for k in range(i+2,length_list):
                tripler_sum=1
                tripler_sum=int(number[i])+int(number[j])+int(number[k])
                if(tripler_sum == 0):
                    count=1
                    print("Is Triplet")
                    print("The triplet Yielding Sum zero is \n %d "%int(number[i]))
                    print(number[j],"\n",number[k])
                    break
    if(count ==0):
        print("No Triplet yielding sum zero found")                
if __name__ == "__main__":
    check_triplet()

