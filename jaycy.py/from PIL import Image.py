from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_data = np.array(image)
    
    encrypted_data = (image_data + key) % 256
    
    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_data = np.array(image)
    
    decrypted_data = (image_data - key) % 256
    
    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt an image using pixel manipulation.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode to run the script in: encrypt or decrypt.")
    parser.add_argument("input_image", help="Path to the input image.")
    parser.add_argument("output_image", help="Path to save the output image.")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (integer).")
    
    args = parser.parse_args()
    
    if args.mode == "encrypt":
        encrypt_image(args.input_image, args.output_image, args.key)
    elif args.mode == "decrypt":
        decrypt_image(args.input_image, args.output_image, args.key)


