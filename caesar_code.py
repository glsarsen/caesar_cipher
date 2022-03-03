def encrypt(text, mode, lang, shift):
    """
    Implementation of caesar encryption algorithm
    
        Parameters:
            text (str): Text to encode
            mode (str): Work mode: 'e' to encode, 'd' to decode
            lang (str): Language of the text: 'en' for english, 'ru' for russian
            shift (int): Number of positions to cyclic shift the code
        
        Returns:
            text_encoded (str): Text encoded by caesar encryption algorithm
    """
    text_encoded = ''
    
    if mode == 'e':
        pass
    elif mode == 'd':
        shift = -(shift)
    
    if lang.lower() == 'en':
        for c in text:
            if c.isalpha() and c.islower():
                text_encoded = text_encoded + chr(ord('a') + (ord(c) - ord('a') + shift) % 26)
            elif c.isalpha() and c.isupper():
                text_encoded = text_encoded + chr(ord('A') + (ord(c) - ord('A') + shift) % 26)
            else:
                text_encoded = text_encoded + c
    
    if lang.lower() == 'ru':
        for c in text:
            if c.isalpha() and c.islower():
                text_encoded = text_encoded + chr(ord('а') + (ord(c) - ord('а') + shift) % 32)
            elif c.isalpha() and c.isupper():
                text_encoded = text_encoded + chr(ord('А') + (ord(c) - ord('А') + shift) % 32)
            else:
                text_encoded = text_encoded + c
    return text_encoded

def len_text(text):
    count = 0
    for c in text:
        if c.isalpha():
            count += 1
    return count


# Example: Encoding each word in text by a shift equal to its length
text = input("Enter a string to encode: ").strip().split()
text_coded = ''

for i in text:
    text_coded += encrypt(i, 'e', 'en', len_text(i)) + ' '
text_coded.strip()

print("Encoded string:", text_coded)

# Example: Decoding each word in text by a shift equal to its length
text_coded = text_coded.split()
text_decoded = ''
for i in text_coded:
    text_decoded += encrypt(i, 'd', 'en', len_text(i)) + ' '
text_decoded.strip()

print("Decoded string:", text_decoded)
