# Write a Python program to count the number of each character of a given text of a text file.

def count_char():
    file_name = input("Enter File name")
    file_handle = open(file_name,'r')
    data = file_handle.read()
    length = len(data)
    length_withoutspace = len(data.replace(" ",""))
    print("Length of File including white spaces are :",length)
    print("Length of file excluding white spaces are:",length_withoutspace)
    

if __name__ == "__main__":
    count_char()