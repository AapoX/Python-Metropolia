nums = []

while True:
    x = (input("Anna numero: "))
    if x == "":
        break
    y = int(x)
    nums.append(y)
    
nums.sort(reverse=True)

print(nums)