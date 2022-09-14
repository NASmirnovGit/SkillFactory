def chek_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False

print(chek_palindrome("Кит на море не романтик"))
