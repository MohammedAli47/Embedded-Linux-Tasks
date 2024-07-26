char = input("Enter a character: ")

if (char >= "a" and char <= "z") or (char >= "A" and char <= "Z"):
    is_vowel = (
        (char == "a")
        + (char == "e")
        + (char == "i")
        + (char == "o")
        + (char == "u")
        + (char == "A")
        + (char == "E")
        + (char == "I")
        + (char == "O")
        + (char == "U")
    )
    if is_vowel:
        print("Character is a Vowel")
    else:
        print("Character is a Consonant")
else:
    print("Character is not valid")
