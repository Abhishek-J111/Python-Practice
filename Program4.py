import re
def word_frequency():
    count=dict()
    line= input("Enter Text")
    word=re.split('[. ]',line)
    print(word)
    for i in word:
        count[i]=count.get(i,0)+1
    print(count)

if __name__ == "__main__":
    word_frequency()