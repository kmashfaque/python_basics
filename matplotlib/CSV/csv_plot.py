from matplotlib import pyplot as plt
from collections import Counter
import csv

# plt.style.use("fivethirtyeight")

# with open("py\matplotlib\CSV\c_s_v_data.csv") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     language_counter = Counter()

#     for row in csv_reader:
#         language_counter.update(row["LanguagesWorkedWith"].split(";"))
# print(language_counter.most_common(15))

# language = []
# popularity = []

# for item in language_counter.most_common(15):
#     language.append(item[0])
#     popularity.append(item[1])

# print(language)
# print(popularity)

# language.reverse()
# popularity.reverse()

# plt.barh(language, popularity)
# plt.ylabel("Number of people using")
# plt.tight_layout()
# plt.show()


# c = ["python", "javascript", "C++", "java", "javascript", "java"]
# count = Counter(c)
# count.update({"python", "javascript"})
# count.update({"python", "javascript"})
# count.update({"python", "javascript"})
# count.update({"python", "javascript"})
# count.update({"python", "javascript"})
# print(count)


sales = Counter(banana=15, tomato=4, apple=39, orange=30)

# All objects in reverse order
# sales.most_common()[::-1]
# [('tomato', 4), ('banana', 15), ('orange', 30), ('apple', 39)]

# The two least-common objects
# print(sales.most_common()[:-2:-1])
