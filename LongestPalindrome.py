n=int(input("input the length of the word: ").strip())
word=input("input the word: ").strip()
subword=""

"""input=The first line of the input
contains a single integer N indicating
the length of the word. The following
line contains a single word of length
N, made up of the letters a,b,…, z."""


def search(l,r): #l=leftpointer r=rightpointer
    global subword
    while l>=0 and r<n and word[l]==word[r]:
        current=word[l:r+1]
        if len(current)>len(subword) or (len(current)==len(subword) and current<subword):
            subword=current
        l -= 1
        r += 1
for i in range(n):
    search(i,i)
    search(i,i+1)
"""output=The first line of the output 
must contain a single integer indicating 
the length of the longest subword of the 
given word that is a palindrome. 
The second line must contain a subword that
 is a palindrome and which of maximum length.
  If there is more than one subword palindrome 
  of maximum length, print the one that is 
  lexicographically smallest (i.e., smallest 
  in dictionary order)."""

print("The length of the longest subword of the given word that is a palindrome:",len(subword)10)
print("Subword that is a palindrome and which of maximum length:",subword)
