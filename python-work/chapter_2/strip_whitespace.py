string_with_right_whitespace = "python "
string_with_left_whitespace = " python"
string_with_both_whitespace = " python "

print(string_with_right_whitespace)
string_with_right_whitespace = string_with_right_whitespace.rstrip()
print(string_with_right_whitespace)

print(string_with_left_whitespace)
string_with_left_whitespace = string_with_left_whitespace.lstrip()
print(string_with_left_whitespace)

print(string_with_both_whitespace)
string_with_both_whitespace = string_with_both_whitespace.strip()
print(string_with_both_whitespace)