vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Enter your word: ')
found = []
for i in word:
  if i in vowels:
    if i not in found:
      found.append(i)
for k in found:
  print(k)