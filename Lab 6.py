def encoder(password):
  digit = 0
  new_password = ''
  for i in range(len(password)):
    digit = int(password[i]) + 3
    if int(digit) > 9:
      new_password += str(digit - 10)
    else:
      new_password += str(digit)
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
  return password

password = ''
option = 0
while option != 3:
  print("")
  print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit")
  option = int(input("Please enter an option: "))
  if option == 1:
    password = input("Please enter your password to encode: ")
    encoded_password = encoder(password)
    print("Your password has been encoded and stored!")
  elif option == 2:
    password = decode(encoded_password)
    print("The encoded password is", encoded_password, "and the original password is", password, end = ".")
    print("")
  else:
    quit