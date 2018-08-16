import matplotlib.pyplot as plt
import datetime

# something 
def plotpie(sizes, labels, colors, name):

    def make_autopct(values):
        def my_autopct(pct):
            print(pct)
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{v:d}'.format(v=val)
        return my_autopct

    a,b, plot = plt.pie(sizes, labels=labels, colors=colors,
            autopct = make_autopct(sizes), pctdistance=0.9, rotatelabels=True, startangle=90, radius=10)

    for autotext in plot:
        autotext.set_color('white')

    plt.axis('equal')
    # plt.title("Million Discord P's")
    file = "Discord Logging/" + str(datetime.date.today()) + "/" + name + ".png"
    plt.savefig(file)

    return file
