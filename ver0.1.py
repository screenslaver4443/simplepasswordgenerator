import random
pswdlength = int(input("How long do you want your password? "))
pswdlengthdone = 0
pswd = ""
alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")"]
while pswdlengthdone < pswdlength:
    pswd += (random.choice(alphabet))
    pswdlengthdone += 1
print(pswd)
