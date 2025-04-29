def sum_of_number():
    s = input().split()
    a = float(s[0])
    b = float(s[1])
    sum = a+b

    if int(sum) == sum:
        return int(sum)
    else:
        return sum    
    
print(sum_of_number())