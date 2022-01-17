import datetime

end_time = input("End Time : ")
end = end_time

date_end = datetime.datetime.strptime(str(end), '%H%M')
dateformat = "%H시%M분"
tmp_end = date_end.strftime(dateformat)

print(tmp_end, '\n')



date_cur = datetime.datetime.now()
dateformat = "%H시%M분"
tmp_cur = date_cur.strftime(dateformat)


elap_time = date_cur + datetime.timedelta(days=777)
print(elap_time)

