# -*- coding: utf-8 -*-
"""Lists and Tuples

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13Oq7fI6ip3SkzdhaZDJgHhEPp8DQ3wrI
"""

#Lucas Vandenakker
#CS175
#List and Tuples

score = [2.5, 7.3, 6.5, 4.0, 5.2]

total =0;
for i in score:
  total+= i;

avg = total/len(score)
print("The average of the elements is:", avg)

#Lucas Vandenakker
#CS175
#List and file


list1 = []

with open("cities.txt", 'r') as file:


  for i in file:
    list1.append(i.strip())

  print(list1)

#Lucas Vandenakker
#CS175
#MatPlotLib

import matplotlib.pyplot as plt

left_edges = [0, 10, 20, 30, 40]
names = ["2016", "2017", "2018", "2019", "2020"]

heights = [100, 200, 300, 400, 500]

colors = ['r', 'g', 'b', 'w', 'k']

width = 10

plt.bar(left_edges, heights, width, color=colors)


plt.xlabel("Year")
plt.ylabel("Sales")

plt.title("Sales by Year")

plt.xticks([5, 15, 25, 35, 45], names)
plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

plt.show()