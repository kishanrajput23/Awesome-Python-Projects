conversion_rates = {
    'USD': 1.0,     # US Dollar
    'EUR': 0.95,    # Euro
    'GBP': 0.82,    # British Pound
    'JPY': 148.45,   # Japanese Yen
    'CAD': 1.37,    # Canadian Dollar
    'AUD': 1.57,    # Australian Dollar
    'INR': 83.22,   # Indian Rupee
    'CNY': 7.20,    # Chinese Yuan
    'CHF': 0.92,    # Swiss Franc
    'NZD': 1.68,    # New Zealand Dollar
    'SEK': 11.03,    # Swedish Krona
    'SGD': 1.37,    # Singapore Dollar
    'HKD': 7.83,    # Hong Kong Dollar
    'KRW': 1348.59,  # South Korean Won
    'BRL': 5.16,    # Brazilian Real
    'RUB': 99.55,   # Russian Ruble
    'TRY': 13.55,   # Turkish Lira
    'ZAR': 19.29,   # South African Rand
    'MXN': 17.95,   # Mexican Peso
    'AED': 3.67     # UAE Dirham
}
def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    
    if from_currency in conversion_rates and to_currency in conversion_rates:
        converted_amount = amount / conversion_rates[from_currency] * conversion_rates[to_currency]
        return converted_amount
    else:
        return None

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the source currency (e.g., USD): ").upper()
to_currency = input("Enter the target currency (e.g., EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)

if result is not None:
    print(f"{amount} {from_currency} is equal to {result} {to_currency}")
else:
    print("Invalid currency codes. Please check your input.")
