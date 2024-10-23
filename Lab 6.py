def encoder(password):
  new_password = ''
  for i in range(8):
    new_password += int(password[i,i+1] + 3)
  return new_password

# decodes the password
def decode(encoded_password):
  password = ""
  for letter in encoded_password:
    if letter.isdigit():
      letter = int(letter)
      letter -= 3
      if letter < 0:
        letter += 10
      letter = str(letter)
      password += letter

password = ''
option = 0
while option != 3:
  print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")
  option = int(input("Please enter an option: "))
  if option == 1:
    password = input("Please enter your password to encode: ")
    encoded_password = encoder(password)
    print("Your password has been encoded and stored!")
  elif option == 2:
    password = decode(encoded_password)
    print("The encoded password is", encoder(password), "and the original password is", password, ".")
  else:
    quit