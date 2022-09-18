def main():
    print("Welcome to the tip calculator.")
    total_bill = input("What was your total bill?\n$")
    tip = input("What percentage tip would you like to give? 10, 12, or 15 percent? ")
    print("Your total tip amount is about $" + str(round(float(total_bill) * (int(tip) / 100))))

if __name__ == "__main__":
    main()