def is_acceptable(s):
  vowels = "aeiou"
  has_vowel = False
  v_count = 0
  c_count = 0

  for i in range(len(s)):
    if s[i] in vowels:
      has_vowel = True
      v_count+= 1
      c_count = 0
    else:
      c_count +=1
      v_count = 0
    if v_count ==3 or c_count ==3:
      return False
    if i>0 and s[i] == s[i-1]:
      if s[i] != 'e' and s[i] != 'o':
        return False
      
  return has_vowel

while True:
  s = input()
  if s == 'end':
    break
  if is_acceptable(s):
    print(f"<{s}> is acceptable.")
  else:
    print(f"<{s}> is not acceptable.")