def soal_pertama(n):
    data = []
    sama_kata = []

    for i in range(0, n):
        words = input()
        data.append(words)    

    dup_first = ''
    for x in data:
        if data.count(x)>1:
            dup_first = x
            break

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