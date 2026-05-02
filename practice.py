def power_2(num):
    return num & (num-1)==0

num=32
print(power_2(num))