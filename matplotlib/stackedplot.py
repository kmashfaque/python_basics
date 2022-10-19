from matplotlib import pyplot as plt
import numpy as np


# for stacked plot

# w = .4
# x_axis = ["CSE", "ISE", "ECE", "EEE", "Mech"]
# boys = [100, 40, 60, 240, 300]
# girls = [200, 70, 30, 120, 150]

# plt.bar(x_axis, boys, w, label="boys")
# plt.bar(x_axis, girls, w, bottom=boys, label="girls")
# plt.title("Students of engineering departments..")
# plt.legend()
# plt.xlabel("Departments")
# plt.ylabel("Number of students")
# plt.tight_layout()
# plt.show()


# for multiple plot
x_axis = ["USA", "GBR", "FRANCE", "RUSSIA", "CHINA"]
gold = [30, 20, 40, 55, 68]
silver = [110, 90, 88, 140, 100]
bronze = [211, 202, 303, 190, 120]
w = .3

bar_1 = np.arange(len(x_axis))
bar_2 = w+bar_1
bar_3 = bar_2+w

plt.bar(bar_1, gold, w, color="#008fd5", label="gold")
plt.bar(bar_2, silver, w, color="#fc4f30", label="silver")
plt.bar(bar_3, bronze, w, color="#6d904f", label="bronze")

plt.title("Madels for different countries")
plt.xlabel("Countries")
plt.ylabel("Number of madels")

plt.legend(loc="upper left", bbox_to_anchor=(.805, .94))
plt.xticks(bar_1+w, x_axis, color="red")

plt.tight_layout()
plt.show()
