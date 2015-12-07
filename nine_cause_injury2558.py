"""Nine cause's injury of Thai People in 2552 B.E."""
import csv
import pygal
def call_data(file):
    """Project"""
    data = csv.reader(open(str(file)+'.txt'))
    sore, death = 0, 0
    table = [row for row in data]
    data, dict_death_sore = {}, {}
    list_death_sore, list_case,  = [], []
    for i in table:
        sore += int(i[1])
        death += int(i[2])
    for each in table:
        print(each[0], 'จำนวนผู้บาดเจ็บ:'+'%.2f'%((int(each[1])/sore)*100)+'%', 'จำนวนผู้ตาย:'+'%.2f'%((int(each[2])/int(each[1]))*100)+'%')
        dict_death_sore[each[0]] = float('%.2f'%((int(each[2])/int(each[1]))*100))
        data[each[0]] = [float('%.2f'%((int(each[1])/sore)*100)), \
                      float('%.2f'%((int(each[2])/int(each[1]))))]
    list_case = list(dict_death_sore.keys())
    list_death_sore = list(dict_death_sore.values())
    list_death_sore.sort()
    print("จำนวนผู้บาดเจ็บ:"+str(sore) , "จำนวนคนตาย:"+str(death))
    print("5 อันดับที่มีอัตราการตายมากที่สุด")
    for i in range(5):
        for m in list_case:
            if dict_death_sore[m] == list_death_sore[18-i]:
                print(str(i+1)+'. '+m+':', str(list_death_sore[18-i])+'%')
    return data

def bar_chart(data, name):
    """Render file in Basic simple bar chart form \
    and return file after render as file.svg, embed URI code."""
    chart = pygal.Bar()
    chart.title = "Nine cause's injury of Thai People in 2552 B.E."
    name_cause = sorted(list(data.keys()))
   # print(name_cause)
    death, injury = [], []
    for i in name_cause:
        injury.append(data[i][0])
    chart.x_labels = map(str, range(1, len(name_cause)+1))
    chart.add("Injury", injury)
    chart.render_to_file(str(name)+".svg")
    embed_code = chart_data_uri()
    print("Embed URI code's this programs : "+embed_code)

def main():
    """Main Project."""
    bar_chart(call_data("injury_db"), "injury_db")

main()
