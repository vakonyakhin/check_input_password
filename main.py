import urwid


def check_length_pass(text):
  return len(text) > 12


def has_digit(text):
  return any(letter.isdigit() for letter in text)


def has_alpha(text):
  return any(letter.isalpha() for letter in text)


def has_lower(text):
  return any(letter.islower() for letter in text)


def has_upper(text):
  return any(letter.isupper() for letter in text)


def has_symbol(text):
  return not text.isalnum()



def get_pass_value(text, list):
  value = 0
  for func in list:
    if func(text):
      value += 2    
  return value


def main():
  
  ask = urwid.Edit('Введите пароль: ', mask='*')
  reply = urwid.Text("")
  menu = urwid.Pile([ask, reply])
  menu = urwid.Filler(menu, valign='top')
  valuation_pass_functions = [
      has_upper, 
      has_lower, 
      has_digit,
      has_symbol,
      check_length_pass,
      has_alpha
  ]

  def on_ask_change(edit, new_edit_text):
    reply.set_text("Рейтинг этого пароля: %s" % get_pass_value(new_edit_text, valuation_pass_functions))


  urwid.connect_signal(ask, 'change', on_ask_change)
  urwid.MainLoop(menu).run()
if __name__ == "__main__":
  main()

