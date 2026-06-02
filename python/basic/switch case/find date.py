date=int(input("enter date:"))
month=int(input("enter month:"))
year=int(input("enter year:"))

match(month):
    case 1:
       print(f"{date}'january'{year}")
    case 2:
       print(f"{date}'feb'{year}")
    case 3:
       print(f"{date}'march'{year}")
    case 4:
       print(f"{date}'april'{year}")
    case 5:
       print(f'{date}may{year}')
    case 6:
       print(f"{date}'jun'{year}")
    case 7:
       print(f"{date}'july'{year}")
    case 8:
       print(f"{date}'august'{year}")
    case 9:
       print(f"{date}'september'{year}")
    case 10:
       print("{date}'octomber'{year}")
    case 11:
       print(f"{date}'november'{year}")
    case 12:
       print(f"{date}'december'{year}")

