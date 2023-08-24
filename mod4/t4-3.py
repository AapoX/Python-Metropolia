nums = []

while True:
    num = input("Anna numero: ")
    if num == "":
        break
    x = int(num)
    nums.append(x)
print(min(nums), max(nums))