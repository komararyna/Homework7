n = str(input('insert your number:'))
sl = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
oth = n[-1]
res = sl[oth]
for item in n[-2::-1]:
      if sl[item] >= sl[oth]:
          res += sl[item]
      else:
            res -= sl[item]
      oth = item
print(res)
