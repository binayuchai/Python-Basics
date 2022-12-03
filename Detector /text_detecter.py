import os # use this model to interact with operating system

def isPresent(fileName):
    with open(fileName,'r') as f:
        fileContent = f.read()
    
    #Checking whether the content is present in file or not
    if "hello" in fileContent.lower():
        return True    
    return False


if __name__ == '__main__':
    #Listing the contents of this folder
    dir_content = os.listdir()

    countHello = 0
    for item in dir_content:
        if item.endswith('txt'):
            print("----Checking the text in a file----")
            check = isPresent(item)
            if(check):
               print(f"hello is present in file; {item}") 
               countHello+=1
            else:
                print(f"hello is not present in {item}")
            
    print(f"{countHello} file contains 'hello' word in it")