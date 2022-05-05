#Enter the decimal number
decimal_number=int(input("Enter decimal number: "))
#define a list to hole the binary number
binary_namber=[]
#while loop for the conversion
while(decimal_number>0):
    temp = decimal_number%2
    binary_namber.append(temp)
    decimal_number=decimal_number//2
#reverse the list to get the corect number
binary_namber.reverse()

#print the binary number
print("Equivalent in binary is :", end = " ")
for i in binary_namber:
    print(i,end="")
    
    
    