# let's start with sentences that don't include punctuation

vowels = ['a', 'e', 'i', 'o', 'u']
consonantClusters2 = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
consonantClusters3 = ['sch', 'scr', 'shr', 'sph', 'spl', 'spr', 'squ', 'str', 'thr']

phrase = input('Enter a phrase: ')
print('your phrase is: ', phrase)

phraseSplitted = phrase.split()

for word in phraseSplitted:
  if (word[0] in vowels):
    print (word + 'way')
  elif (word[0:3] in consonantClusters3):
    print (word[3:] + word[0:3] + 'ay')
  elif (word[0:2] in consonantClusters2):
    print(word[2:] + word[0:2] + 'ay')
  else:
    print(word[1:] + word[0:1] + 'ay')
