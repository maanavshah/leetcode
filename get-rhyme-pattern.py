def getRhymePattern(word):
  vowels = ['a', 'e', 'i', 'o', 'u', 'y']
  flag = False
  res = ''
  if word[0] == 'y':
    word = word[1:]

  for i, w in enumerate(word[::-1]):
    if w in vowels:
      flag = True
      if i == 0 and w == 'y':
        flag = False
    elif flag:
        break
    res += w
  return res[::-1]
