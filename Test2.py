from datetime import datetime
from time import sleep
import pytz

timezones = ['Europe/Dublin','Asia/Shanghai',]
localFormat = "%m-%d-%Y %H:%M:%S"

while True:
    try:
        utcmoment_naive = datetime.utcnow()
        localDatetimeBerlin = utcmoment_naive.astimezone(pytz.timezone('Europe/Berlin'))
        localDatetimeShanghai = utcmoment_naive.astimezone(pytz.timezone('Asia/Tokyo'))
        print('Berlin:{} \nShanghai:{}'.format(localDatetimeBerlin.strftime(localFormat),localDatetimeShanghai.strftime(localFormat)))
        sleep(1)
    except:
        print("Erro")
        