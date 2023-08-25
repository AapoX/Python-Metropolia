from random import randint


def arpa(puolia):
    return randint(1, puolia) 


def main():
    puolia = int(input("Anna kuinka monta puolikasta arvassa on: "))
    while True:
        roll = arpa(puolia)
        print(f"{roll}")
        if roll == puolia:
            break
        

if __name__ == "__main__":
    main()