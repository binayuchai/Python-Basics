def matrix(m,n):
    A = []
    for i in range(m):
        row = []
        for j in range(n):
            input_user = int(input(f"ENter O[{i}][{j}]"))
            row.append(input_user)
        A.append(row)    
        
    return A  



def sum(A,B):
    output = []
    for i in range(len(A)):
        result = []
        for j in range(len(A[0])):
            result.append(A[i][j] + B[i][j])
        output.append(result)    
    return output
    
    
    
    
    
    
    
m = int(input("Enter the number of rows"))
n = int(input('Enter the number of columns'))  
A = matrix(m,n)
print(A)

B = matrix(m,n)
print(B)

C = sum(A,B)

print(C)


