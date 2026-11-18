def bankoper(initialbal, deposit, withdraw):
    totalbal = initialbal + deposit
    updatedbal = totalbal - withdraw

    return totalbal, updatedbal


if __name__ == "__main__":
    initialbal = int(input("enter initial balance:"))
    deposit = int(input("enter deposit balance:"))
    withdraw = int(input("enter withdraw balance:"))

    totalbal, updatedbal = bankoper(initialbal, deposit, withdraw)

    print("Total balance after deposit:", totalbal)
    print("Updated balance after withdrawal:", updatedbal)