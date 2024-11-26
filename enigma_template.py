# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: The Lord
# created: 11.18.2024
# last update:  11.18.2024
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"
# user inputs a message and selects a key (or random), the message is then translated using the cipher
def encode_message():
    EOut = ""
    text = input("whats the text you want to encode?")
    key = int(input("whats the key that you want to use for the cypher?"))
    for x in text.lower():
        if x not in alphabet:
            EOut += x
    # for each character in text it checks if its not in alphabet, if it isn't it just re-adds the character to EOut
        else:
            if (alphabet.find(x) + key) > len(alphabet):
                g = (int(alphabet.find(x)) + 26) + key
                l = alphabet[g]
                EOut += l
    # for each character in text it checks if the math would go over the length of the alphabet, if it does it does more math and finds the correct character in the alphabet to change it to based on the key then adds it to EOut
            else:
                o = alphabet.find(x) + key
                k = alphabet[o]
                EOut += k
    print(EOut)
    # If the math does not exceed the length of the alphabet then it just finds the correct character to change it to and adds it to EOut without doing that more math
# encodes a target file, similarly to encode_message, except now targeting a filename
def encode_file():
    EOut = ""
    FI = input("what file do you want to encode?")
    with open(FI) as file:
        f = file.read()
    key = int(input("whats the key that you want to use for the cypher?"))
    # opens and reads the file that the user wants to encode, aswell as asking what number they want the key to be
    for x in f.lower():
        if x not in alphabet:
            EOut += x
    # for each character in the file it checks if its not in alphabet, if it isn't it just re-adds the character to EOut
        else:
            if (alphabet.find(x) + key) > len(alphabet):
                g = (int(alphabet.find(x)) - 26) + key
                l = alphabet[g]
                EOut += l
        # for each character in text it checks if the math would go over the length of the alphabet, if it does it does more math and finds the correct character in the alphabet to change it to based on the key then adds it to EOut
            else:
                o = alphabet.find(x) + key
                k = alphabet[o]
                EOut += k
    print(EOut)
    file.close()
    # If the math does not exceed the length of the alphabet then it just finds the correct character to change it to and adds it to EOut without doing that more math, and then closes the file

# decodes target file using a user-specified key. If key is unknown, a keypress should
# call decode_unknown_key()
def decode_file():
    EOut = ""
    FI = input("what file do you want to decode?")
    with open(FI) as file:
        f = file.read()
    key = int(input("whats the key that you want to use for the cypher?"))
    # opens and reads the file that the user wants to decode, aswell as asking what number they want the key to be
    for x in f.lower():
        if x not in alphabet:
            EOut += x
    # for each character in the file it checks if its not in alphabet, if it isn't it just re-adds the character to EOut
        else:
            if (alphabet.find(x) - key) > len(alphabet):
                g = (int(alphabet.find(x)) + 26) - key
                l = alphabet[g]
                EOut += l
            # for each character in text it checks if the math would go over the length of the alphabet, if it does it does more math and finds the correct character in the alphabet to change it to based on the key then adds it to EOut
            else:
                o = alphabet.find(x) - key
                k = alphabet[o]
                EOut += k
    print(EOut)
    file.close()
    # If the math does not exceed the length of the alphabet then it just finds the correct character to change it to and adds it to EOut without doing that more math, and then closes the file

# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key():
    FI = input("what file do you want to decode?")
    with open(FI) as file:
        f = file.read()
    # opens and reads the file that the user wants to decode
    for key in range(0, 26):
        EOut = ""
    # for each number from 0 to 26 it will do set EOut equal to an empty string, allowing the rest to add to EOut without itjust adding to the same string and making it actually reset before adding the next loop
        for x in f.lower():
            if x not in alphabet:
                EOut += x
        # for each character in the file it checks if its not in alphabet, if it isn't it just re-adds the character to EOut
            else:
                if (alphabet.find(x) - key) > len(alphabet):
                    g = (int(alphabet.find(x)) + 26) - key
                    l = alphabet[g]
                    EOut += l
                # for each character in text it checks if the math would go over the length of the alphabet, if it does it does more math and finds the correct character in the alphabet to change it to based on the key then adds it to EOut
                else:
                    o = alphabet.find(x) - key
                    k = alphabet[o]
                    EOut += k
        print(f" {key}) {EOut}")
    file.close()
    # If the math does not exceed the length of the alphabet then it just finds the correct character to change it to and adds it to EOut without doing that more math, and then closes the file

# main method declaration
def main():
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Decode file with an unknown key. \n"
              f"[5]: Exit.")
    # menu used to asking the user what they want to do.

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            decode_unknown_key()
        elif selection == "5":
            print("Goodbye.")
            exit()
        # calls the correct function depending on what the user chooses to do in the menu
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()