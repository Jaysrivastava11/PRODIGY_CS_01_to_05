def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

# Main program
def main():
    while True:
        choice = input("Do you want to encrypt (E) or decrypt (D) a message? (E/D): ").strip().upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter E or D.")
            continue
        
        message = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value (a positive integer): "))
            if shift < 1:
                print("Shift value must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Shift value must be a positive integer.")
            continue
        
        if choice == 'E':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'D':
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        another = input("Do you want to encrypt or decrypt another message? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
