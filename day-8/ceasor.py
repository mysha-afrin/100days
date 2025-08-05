alphabetes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k','l','m','n', 'o', 'p','q', 'r','s','t','u','v','w' ,'x','y','z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k','l','m','n', 'o', 'p','q', 'r','s','t','u','v','w' ,'x','y','z']
direction = input("Type encode to encrypt and type decode to decrypt: \n")
shift = int(input('Type the shift number \n'))
if direction == "encode":
    text = ("Type your message : \n")
elif direction == "decode":
    shifted_msg = input("Type your encoded message : \n")
else:
    print("You typed invalid.")

def encrypt(actual_message, shifted_amount):
    cyfer_text = ""


    for letter in actual_message:
        shifted_position = alphabetes.index(letter) + shifted_amount
        cyfer_text += alphabetes[shifted_position]
    print(f"Here is the shifted message: {cyfer_text}")

    
encrypt(actual_message= text, shifted_message= shift)








'''ask_user = input("Do you want to continue? y for yes and n for NO")
if ask_user == "y":
    print("Let's continue.")'''
    