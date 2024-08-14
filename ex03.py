import re

def palindromo(s):
  s = re.sub(r'[^a-zA-Z0-9]','',s).lower() # remove qualquer coisa que não seja alpha numerico
  return len(s) <= 1 or s[0] == s[-1] and palindromo(s[1:-1])
  
# USO
print(palindromo("arara"))
print(palindromo("python"))
print(palindromo("A man a plan a canal Panama"))
print(palindromo("ovo"))
print(palindromo("Socorram-me, subi no ônibus em Marrocos"))