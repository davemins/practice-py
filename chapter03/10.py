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

    #print("cur_time : {0} | elap_time : {1} | rem_time : {2}".format(tmp_cur, tmp_cur, tmp_cur))
    
    i = input("")
