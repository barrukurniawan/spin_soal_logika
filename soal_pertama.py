def soal_pertama(n):
    data = []
    sama_kata = []

    for i in range(0, n):
        words = input()
        data.append(words)

    aset = set()
    dup_first = ''
    for i in data:
        if i in aset:
            dup_first = i
            break
        else:   
            aset.add(i)

    for i in range(len(data)):
        if data[i] == dup_first:
            sama_kata.append(i+1)

    if len(sama_kata) == 0:
        print ("false")
    else:
        print (sama_kata)

if __name__ == '__main__':
    n = int(input("Input jumlah string, lalu enter tiap kata : "))
    soal_pertama(n)