from datetime import datetime, timedelta, date
import math

def soal_keempat():
    exp_date = '2021-12-31'

    cuti_bersama = int(input('Jumlah cuti bersama : '))
    join_date = input('Tanggal join karyawan : ')
    rencana_cuti = input('Tanggal rencana cuti : ')
    durasi_cuti = int(input('Durasi cuti (hari) : '))

    date = datetime.strptime(join_date, "%Y-%m-%d")
    coba = datetime.strftime(date, "%Y-%m-%d")
    year, month, day = datetime.strftime(date, "%Y"), datetime.strftime(date, "%m"), datetime.strftime(date, "%d")

    modified_date = date + timedelta(days=180)
    hasil = datetime.strftime(modified_date, "%Y-%m-%d")
    ryear, rmonth, rday = datetime.strftime(modified_date, "%Y"), datetime.strftime(modified_date, "%m"), datetime.strftime(modified_date, "%d")

    cuti_rencana = datetime.strptime(rencana_cuti, "%Y-%m-%d")
    end_year = datetime.strptime(exp_date, "%Y-%m-%d")
    result = end_year - modified_date

    calculate = float(int(result.days)/365) * cuti_bersama

    cuti = 'true'
    hari = ''

    if cuti_rencana < modified_date:
        hari = 'Alasan : karena belum 180 hari sejak tanggal join karyawan'
        cuti = 'false'
    if cuti_rencana >= modified_date:
        if durasi_cuti > math.floor(calculate):
            cuti = 'false'
            hari = 'Alasan : karena hanya boleh mengambil {} hari cuti'.format(math.floor(calculate))
        elif durasi_cuti <= math.floor(calculate):
            cuti = 'true'

    print (cuti)
    print (hari)

if __name__ == '__main__':
    soal_keempat()