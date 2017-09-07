import os
import time
import datetime

#创建日报日志
def write_log(log_body,log_tail = '\n'):
    log=' '.join([str(time.strftime('%Y-%m-%d %H:%M:%S')), log_body, log_tail])
    with open(r'C:\Users\guofurong_sh\PycharmProjects\mp\dailyreport.txt', 'a') as ilog:
        ilog.write(log)

#获取日报日期
def get_date():
    now=datetime.date.today()
    delta=datetime.timedelta(days=1)
    yestday=now-delta
    time_1=time.mktime(yestday.timetuple())
    time_2= time.localtime(time_1)
    yestday_date = time.strftime("%Y%m%d", time_2)
    if yestday_date:
        log='设置日报日期为:{}'.format(yestday_date)
        write_log(log)
        return (yestday_date)
    else:
        log = "日期错误！"
        write_log(log)
        return false

#打开桌面文件
def find_file(yestday_date):
    filename = '日报{}.xlsb'.format(str(yestday_date))
    file_path = r'D:\baidu\Desktop'
    file = os.path.join(file_path, filename)
    if os.path.exists(file):
        log = '日报已存在！'
        write_log(log)
    else:
        pass

find_file(get_date())