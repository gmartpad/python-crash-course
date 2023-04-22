def italic(txt):
  return f"\033[3m{txt}\033[0m"

formatted_quote = 'Mark Twain once said, "I do not fear death. I had been dead for billions and billions of years before I was born, and had not suffered the slightest inconvenience from it."'

print(f"{italic(formatted_quote)}")