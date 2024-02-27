def is_palindrome(s):
    clean_s = ''.join(s.split()).lower()

    left, right = 0, len(clean_s) - 1

    while left < right:
        if clean_s[left] != clean_s[right]:
            return False
        left += 1
        right -= 1

    return True

string_to_check = "A man a plan a canal Panama"
result = is_palindrome(string_to_check)

if result:
    print(f'"{string_to_check}" is a palindrome.')
else:
    print(f'"{string_to_check}" is not a palindrome.')
