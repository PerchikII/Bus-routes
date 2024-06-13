import time
from datetime import timedelta




month_lst = [None,'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
             'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


time_now = time.time()
time_day = time.localtime(time_now)[2]
time_month = month_lst[time.localtime(time_now)[1]]

def work_time_calc(hour_begin:str, min_begin:str, end_hour:str, end_minutes:str):
    H_b = int(hour_begin)
    M_b = int(min_begin)
    End_H = int(end_hour)
    End_M = int(end_minutes)

    time_begin = timedelta(hours=H_b,minutes=M_b)
    time_end = timedelta(hours=End_H,minutes=End_M)
    return time_end - time_begin







