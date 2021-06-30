def main():
    for i in range(1, 101):
        print(answer(i))


def answer(num: int) -> str:
    if(num % 15 == 0):
        return "FizzBuzz"
    if(num % 3 == 0):
        return "Fizz"
    if(num % 5 == 0):
        return "Buzz"
    return str(num)


if __name__ == "__main__":
    main()
