import time


month_lst = [None,'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
             'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']


time_now = time.time()
time_day = time.localtime(time_now)[2]
time_month = month_lst[time.localtime(time_now)[1]]




