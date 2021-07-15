# 2941
word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia :
    word = word.replace(i, '*')
print(len(word))





# 1316 _ 1
res = int(input())
for j in range(res) :
    word = input()
    check = word[-1]
    for k in range(len(word) - 1) :
        if word[k] != word[k + 1] :
            if word[k] not in check :
                check += word[k]
            else :
                res -= 1
                break
print(res)





# 1316 _ 2
res = int(input())
for j in range(res) :
    word = input()
    for k in range(len(word) - 1) :
        if word[k] != word[k + 1] :
            if word[k] in word[k + 1:] :
                res -= 1
                break
print(res)





