def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypt_word = input("what do you wanna encrypt?")
shift = int(input("what number are you shifting to?"))
encrypted_text = encrypt(encrypt_word , shift)
print(encrypted_text)
decrypt_choice = input("do you wanna decrypt this text?")
if decrypt_choice == "yes":
    decrypt_text = decrypt(encrypted_text , shift)
    print(decrypt_text)


 
 