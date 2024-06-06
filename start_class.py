from tkinter import *
import dates_time as datatime
from tkinter import ttk
import working_days_card as card


class  GUI_Work_time(Tk):
    def __init__(self):
        super().__init__()
        frame_day = Frame(self)
        frame_day.pack(side=LEFT, anchor=N)
        Label(frame_day, text='Число').pack()
        self.day_date = ttk.Combobox(frame_day,values=list(range(1,32)),width=3)
        self.day_date.pack(padx=5)
        self.day_date.set(datatime.time_day)

        frame_month = Frame(self)
        frame_month.pack(side=LEFT, anchor=N)
        Label(frame_month, text='Месяц').pack()
        self.month_date = ttk.Combobox(frame_month,values=datatime.month_lst,width=10)
        self.month_date.pack()
        self.month_date.set(datatime.time_month)

        frame_bus_rout = Frame(self)
        frame_bus_rout.pack(side=LEFT, anchor=N)
        Label(frame_bus_rout, text='Маршрут').pack()
        self.bus_rout = ttk.Combobox(frame_bus_rout,values=list(card.dct_num_card.keys()),width=3)
        self.bus_rout.pack()
        self.bus_rout.set(card.list_card[0])

        frame_num_card = Frame(self)
        frame_num_card.pack(side=LEFT, anchor=N)
        Label(frame_num_card, text='Карта').pack()
        self.num_card = ttk.Combobox(frame_num_card,values=card.dct_num_card[card.list_card[0]],width=2)
        self.num_card.pack()
        self.num_card.set(1)



        self.bus_rout.bind("<<ComboboxSelected>>",self.choice_bus_route)

    def choice_bus_route(self,event):
        print(self.bus_rout.get(),self.num_card.get())








if __name__ == '__main__':
    root = GUI_Work_time()
    root.geometry('500x500+1200+150')
    root.resizable(False,False)
    root.title('Учёт рабочего времени')
    root.mainloop()