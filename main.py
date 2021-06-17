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
 

def check_pass_value(text, list):
  value = 0
  for func in list:
    if func(text):
      value += 2
      
  return value


def main():
  
  ask = urwid.Edit('Тайный ввод: ', mask='*')
  reply = urwid.Text("")
  menu = urwid.Pile([ask, reply])
  menu = urwid.Filler(menu, valign='top')
  def on_ask_change(edit, new_edit_text):
    reply.set_text("Вы тайно написали: %s" % check_pass_value(new_edit_text, functions))

  functions = [
              check_length_pass, 
              has_upper, 
              has_lower, 
              has_alpha, 
              has_digit,
              has_symbol
              ]
  
  urwid.connect_signal(ask, 'change', on_ask_change)
  urwid.MainLoop(menu).run()
if __name__ == "__main__":
  main()

