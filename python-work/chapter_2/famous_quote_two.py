famous_person = "Mark Twain"
message = "I do not fear death. I had been dead for billions and billions of years before I was born, and had not suffered the slightest inconvenience from it."

def italic(txt):
  return f"\033[3m{txt}\033[0m"

formatted_quote = f'{famous_person} once said, "{message}"'

print(f"{italic(formatted_quote)}")