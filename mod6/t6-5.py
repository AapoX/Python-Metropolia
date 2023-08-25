def parilliset(nums):
    x = [i for i in nums if i % 2 == 0]
    return x
    
def main() :
    l1 = [1, 2, 10, 3045, 340, 3]
    l2 = parilliset(l1) 
    
    print(f"Alkuperäinen lista: {l1}")
    print(f" Vain parilliset: {l2}")



if __name__ == "__main__":
    main()