lst =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","j","u","v","w","x","y","z"]

def encrypt(og_txt,shift): 
    cipher_text = ""
    
    for i in og_txt:   
        shifted_position = lst.index(i) + shift
        
        shifted_position %= len(lst)
        
        cipher_text += lst[shifted_position]
        
    print(f"Your encoded code is : {cipher_text}")
    
    
def decrypt(og_txt,shift):
    cipher_text = ""
    
    for i in og_txt:
        shifted_position=lst.index(i) - shift
        
        shifted_position %= len(lst)
        cipher_text += lst[shifted_position]
    print(f"Your encoded code is : {cipher_text}")
        
    
    
code =False
while not code :

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    user_ip = input("Type you message:\n").lower()
    shift = int(input("Type shift number:\n"))
    if direction == "encode" :
        encrypt(og_txt=user_ip,shift=shift)
    elif direction == "decode" :
        decrypt(og_txt=user_ip,shift=shift)
    else:
        print("Enter a valid input ")
        break
        
    contiue_code = input("Type 'yes' if you want to go again. Otherwise type 'no'.") 
    if contiue_code.lower() == "no" :
        print("Bye")
        break
    elif contiue_code.lower() == "yes" :
        pass
    else:
        print("Enter a valid input")
        break
    
    