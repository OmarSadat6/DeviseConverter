
#CurrencyConverter

import requests
key = "56636f3563a0011e68bc8e4a123a4648"
# link
url = str.__add__("http://data.fixer.io/api/latest?access_key=", key)

# get the data
data = requests.get(url).json()
rates = data["rates"]

def returnCurrency(country):
    if country in rates:
        return rates[country]
    else:
        return 0


def convert(convert_from, convert_to, amount):
    if returnCurrency(convert_from) == 0 or returnCurrency(convert_to) == 0 :
        print("One of the currencies that has been entered doesn't exist")
        return False

    if convert_from == 'EUR':
        new_amount = returnCurrency(convert_to) * amount
    else:
        new_rate = returnCurrency(convert_to)/returnCurrency(convert_from)
        new_amount = new_rate * amount
    print("For", amount, convert_from, "you have", round(new_amount, 2), convert_to)

    return True


if __name__ == "__main__":
    success = False
    while not success:
        try:
            base = (input("Enter the currency you want to convert from: "))
            new_currency = (input("Enter the currency you want to convert to: "))
            user_amount = float(input("Enter the amount you want to convert: "))
            success = convert(base, new_currency, user_amount)
        except ValueError:
            print("Currencies can't contain numbers and the amount can't contain alphabetical characters !")










