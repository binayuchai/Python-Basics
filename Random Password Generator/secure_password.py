
#Suggesting the strong password

SECURE = (('s','$'),('and','&'),('a','@'),('o','0'),('i','1'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password    

if __name__ == '__main__':
    password = input("Enter your password")
    print("Suggested password is: ")
    print(securePassword(password))