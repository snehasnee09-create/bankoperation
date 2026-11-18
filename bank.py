def bankoper(initialbal, deposit, withdraw):
    totalbal = initialbal + deposit
    updatedbal = totalbal - withdraw

    return totalbal, updatedbal


if __name__ == "__main__":
    initialbal = int(sys.argv[1])
    deposit = int(sys.argv[2])
    withdraw = int(sys.argv[3])

    totalbal, updatedbal = bankoper(initialbal, deposit, withdraw)

    print("Total balance after deposit:", totalbal)
    print("Updated balance after withdrawal:", updatedbal)