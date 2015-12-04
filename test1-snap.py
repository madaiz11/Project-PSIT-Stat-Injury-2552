"""project"""
def test():
    """Project"""
    import csv
    data = csv.reader(open('xxx.txt'))
    sore = 0 #คนเจ็บ
    death = 0 #ตาย
    check1 = 0
    check2 = 0
    #len(data)
    table = [row for row in data]
    for i in table:
        sore += int(i[1])
        death += int(i[2])
        #print(i[1])
    print(sore)
    for m in table:
        print(m[0], '%.2f'%((int(m[1])/sore)*100)+'%', '%.2f'%((int(m[2])/death)*100)+'%')
        check1 += float('%.2f'%((int(m[1])/sore)*100))
        check2 += float('%.2f'%((int(m[2])/death)*100))
    print(check1, check2)
    #อัตราการบาดเจ็บต่อการตาย

test()
