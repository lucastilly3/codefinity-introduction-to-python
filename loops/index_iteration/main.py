prices = [29.99, 45.50, 12.75, 38.20]
discount_factors = [.10, .20, .15, .05]
for index in range(len(prices)):
    prices[index] -= prices[index] * discount_factors[index]
    print(f"Updated price for item {index}: {prices[index]:.2f}")