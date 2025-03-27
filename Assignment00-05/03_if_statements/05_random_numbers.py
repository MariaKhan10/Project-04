import random

N_Numbers : int = 10
min_value : int = 1
max_value : int = 100


def main():
    for _ in range(N_Numbers):
        value = random.randint(min_value,max_value)
        print(value)


if __name__ == '__main__':
    main()    



  