# pip install matplotlib
import matplotlib.pyplot as plt

x = [30, 30, 20, 20]

labels = ["Python", "Java", "C", "C++"]

plt.pie(x, labels=labels)
plt.show()