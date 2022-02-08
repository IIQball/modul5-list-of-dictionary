if __name__ == '__main__':
    import main_menu as mn
    import do_menu1 as do_mn1
    import do_menu2 as do_mn2

    lanjut = 1
    ls_matkul = []
    while lanjut == 1:
        mn.menu()
        
        pilihan = int(input('Pilih Menu : '))
        
        if pilihan == 1:
            ls_matkul = do_mn1.do_menu1(ls_matkul)
        elif pilihan == 2:
            do_mn2.cetak(ls_matkul)
            pass
        else :
            lanjut = 0
    print('Program Selesai')