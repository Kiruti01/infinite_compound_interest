print ("Welcome to Trustees Investment Bank Compoud Interest Calculator")
print ("Interest is calculated at 3.15% per annum")

while True:
    try:
        deposit2 = float(input("\nEnter initial deposit above £1000? "))
        rate = 1.417
        if deposit2<100:
            print ("Not a valid amount, please try again.")
        else:
            break

    except ValueError:
        print ("You have not entered a number. Please enter a valid number")

for year in range(1,13):
    amount = deposit2 * (1.0 + rate) ** year
    print ("%4d%21.2f" % (year, amount))