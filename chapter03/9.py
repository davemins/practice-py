import datetime

end_time = input("End Time : ")
end = end_time

date_end = datetime.datetime.strptime(str(end), '%H%M')
dateformat = "%H시%M분"
tmp_end = date_end.strftime(dateformat)
date_to_compare = datetime.datetime.strptime(str(end), "%H%M")

print(tmp_end, '\n')



date_cur = datetime.datetime.now()
dateformat = "%H시%M분"
tmp_cur = date_cur.strftime(dateformat)


elap_time = date_to_compare - date_cur 

print("{}시간 {}분".format(int((elap_time).seconds / 3600), int(((elap_time).seconds % 3600) / 60)))