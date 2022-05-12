import random #imports the module required to do random stuff.
pswdlength = int(input("How long do you want your password? ")) #Asks the user how long they want their password to be.
pswdlengthdone = 0 #Prepares a varible thats being used to check password length
pswd = ""
alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")"] #All the characters that the password can contain
while pswdlengthdone < pswdlength: #simple while loop that stops when the password is the same length as the requested length.
    pswd += (random.choice(alphabet)) #Adds a random character from the above list to the password.
    pswdlengthdone += 1 #Adds 1 to the known password length.
print(pswd) #prints completed password.
input("") #makes it so the program doesn't close immediatly.
