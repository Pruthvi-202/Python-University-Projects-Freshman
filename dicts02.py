def charFrequency( characters ):
  dictionary = {}
  for letter in characters:
      if letter not in dictionary:
          dictionary[letter] = 1
      else:
          dictionary[letter] += 1
  return dictionary


print( charFrequency('aaaabbbbbccdddeehhhh') )
print( charFrequency('PythonRocks') )
