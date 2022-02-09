def garis() :
    print('-------------------------------------------------------------------')

def cetak(ls_matkul):
    
    print()
    print('Kartu Hasil Studi')
    garis()
    jumlah = 0
    print('{:^12} {:<15} {:>7} {:>5} {:^13} {:>10}'.format('Kode MK','Mata Kuliah','SKS(K)','Nilai','Point(P)','K X P'))
    garis()
    dict_poin = {'A' : 4, 'B' : 3, 'C' : 2, 'D' : 1}
    total_sks = 0
    total_KxP = 0
    for matkul in ls_matkul.find() :
        poin = dict_poin[matkul['nilai']]
        total_sks = total_sks + matkul['sks']
        KxP = matkul['sks'] * poin
        total_KxP = total_KxP + KxP

        print('{:^12} {:<15} {:^7} {:^5} {:^13} {:>10}'.format(matkul['kode'],matkul['nama'],matkul['sks'],matkul['nilai'],poin, KxP))
    
    garis()
    print('{:^12} {:<15} {:^7} {:^5} {:^13} {:>10}'.format('','',total_sks, '', '', total_KxP))
    IP = total_KxP / total_sks
    garis()
    print('{:<21} = {:.2f}'.format('Indeks Prestasi(IP)', IP))
    garis()