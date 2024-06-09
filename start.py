from tkinter import *
import dates_time as datatime
from tkinter import ttk
import working_days_card as card
from tkinter import font
DAY_DATA = datatime.time_day
MONTH_DATA = datatime.time_month
# BUS_ROUTE = card.list_card[0]
# ROUTE_CARD = card.dct_num_card[card.list_card[0]][0]

class TimeLabel(Label):
    def __init__(self,parent,font,**kwargs):
        super().__init__(parent,font=font,relief=RAISED,**kwargs)


class  GUI_Work_time(Tk):
    def __init__(self):
        super().__init__()
        FONT = font.Font(family="Verdana", size=13, weight="bold", slant="roman")
        FONT_2 = font.Font(family="Verdana", size=20, weight="bold", slant="roman")
        self.num_smena = IntVar()
        self.marsh_var = StringVar()
        self.time_hour_out_park = StringVar()
        self.time_minutes_out_park = StringVar()
        self.time_end_work = StringVar()
        self.total_hour_var = StringVar()
        self.total_minutes_var = StringVar()

        root_frame = Frame(self)
        root_frame.pack(fill='x')

        frame_day = Frame(root_frame)
        frame_day.pack(side=LEFT, anchor=N)
        Label(frame_day, text='Число').pack()
        self.day_date = ttk.Combobox(frame_day,values=list(range(1,32)),width=3)
        self.day_date.pack(padx=5)
        self.day_date.set(DAY_DATA)

        frame_month = Frame(root_frame)
        frame_month.pack(side=LEFT, anchor=N)
        Label(frame_month, text='Месяц').pack()
        self.month_date = ttk.Combobox(frame_month,values=datatime.month_lst,width=10)
        self.month_date.pack()
        self.month_date.set(MONTH_DATA)

        frame_bus_rout = Frame(root_frame)
        frame_bus_rout.pack(side=LEFT, anchor=N)
        Label(frame_bus_rout, text='Маршрут').pack()
        self.bus_rout = ttk.Combobox(frame_bus_rout,values=list(card.dct_num_card.keys()),width=3,name='100')
        self.bus_rout.pack()
        self.bus_rout.set(3)

        frame_num_card = Frame(root_frame)
        frame_num_card.pack(side=LEFT, anchor=N)
        Label(frame_num_card, text='Карта').pack()
        self.num_card = ttk.Combobox(frame_num_card,values=card.dct_num_card[card.list_card[0]],width=2,name='101')
        self.num_card.pack()
        self.num_card.set(1)

        radio_I_sm = Radiobutton(root_frame,text='I смена',variable=self.num_smena,value=1)
        radio_I_sm.pack(side=LEFT,padx=5,pady=10)
        radio_II_sm = Radiobutton(root_frame,text='II смена',variable=self.num_smena,value=2)
        radio_II_sm.pack(side=LEFT,padx=5,pady=10)
        self.num_smena.set(1)

        main_label = ttk.LabelFrame(self, text='Информация о работе')
        main_label.pack(fill=X)

        frame_in_label_one = Frame(main_label)
        frame_in_label_one.pack(side=LEFT,anchor=N)
        Label(frame_in_label_one,text='Время выезда',font=FONT, bg='lightblue').pack(padx=5)

        frame_hour_out_park = Frame(frame_in_label_one)
        frame_hour_out_park.pack()
        time_hour_outpark_label = TimeLabel(frame_hour_out_park,
                                            textvariable=self.time_hour_out_park,bg='lightblue',font=FONT)
        time_hour_outpark_label.pack(side=LEFT)
        TimeLabel(frame_hour_out_park,text=':',font=FONT,bg='lightblue').pack(side=LEFT)
        time_minutes_outpark_label = TimeLabel(frame_hour_out_park,
                                               textvariable=self.time_minutes_out_park,bg='lightblue',font=FONT)
        time_minutes_outpark_label.pack(side=LEFT)
        self.time_hour_out_park.set('05')
        self.time_minutes_out_park.set('43')

        frame_in_label_two = Frame(main_label)
        frame_in_label_two.pack(side=LEFT, anchor=N)
        Label(frame_in_label_two, text='Конец работы',font=FONT, bg='lightblue').pack()

        info_time_label = Label(frame_in_label_two, textvariable=self.time_end_work,font=FONT, bg='lightblue')
        info_time_label.pack()
        # self.time_out_park.set('test 69-71')

        frame_in_label_three = Frame(main_label)
        frame_in_label_three.pack(side=LEFT)
        Label(frame_in_label_three, text='Обед',font=FONT, bg='lightgreen').pack()

        info_time_label = Label(frame_in_label_three, textvariable=self.time_end_work,font=FONT, bg='lightgreen')
        info_time_label.pack(anchor=E)
        self.time_end_work.set('test 79-81')

        time_label = ttk.LabelFrame(self, text='Отработка',labelanchor=N)
        time_label.pack(fill=X)
        frame_total_time_in_time_label = Frame(time_label)
        frame_total_time_in_time_label.pack()
        self.total_hour_Label = Label(frame_total_time_in_time_label,font=FONT_2,textvariable=self.total_hour_var)
        self.total_hour_Label.pack(side=LEFT)
        self.total_hour_var.set('15')
        Label(frame_total_time_in_time_label,text=':',font=FONT_2).pack(side=LEFT)
        self.total_minutes_Label = Label(frame_total_time_in_time_label,font=FONT_2,textvariable=self.total_minutes_var)
        self.total_minutes_Label.pack(side=LEFT)
        self.total_minutes_var.set('00')


        self.bus_rout.bind("<<ComboboxSelected>>",self.main_func)
        self.num_card.bind("<<ComboboxSelected>>",self.main_func)





    def main_func(self,event):
        if str(event.widget) == '.!frame.!frame3.100' and self.num_smena.get() == 1:
            print('OK')
            self.num_card['values'] = card.dct_num_card[self.bus_rout.get()] # получаем список карточек выбранного маршрута
            self.num_card.set(1)
            self.time_out_park.set(str(card.dct_work_cards_I[self.bus_rout.get()][self.num_card.get()][0])+":"+
            str(card.dct_work_cards_I[self.bus_rout.get()][self.num_card.get()][1]))


        elif str(event.widget) == '.!frame.!frame4.101':
            print('Карта')








if __name__ == '__main__':
    root = GUI_Work_time()
    root.geometry('500x500+1200+150')
    root.resizable(False,False)
    root.title('Учёт рабочего времени')
    root.mainloop()