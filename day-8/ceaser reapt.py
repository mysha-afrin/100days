from art import logo

print(logo)

alphabetes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n', 'o', 'p','q', 'r','s','t','u','v','w' ,'x','y','z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n', 'o', 'p','q', 'r','s','t','u','v','w' ,'x','y','z']
direction = input("Type encode to encrypt and type decode to decrypt: \n")
shift = int(input('Type the shift number \n'))


text = input("Type you message:").lower()

'''def encrypt(actual_message, shifted_amount):
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
    
decrypt(original_text = text, shift_amount = shift)'''
    

def ceaser (original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if letter not in alphabetes:
            output_text += letter
            continue
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1
        shifted_position = alphabetes.index(letter) - shift_amount
        shifted_position %= len(alphabetes)
        output_text += alphabetes[shifted_position]
    print(f"Here is the shifted message: {output_text}")
ceaser(original_text = text, shift_amount = shift, encode_or_decode = direction)

should_continue = True
while should_continue:
    direction = input("Type encode to encrypt and type decode to decrypt: \n")
    text = input("Type you message:")
    shift = int(input('Type the shift number \n'))
    ceaser(original_text = text, shift_amount = shift, encode_or_decode = direction)
    restart = input("Do you want to restart the program? Type 'yes' or 'no': \n")
    if restart.lower() == "no":
        should_continue = False
        print("Goodbye!")
        break
