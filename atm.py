accountinfo = {
    "name": "Amruta Ghatage",
    "acc.No.": "5456465468855",
    "available Balance": "55000",
    "pin": "2525" 
}
print(accountinfo)

pin = int(input("Enter ATM pin: "))
if pin == accountinfo["pin"]:

    while True:
        print("/n====ATM MENU====")
        print("1. Check Balance")
        print("2. withdrow amount")
        print("3 deposit amount")
        print("4. change pin")
        print("5. amount details")
        print("6. Exit")