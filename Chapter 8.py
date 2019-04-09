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
    rotate = ''
    for letter in text:
        rotate = rotate + chr(ord(letter) + step)
    print(rotate)


rotate_word(text, 5)
