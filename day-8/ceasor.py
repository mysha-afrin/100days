alphabetes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k','l','m','n', 'o', 'p','q', 'r','s','t','u','v','w' ,'x','y','z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k','l','m','n', 'o', 'p','q', 'r','s','t','u','v','w' ,'x','y','z']
direction = input("Type encode to encrypt and type decode to decrypt: \n")
shift = int(input('Type the shift number \n'))


text = input("Type you message:")

def encrypt(actual_message, shifted_amount):
    cyfer_text = ""


    for letter in actual_message:
        shifted_position = alphabetes.index(letter) + shifted_amount
        cyfer_text += alphabetes[shifted_position]
        shifted_position %= len(alphabetes)
        cyfer_text += alphabetes[shifted_position]
    print(f"Here is the shifted message: {cyfer_text}")
encrypt(actual_message= text, shifted_amount= shift)
def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        shifted_position = alphabetes.index(letter) - shift_amount
        shifted_position %= len(alphabetes)
        output_text += alphabetes[shifted_position]
    print(f"Here is the shifted message: {output_text}")
decrypt(original_text = text, shift_amount = shift)
    

def ceaser (original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabetes.index(letter) - shift_amount
        shifted_position %= len(alphabetes)
        output_text += alphabetes[shifted_position]
    print(f"Here is the shifted message: {output_text}")
ceaser(original_text = text, shift_amount = shift, encode_or_decode = direction)

'''ask_user = input("Do you want to continue? y for yes and n for NO")
if ask_user == "y":
    print("Let's continue.")'''
    