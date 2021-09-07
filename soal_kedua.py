import math

def soal_kedua():
    total_belanja = int(input('Total belanja seorang customer: Rp '))
    total_bayar = int(input('Pembeli membayar: Rp '))

    if total_bayar < total_belanja:
        print ("false, kurang bayar")
    else:
        kembalian = total_bayar - total_belanja
        uang = kembalian - (abs(kembalian)%100)

        list_kembalian = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
        sisa = uang

        print('Kembalian yang harus diberikan kasir: {},  dibulatkan menjadi {} '.format(kembalian, math.ceil(uang)))
        
        for pecahan in list_kembalian:
            if sisa < pecahan:
                continue
            banyak_pecahan = int(sisa / pecahan)
            sisa = sisa - ( pecahan * banyak_pecahan )
            print('{} lembar {}'.format(banyak_pecahan, pecahan))

if __name__ == '__main__':
    soal_kedua()