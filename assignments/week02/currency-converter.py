"""
Currency Converter
"""

RATE = 35.5

print("Currency Converter")
print("1. THB to USD")
print("2. USD to THB")

choice = int(input("Choose conversion (1-2): "))

if choice == 1:
    thb = float(input("Enter amount in THB: "))
    usd = thb / RATE

    print(f"\nFormula: {thb:.2f} / {RATE} = {usd:.2f}")
    print(f"Result: {thb:.2f} THB = {usd:.2f} USD")

elif choice == 2:
    usd = float(input("Enter amount in USD: "))
    thb = usd * RATE

    print(f"\nFormula: {usd:.2f} * {RATE} = {thb:.2f}")
    print(f"Result: {usd:.2f} USD = {thb:.2f} THB")

else:
    print("Invalid choice!")