alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        while(shifted_position > len(alphabet)):
            shifted_position %= len(alphabet)

        cipher_text+=alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")

#     listIndex = []
#     for letter in original_text:
#         listIndex.append(alphabet.index(letter))
#
#     for x in range(len(listIndex)):
#         if listIndex[x] + shift_amount > len(alphabet) - 1:
#             listIndex[x] += shift_amount - len(alphabet) - 1
#         else:
#             listIndex[x] += shift_amount
#
#     newStr = ""
#
#     for el in listIndex:
#         newStr += alphabet[el]
#
#     print(newStr)


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

if direction == "encode":
    encrypt(text, shift)