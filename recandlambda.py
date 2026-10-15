
# LAB_RECURSION_LAMBDA

# 1) Count vowels using recursion
def count_vowels(text):
    # Base case
    if text == "":
        return 0

    vowels = "aeiou"
    first_char = text[0].lower()

    if first_char in vowels:
        return 1 + count_vowels(text[1:])
    else:
        return count_vowels(text[1:])


phrase = input("Enter a word or phrase: ")
print("Number of vowels:", count_vowels(phrase))


# 2) Square each number using map() and lambda
numbers = [40, 35, 10, 15, 20]

squared_numbers = list(map(lambda number: number * number, numbers))

print("Squared numbers:", squared_numbers)
