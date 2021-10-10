sl = {1: 'mon', 2: 'tue', 3: 'wed', 4: 'thu', 5: 'fri', 6: 'sat', 0: 'sun'}
date = int(input('insert date:'))
res = date % 7
ans = sl[res]
print(ans)