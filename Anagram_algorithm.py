def Anagram(s:list):
    dictionary={}
    for word in s:
      r=''.join(sorted(word))
      if r in s:
        dictionary[r].append(word)
      else:
        dictionary[r]=word
    return dictionary #return all anagrams in the set of strings s   
