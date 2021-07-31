decimal = int(input("Enter a decimal number \n"))
octal = 0
ctr = 0
temp = decimal  #copying number
 
#calculating octal
while(temp > 0):
    octal += ((temp%8)*(10**ctr))  #Stacking remainders
    temp = int(temp/8)             #updating dividend
    ctr += 1
       
print("octal of {x} is: {y}".format(x=decimal,y=octal))
