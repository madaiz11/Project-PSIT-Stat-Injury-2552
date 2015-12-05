"""Nine cause's injury of Thai People in 2552 B.E."""
import csv
import pygal
def call_data(file):
    """Project"""
    data = csv.reader(open(str(file)+'.txt'))
    sore, death = 0, 0
    table = [row for row in data]
    data = {}
    for i in table:
        sore += int(i[1])
        death += int(i[2])
    for each in table:
        data[each[0]] = [float('%.2f'%((int(each[1])/sore)*100)), \
                      float('%.2f'%((int(each[2])/death)))]
    return data

def pie_chart(data, name):
    """Render file in donut pie form (file after render is file.svg)."""
    chart = pygal.Pie(inner_radius=.4)
    chart.title = "Nine cause's injury of Thai People in 2552 B.E."
    name_cause = list(data.keys())
    for i in name_cause:
        chart.add(i, data[i][1])
    chart.render_to_file(str(name)+".svg")

def main():
    """Main Project."""
    pie_chart(call_data("maincause"), "maincause")

main()
