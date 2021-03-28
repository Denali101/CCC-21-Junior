boil_temp = int(input())

result = 5 * (boil_temp)
result = result - 400
sea_level = 0

if result < 100:
    print(result)
    print('1')
elif result > 100:
    print(result)
    print('-1')
elif result == 100:
    print(result)
    print('0')
