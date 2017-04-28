print("Check Digit\n\n")
def checkDigit():
    lists = []
    for i in range(6):
        number = int(input())
        lists.append(number)
    total = sum(lists)
    print(total//16)
    print(total % 16)
checkDigit()
print("""
      Repeat?    y/n """)
respo = input()
while respo == "y":
    checkDigit()
