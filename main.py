if __name__ == '__main__':
    import main_menu as mn

    lanjut = 1
    while lanjut == 1:
        mn.menu()
        
        pilihan = int(input('Pilih Menu : '))
        
        if pilihan == 1:
            print('DO MENU 1')
            pass
        elif pilihan == 2:
            print('DO MENU 1')
            pass
        else :
            lanjut = 0
    print('Program Selesai')