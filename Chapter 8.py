fruit = 'banana'
print(fruit[:])

word = 'banana'
print(word.count('na'))

print(word[::-1])


def palindrome(input_string):
    if input_string == input_string[::-1]:
        print("This string is a palindrome!")
    else:
        print("It is not a palindrome!")


text = input("Please, write a string: ")
palindrome(text)


def rotate_word(data, step):
    new_text = ''
    for letter in text:
        rotate = chr(ord(letter) + step)
        new_text = new_text + rotate
    print(new_text)


rotate_word(text, 5)
