#1

Dictionary = {
  "Number": "Թիվ",
  "Int": "Ամբողջ թիվ",
  "Float": "Սահող կետով թիվ",
  "Complex": "Կոմպլեքս թիվ",
  "Bitwise Operators": "Բիթային օպերատոր",
  "Lists": "Ցուցակներ՝ կարգավորված, փոփոխման ենթակա հավաքածուներ",
  "Boolean Values":"Բուլյան արժեքներ"
}
word = input("Enter a word to see its translation to Armenian: ")
if word in Dictionary:
    print(word, "in Armenian means: ",Dictionary[word])
else:
    print("No such word in the Dictionary")


#2

days = ["Mon", "Tue", "Wed", "Thr", "Fr", "Sat", "Sun"]
day=int(input("PLease enter the number of week day: "))
print(days[day-1])

current_month=int(input("Please enter the number of current month: "))
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
for i in range(12):
    i = current_month
print("The current month is: ",months[i-1])

maxdays = { "January":31,
"February":29,
"March":31,
"April":30,
"May":31,
"June":30,
"July":31,
"August":31,
"September":30,
"October":31,
"November":30,
"December":31 }
for i in range(12):
    i = months[i-1]
print(" And it has", maxdays[i], "days")

import math
root=float(input("Please enter a number to calculate its square root: "))
print(math.sqrt(root))

#3

import dis
def myfunc(alist):
    return len(alist)
bytecode = dis.Bytecode(myfunc)
for instr in bytecode:
    print(instr.opname)
