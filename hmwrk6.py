for i in range(3):
    print("number ",i)


def mapf(a, b):
  return a + b

x = map(mapf, ('1', '2', '3'), (' one', ' two', ' three'))

print(list(x))


a = ("1", "2", "3")
b = ("one", "two", "three", "four")

x = zip(a, b)

print(tuple(x))



list= ["morning", "afternoon", "evening", "night"]

for i in enumerate(list):
    print (i)



age = [5, 12, 17, 45,15, 3, 54, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, age)

for x in adults:
  print(x)



#2
list1 = []
list2 = []
n1 = int(input("Enter the number of elements of the first list: "))
for i in range(0, n1):
    elements1 = int(input("Enter the elements of the first sorted list: "))
    list1.append(elements1)
n2 = int(input("Enter the number of elements of the second list: "))
for j in range(0, n2):
    elements2 = int(input("Enter the elements of the second sorted list: "))
    list2.append(elements2)

print ("The original list 1 is : " , (list1))
print ("The original list 2 is : " , (list2))

size1 = len(list1)
size2 = len(list2)

result = []
i, j = 0, 0

while i < size1 and j < size2:
    if list1[i] < list2[j]:
      result.append(list1[i])
      i += 1
    else:
      result.append(list2[j])
      j += 1

result = result + list1[i:] + list2[j:]

print ("The combined sorted list is : " , result)

#3
def verbose(num):
    hint={0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

    if num > 1015:
        return("Try again, this time less than 1015")
    elif num < 20:
        return(hint[num])
    elif (20 < num < 100 and num % 10 == 0):
        return(hint[num])
    elif (20 < num < 100 and num % 10 != 0):
        return (hint[num//10*10]+'-'+hint[num%10])

    if (100 <= num < 1000):
        if  num % 100 == 0:
            return (hint[num//100]+' hundred')
        elif num % 10 == 0:
            return (hint[num//100]+' hundred and '+ hint[num%100])
        else:
            return (hint[num//100]+' hundred and '+hint[num%100//10]+'-'+hint[num%10])

    if (num >= 1000):
        if (num % 1000 == 0):
            return('one thousand')
        elif (num % 100 == 0):
            return(hint[num//1000]+' thousand '+hint[num//100]+' houndred')
        else:
            return(hint[num//1000]+' thousand and '+ hint[num%100])

num = int(input("Please enter a number greater than 1015: "))
print(verbose(num))


#4
def is_sorted(bool):
    for i in range (n):
        if list[i+1] > list[i]:
            return (True)
        else:
            return (False)

list = []
n = int(input("Enter number of elements of your list: "))
for i in range(0, n):
    element = int(input("Enter the elements of your list: "))
    list.append(element)

print(is_sorted(list))



