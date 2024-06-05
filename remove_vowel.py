def remove_vowels(text):
  vowels = 'aeiouAEIOU'
  result = ''
  for char in text:
    if char not in vowels:
      result += char
    return result
text = "Welcome back!!"
result = remove_vowels(text)
print("String after removing the vowel is : " , result)
