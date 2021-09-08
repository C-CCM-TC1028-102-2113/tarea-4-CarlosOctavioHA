#Alternar caracteres 

num = int(input("Dame un numero"))
cont = 0
variable_1= "#"

while cont < num:

    cont = cont + 1

    if variable_1 == "#":
        print(cont,"-",  variable_1)
        variable_1= "%"
    else:
        variable_1 == "%"
        print (cont,"-", variable_1)
        variable_1= "#"