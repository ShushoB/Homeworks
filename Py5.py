n = int(input("Enter the side of a square: ")) 
print(n * '*')
for i in range(n-2):
    print ('*' + ' ' * (n-2) + '*')
print(n * '*' )
