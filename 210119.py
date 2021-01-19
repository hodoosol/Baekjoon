# 1021
chardata=input()
print(chardata)



# 1022
stringdata=input()
print(stringdata)



# 1023
a, b = input().split('.')
print(a)
print(b)



# 1024
str = input()
for i in str:
  print("'"+i+"'")

  

# 1025
number = input()

print("[%d]" %(int(number[0]) * 10000))
print("[%d]" %(int(number[1]) * 1000))
print("[%d]" %(int(number[2]) * 100))
print("[%d]" %(int(number[3]) * 10))
print("[%d]" %(int(number[4])))




# 1026
time = input().split(':')
if int(time[1])==00 :
    print(0)
else:
    print(time[1])

    
    
    
# 1027
date = input().split('.')
print(date[2], date[1], date[0], sep='-')
