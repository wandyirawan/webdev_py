masuk_list = []
keluar_list = []


def cli_menu():
    exit = True
    status = False
    while status != exit:
        choice = int(input("pilih menu : masuk(1)/keluar(2)/sum(3)/exit(4) => "))
        if choice == 1:
            masuk_menu()
        elif choice == 2:
            keluar_menu()
        elif choice == 3:
            sum_menu()
        elif choice == 4:
            status = True


def masuk_menu():
    pemasukan = input("berapa pemasukan yang masuk : ")
    masuk_list.append(pemasukan)
    print(f"catatan pemasukan = {masuk_list}")
    print("\n ")
    print("\n ")


def keluar_menu():
    pengeluaran = input("berapa pengeluaran yang keluar : ")
    keluar_list.append(pengeluaran)
    print(f"catatan pengeluaran = {keluar_list}")
    print("\n ")
    print("\n ")


def sum_menu():
    pengeluaran = input("berapa pengeluaran yang keluar : ")
    keluar_list.append(pengeluaran)
    print(f"catatan pemasukan = {keluar_list}")
    print("\n ")
    print("\n ")


if __name__ == "__main__":
    cli_menu()
