def main():
    print("Welcome to the tip calculator.")
    bill = input("What was your bill?\n$")
    tip = input("What percentage tip would you like to give? 10, 12, or 15 percent? ")
    print("Your total amount is about $" + str(round(float(bill) * (int(tip) / 100)) + float(bill)))

if __name__ == "__main__":
    main()