"""project"""
def test():
    """Project"""
    import csv
    data = csv.reader(open('xxx.txt'))
    sore = 0 #คนเจ็บ
    death = 0 #ตาย
    list_check = []
    check1 = 0
    check2 = 0
    check3 = 0
    list_case = []
    list_death_sore = []
    dict_death_sore = {}
    #len(data)
    table = [row for row in data]
    for i in table:
        sore += int(i[1])
        death += int(i[2])
        #print(i[1])
    #print(sore)
    for m in table:
        print(m[0], 'จำนวนผู้บาดเจ็บ:'+'%.2f'%((int(m[1])/sore)*100)+'%', 'จำนวนผู้ตาย:'+'%.2f'%((int(m[2])/death)*100)+'%')
        dict_death_sore[m[0]] = '%.2f'%((int(m[2])/int(m[1]))*100)
        check1 += float('%.2f'%((int(m[1])/sore)*100))
        check2 += float('%.2f'%((int(m[2])/death)*100))
        check3 += float('%.2f'%((int(m[2])/int(m[1]))*100))
    list_case = list(dict_death_sore.values())
    list_death_sore = list(dict_death_sore.keys())
    #print(check1, check2)
    #อัตราการบาดเจ็บต่อการตาย
    print("จำนวนผู้บาดเจ็บ:"+str(sore) , "จำนวนคนตาย:"+str(death))
test()

