from random import randint


def arpa():
    return randint(1, 6)


def main():
    while True:
        roll = arpa()
        print(f"{roll}")
        if roll == 6:
            break
        

if __name__ == "__main__":
    main()