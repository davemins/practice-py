import datetime

start_time = input("Start Time : ")
start = start_time
date_start = datetime.datetime.strptime(str(start), '%H%M')
dateformat = "%H시%M분"
tmp_start = date_start.strftime(dateformat)
print(tmp_start)

end_time = input("End Time : ")
end = end_time
date_end = datetime.datetime.strptime(str(end), '%H%M')
dateformat = "%H시%M분"
tmp_end = date_end.strftime(dateformat)
print(tmp_end, '\n')

i = 0

while i != 'end':
    date_cur = datetime.datetime.now()
    dateformat = "%H시%M분"
    tmp_cur = date_cur.strftime(dateformat)

    elap_time = date_cur - date_start  
    rem_time = date_end - date_cur
    print("cur_time : {} || elap_time : {}시간 {}분 || rem_time : {}시간 {}분".format(tmp_cur, int((elap_time).seconds / 3600), int(((elap_time).seconds % 3600) / 60), int((rem_time).seconds / 3600), int(((rem_time).seconds % 3600) / 60)))

    i = input("")
