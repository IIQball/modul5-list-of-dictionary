def do_menu1(ls_matkul):
    matkul = {}
    print()
    matkul['nama'] = input('Nama MataKuliah : ')
    matkul['kode'] = input('Kode MataKuliah : ')
    matkul['sks'] = int(input('Jumlah SKS : '))
    matkul['nilai'] = input('Nilai : ')
    ls_matkul.insert_one(matkul)
    return ls_matkul