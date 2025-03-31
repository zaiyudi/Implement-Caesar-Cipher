def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        # Check if character is a letter
        if char.isalpha():
            # Shift character and ensure it wraps around the alphabet
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        # Check if character is a letter
        if char.isalpha():
            # Shift character back and ensure it wraps around the alphabet
            start = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted_text += char  # Non-alphabet characters remain unchanged
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").lower()

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (an integer): "))

    if choice == 'e':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()