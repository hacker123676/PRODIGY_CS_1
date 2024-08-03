def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        print("Encrypted message:", encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
