import pandas
import csv
# with open('py\c_s_v\python.csv', "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(row)


# with open('py\c_s_v\python.csv', "r") as csv_file:
# csv_reader = csv.DictReader(csv_file, delimiter=',')
# line_count = 0
# for row in csv_reader:
#     if line_count == 0:
#         print(f'Column names are {", ".join(row)}')
#         line_count += 1
#     print(
#         f'\t{row["name"]} works in the {row["department"]} department and was born in .')
#     line_count += 1
# print(f'Processed {line_count} lines.')


# df = pandas.read_csv("py\c_s_v\hrdata.csv")
# print(df)


# writing the csv file
# with open("py\c_s_v\c_s_v_file.csv", "w")as csvfile:
#     filednames = ["first_name", "last_name", "Rank"]
#     writer = csv.DictWriter(csvfile, fieldnames=filednames)
#     writer.writeheader()
#     writer.writerow(
#         {"Rank": "B", "first_name": "Parker", "last_name": "brian"})
#     writer.writerow({"Rank": "A", "first_name": "Smith",
#                     "last_name": "Rodriguez"})
#     writer.writerow({"Rank": "B", "first_name": "Jane", "last_name": "Oscar"})
#     writer.writerow({"Rank": "B", "first_name": "Jane", "last_name": "Loive"})
# print("Writing Complete")


df = pandas.read_csv("py\c_s_v\hrdata.csv",
                     index_col="Employee",
                     parse_dates=["Hired"],
                     header=0,
                     names=["Employee", "Hired", "Salary", "Sick Days"]
                     )

df.to_csv("py\c_s_v\hrdata_modified.csv")
