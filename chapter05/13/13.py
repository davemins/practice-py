"""
Every week Report 1-50
-------------------
- Weekly Report n -

Department   :
Name         :
Work Summary :

"""


for n in range(1, 51):
    report_file = open("report{}.txt".format(n), "w")
    print("- Weekly Report {} -".format(n), file=report_file)
    print("", file=report_file)
    print("Department   :", file=report_file)
    print("Name         :", file=report_file)
    print("Work Summary :", file=report_file)
    report_file.close()
