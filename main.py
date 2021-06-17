import urwid


def check_length_pass(text):
  if len(text) > 12:
    return True
  return False  


def has_digit(text):
  return any(letter.isdigit() for letter in text)


def has_alpha(text):
  return any(letter.isalpha() for letter in text)


def has_lower(text):
  return any(letter.islower() for letter in text)


def has_upper(text):
  return any(letter.isupper() for letter in text)


def has_symbol(text):
  if text.isalnum():
    return False
  return True
 


def check_pass_value(list):
  value = 0
  for func in list:
    if func:
      value += 2
      
  return value


def main():
  txt = input("password: ")

  functions = [
              check_length_pass(txt), 
              has_upper(txt), 
              has_lower(txt), 
              has_alpha(txt), 
              has_digit(txt),
              has_symbol(txt)
              ]
  
  
  print("value:", check_pass_value(functions))
  

if __name__ == "__main__":
  main()

