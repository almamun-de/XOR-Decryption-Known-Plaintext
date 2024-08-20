def decrypt_zip():
    # Read the encrypted file in binary mode
    with open('encrypted.zip.hex', 'rb') as file:
        zip_bytes = file.read()

    # ZIP header (first 10 bytes) in known plaintext
    zip_header = b'\x50\x4B\x03\x04\x14\x00\x00\x00\x08\x00'

    # Derive the key by XORing the first 10 bytes of the ciphertext with the known header
    key = bytes([zip_bytes[i] ^ zip_header[i] for i in range(10)])

    with open('XOR.key', 'wb') as file:
        file.write(key)

    # Decrypt the entire file using the derived key
    decrypted_bytes = bytearray()
    key_len = len(key)
    for i in range(0, len(zip_bytes), key_len):
        decrypted_bytes.extend(bytes([zip_bytes[i + j] ^ key[j] for j in range(min(key_len, len(zip_bytes) - i))]))

    with open('decrypted.zip', 'wb') as file:
        file.write(decrypted_bytes)

if __name__ == '__main__':
    decrypt_zip()
