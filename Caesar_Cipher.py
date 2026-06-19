#Welcome

# Encrypting Code
def encrypt():
    result = ""
    print("Encrypting message")
    shift = int(input("Choose a shift number(1 to 26): "))
    while shift < 1 or shift > 26:
        shift = int(input("Choose a shift number(1 to 26): "))
    message = input("Enter your message: ")
    for char in message.upper():
        if char.isalpha():
            code = ord(char)
            new_code = code + shift

            if new_code > 90:
                new_code = new_code - 26
            encrypted_message = chr(new_code)
            result += encrypted_message
        else:
            result += char

    print()
    print("=====RESULT=====")
    print("Encrypted Message:")
    print(result)

#Decrypting Code
def decrypt():
    result = ""
    print("Decrypting message")
    shift = int(input("Choose a shift number(1 to 26): "))
    while shift < 1 or shift > 26:
        shift = int(input("Choose a shift number(1 to 26): "))
    message = input("Enter your message: ")
    for char in message.upper():
        if char.isalpha():
            code = ord(char)
            new_code = code - shift

            if new_code < 65:
                new_code = new_code + 26
            decrypted_message = chr(new_code)
            result += decrypted_message
        else:
            result += char

    print()
    print("=====RESULT=====")
    print("Decrypted Message:")
    print(result)

#About
def about():
    print()
    print("Caesar Cipher Encryption Tool")
    print("This project demonstrates basic")
    print("cryptography concepts by encrypting")
    print("and decrypting messages using the")
    print("Caesar Cipher algorithm")
    print("Developed using Python.")
    print()

while True:
    print("====================================")
    print("CAESAR CIPHER ENCRYPTION TOOL")
    print("====================================")
    print()
    print("Welcome")
    print()
    print("This Tool Allows you to:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. About")
    print("4. Exit")
    print()
    opt = int(input("Choose an option: "))
    print()
    while opt not in [1, 2, 3, 4]:
        print("Please choose a valid option!!")
        opt = int(input("Choose an option: "))
        print()

    if opt == 1:
        encrypt()
    elif opt == 2:
        decrypt()
    elif opt == 3:
        about()
    elif opt == 4:
        print("Thank you for using Caesar Cipher Encryption Tool!")
        break

