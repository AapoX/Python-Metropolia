def fuel(amount):
    return amount * 3.785

def main():
    amount = 1
    while amount > 0:
        amount = float(input("How many gallons of gas did you use? "))
        print(f"That is {fuel(amount)} liters.")
    
   
   
if __name__ == "__main__":
    main()