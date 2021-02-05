import sys
s = sys.argv[1:]
s = ' '.join(s)
word = s.replace(', ', ' ').replace('!', ' ').replace('.', ' ').replace('?',' ').replace('  ', ' ').replace('   ', ' ').split()
print(len(word))