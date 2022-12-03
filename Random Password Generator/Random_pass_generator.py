import string
import random



if __name__ == '__main__':
    str1 = string.ascii_lowercase

    str2 = string.ascii_uppercase

    str3 = string.punctuation

    str4 = string.digits

    
    passLength = int(input("Enter password length\n"))  #Handle gibbersish
    s = []
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))


    password = "".join(random.sample(s,passLength)) # ; returns list of random with given length and concatenated
    
  
    print("Your password is: ")
    print(password)    
    
    #Alternative method: 
    # random.shuffle(s)
    #print("".join(s[0:passLength]))