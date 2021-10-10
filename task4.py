n = int(input('insert your number:'))
sl = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
      11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
      17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
sl2 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
th = 'thousand'
hun = 'hundred'
if n == 0:
    print('zero')
elif n < 0:
    print('error')
if n < 20:
    res = sl[n]
if 20 < n < 100:
    res = (sl2[n // 10], sl[n % 10])
if 100 < n < 1000:
    x = n % 100
    if x < 20:
        x = sl[x]
        res = (sl[n // 100], hun, x)
    elif x < 100:
        x = sl2[x // 10]
        y = sl[n % 10]
        res = (sl[n // 100], hun, x, y)
if 1000 < n < 10000:
    x = n % 100
    a = n // 100
    if x < 20:
        x = sl[x]
        res = (sl[n // 1000], th, sl[a % 10], hun, x)
    elif x < 100:
        x = sl2[x // 10]
        y = sl[n % 10]
        res = (sl[n // 1000], th, sl[a % 10], hun, x, y)
if 10000 < n < 100000:
    x = n % 100
    num = n % 1000
    nu_3 = n // 1000
    if nu_3 < 20:
        nu = sl[n]
    else:
        nu = sl2[nu_3 // 10]
        nu_2 = sl[n % 10]
    if x < 20:
        x = sl[x]
        res = (nu, nu_2, th, sl[num // 100], hun, x)
    elif x < 100:
        x = sl2[x // 10]
        y = sl[n % 10]
        res = (nu, nu_2, th, sl[num // 100], hun, x, y)
print(res)
