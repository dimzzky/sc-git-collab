from math_func import add

def main():
    data_1 = int(input("Masukkan Input 1 :"))
    data_2 = int(input("Masukkan Input 2 :"))
    operator = input("Masukkan Operator :")

    if operator  == "+":
        result = add(data_1, data_2)
    print("{} {} {}".format(data_1, operator, data_2, result))

if __name__ == "__main__":
    print("Hello Main !")
    main()