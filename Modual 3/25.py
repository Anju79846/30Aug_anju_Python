#  Write a Python program to unzip a list of tuples into individual lists.

Student_Data = [("Ankush",101),("Nirav",102),("Mahesh",103)]
print("original Data is:" + str(Student_Data))

Stdata=list(zip(*Student_Data))

print("Midified list is" + str(Stdata))