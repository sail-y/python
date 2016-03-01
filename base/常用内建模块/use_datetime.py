from datetime import datetime, timedelta

now = datetime.now()
print(now)

dt = datetime(2016, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())

print(datetime.fromtimestamp(1461039600))
print(datetime.utcfromtimestamp(1461039600))


cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)


print(now.strftime('%Y-%m-%d %H:%M:%S'))

print(now + timedelta(hours=10))