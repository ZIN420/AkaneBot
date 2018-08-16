import matplotlib.pyplot as pyplot
import datetime

import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
sizes = [40, 20, 30, 20]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)

def make_autopct(values):
    def my_autopct(pct):
        print(pct)
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_autopct

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct=make_autopct(sizes), shadow=True, startangle=90)
plt.axis('scaled')
plt.title('Year 2013')
plt.savefig(str(datetime.date.today()) + '.png')
