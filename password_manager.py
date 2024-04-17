from cryptography.fernet import Fernet
'''
def Write_Key():
   key = Fernet.generate_key()
   with open("key.key", "wb") as key_file:
      key_file.write(key)

Write_Key()'''

def load_Key():
   file = open("key.key", "rb")
   key = file.read()
   return key

master_pwd = input("What is the master password? ")
key = load_Key() + master_pwd.encode()
fer = Fernet(key)





def view():
    with open('passwords.txt', 'r') as f:
         for line in f.readlines():
             data = line.rstrip()
             user, passw = data.split("|")
             print("User:", user, "password:", passw, str(fer.decrypt(passw.encode)))
  

def add():
  name = input("Account Name: ")
  pwd = input("Password: ")

  with open('passwords.txt', 'a') as f:
    f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")
  

while True:
  mode = input("Would you like to add new password or view existing ones (view, add), press q to quit? ").lower()
  if mode == "q":
    break
  elif mode == "view":
    view()
  elif mode == "add":
    add()
  else:
    print("Invalid mode.")
    continue