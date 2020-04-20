dollars = int(float(input('Enter an amout of dollar: ')) * 100)
print(dollars)
quarters, change = divmod(dollars, 25)
dimes, change = divmod(change, 10)
nickels, change = divmod(change, 5)
pennies, change = divmod(change, 1)

print(f"Quarters: {quarters}, dimes: {dimes}, nickels: {nickels}, pennies: {pennies}")
