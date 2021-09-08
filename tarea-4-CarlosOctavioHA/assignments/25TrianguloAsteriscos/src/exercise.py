#Triangulos y A

altura=int(input('dame la altura'))
asteriscos= "*"
espacio=" "

for i in range(altura):
    i=i+1
    area=i*asteriscos
    altura=altura-1
    n=altura*espacio 
    print(n,area)