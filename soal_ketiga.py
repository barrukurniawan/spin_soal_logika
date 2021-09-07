def soal_ketiga():
    data = input("masukkan simbol {}[]<> : ")

    list_depan = []
    list_belakang = []
    dict_depan = []
    dict_belakang = []
    less_depan = []
    greater_belakang = []

    for i in range(len(data)):
        if data[i] == '[':
            list_depan.append(i)
        if data[i] == ']':
            list_belakang.append(i)
        if data[i] == '{':
            dict_depan.append(i)
        if data[i] == '}':
            dict_belakang.append(i)
        if data[i] == '<':
            less_depan.append(i)
        if data[i] == '>':
            greater_belakang.append(i)
    
    # index dari dua posisi buka kurung tutup kurung
    # print (list_depan, 'vs', list_belakang)
    # print (dict_depan, 'vs', dict_belakang)
    # print (less_depan, 'vs', greater_belakang)

    kombinasi_input = []

    if len(list_depan) > len(list_belakang):
        kombinasi_input.append("false")
    if len(list_depan) < len(list_belakang):
        kombinasi_input.append("false")
    if len(less_depan) < len(greater_belakang):
        kombinasi_input.append("false")

    for x,y in zip(list_depan,list_belakang):
        if x > y:
            kombinasi_input.append("false")
    for a,b in zip(dict_depan,dict_belakang):
        if a > b:
            kombinasi_input.append("false")
    for c,d in zip(less_depan,greater_belakang):
        if c > d:
            kombinasi_input.append("false")

    result = "true"
    if len(kombinasi_input) > 0:
        result = "false"
        
    print (result)

if __name__ == '__main__':
    soal_ketiga()