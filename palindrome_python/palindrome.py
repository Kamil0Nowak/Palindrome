def palindrome_checker(word):
    if word.lower() == word[::-1].lower():
        return f'"{word}" is a palindrome!'
    return f'"{word}"" is not a palindrome!'


print(palindrome_checker('Racecar'))
