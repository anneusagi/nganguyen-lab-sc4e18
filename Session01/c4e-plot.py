import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#1. Prepare date
labels = ["IOS", "Android", "Web", "React Native"]
values = [20, 15, 40, 25]
colors= ["red","blue","yellow","green"]
explode = [0, 0, 0, 0.2]   #ti le theo ban kinh


#2. Plot
pyplot.pie(values, labels=labels, colors=colors, explode=explode, shadow=True)
pyplot.axis("equal")

#3. Show
pyplot.show()