site = "http://google.com"
dot = site.find(".")
remain = site[7:dot]
len = len(remain)
count_e = site.count("e")
password = remain[0:3] + str(len) + str(count_e) + '!' #[0,3]-> 3 직전까지

print("{0} 의 비밀번호는 {1}입니다".format(site, password))

