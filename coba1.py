
import os
os.system("cls")

Dataset = ['daiva', 'zaki', ['wahyu', 'zaki'], 'shafa', ['zaki', 'aji', 'wahyu'], 'zaki']
data1 = []
data2 = {}

# QUICKSORT

def partition(l, tepi_bwh, tepi_atas):
    pivot = l[tepi_bwh]
    pos_batas = tepi_bwh+1
    for k in range(tepi_bwh+1, tepi_atas):
        if l[k] < pivot:
            l[pos_batas], l[k] = l[k], l[pos_batas]
            pos_batas += 1
    l[pos_batas-1], l[tepi_bwh] = l[tepi_bwh], l[pos_batas-1]
    return pos_batas

def quicksort(l, tepi_bwh, tepi_atas):
    if tepi_atas <= tepi_bwh:
        return
    p = partition(l, tepi_bwh, tepi_atas)
    quicksort(l, tepi_bwh, p-1)
    quicksort(l, p, tepi_atas)
    return l

def sorting():
    print("Sebelum diurutkan:", Dataset)
    for i in range(len(Dataset)):
        if type (Dataset[i]) != str:
            data2[i] = Dataset[i]
        else:
            data1.append(Dataset[i])
            quicksort(data1, 0, len(data1))
    for j in data2:
        quicksort(data2[j], 0, len(data2[j]))
        data1.insert(j, data2[j])
    print("Setelah diurutkan:", data1)

def fibonacci(e, x, o):
    searching1 = 0
    searching2 = 1
    fibonacci = searching1 + searching2
    while (fibonacci < o):
        searching1 = searching2
        searching2 = fibonacci
        fibonacci = searching1 + searching2
    offset = -1
    while (fibonacci > 1):
        i = min(offset + searching1, o-1)
        if (e[i] < x):
            fibonacci = searching2
            searching2 = searching1
            searching1 = fibonacci - searching2
            offset = i
        elif (e[i] > x):
            fibonacci = searching1
            searching2 = searching2 - searching1
            searching1 = fibonacci - searching2
        else:
            return i
    if (searching2 and e[o-1] == x):
        return o-1
    return -1
    
def search():
    print("kata", x, "ditemukan pada =")
    for z in range(len(data1)):
        if type(data1[z]) == list:
            kolomdata = fibonacci(Dataset[z], x, len(Dataset[z]))
            print(x, "berada di array index ke -",z,"kolom",kolomdata)
        else:
            if data1[z] == x:
                print(x, "berada di array index ke -",z)

sorting()
x = "zaki"
search()
print("")