import string
s = str(input('insert your text:'))
sl = {}
for item in string.punctuation:
    if item in string.punctuation:
        s = s.replace(item, ' ')
x = s.split()
for item in x:
    if not sl.get(item):
        sl[item] = x.count(item)
print(sl)
