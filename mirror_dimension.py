#send the words to the mirror dimension
word=input("enter the word to reverse:")
for char in range(len(word)-1,-1,-1):
    print(word[char],end="")
    