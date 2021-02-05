import sys
string = sys.argv[1]
string = list(string)
i = len(string)
while i>0:
    i=i-1
    if string[i] != "(" and string[i] != ")":
        x=string.pop(i)
word=''.join(string)
ass=0
while ass<len(word):
    if word != '' and '()' in word:
        word=word.replace('()', '')
    else:
        break
if word == '':
    print(1)
else:
    print(0)




