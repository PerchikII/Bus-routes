import random as rd

def lst_rand_num():
    return [rd.randint(1, 100) for x in range(8)]

list_card = ['3', '16', '22', '73', '102', '107']

dct_num_card = {'3': [1, 2, 3, 4, 5, 6],
                '16': [1, 2, 3, 4, 5, 6],
                '22': [1, 2, 3, 4, 5, 6],
                '73': [1, 2, 3, 4, 6, 7],
                '102': [1, 2, 3, 4, 5, 6],
                '106': [1, 2, 3, 4, 5, 6, 7],
                '107': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                }

dct_work_cards_I = {('3', '1'): lst_rand_num(),
                    ('3', '2'): lst_rand_num(),
                    ('3', '3'): lst_rand_num(),
                    ('3', '4'): lst_rand_num(),
                    ('3', '5'): lst_rand_num(),
                    ('3', '6'): lst_rand_num(),


                    ('102', '1'): lst_rand_num(),
                    ('102', '2'): lst_rand_num(),
                    ('102', '3'): lst_rand_num(),
                    ('102', '4'): lst_rand_num(),
                    ('102', '5'): lst_rand_num(),
                    ('102', '6'): lst_rand_num(),

                    ('106', '1'): lst_rand_num(),
                    ('106', '2'): lst_rand_num(),
                    ('106', '3'): lst_rand_num(),
                    ('106', '4'): lst_rand_num(),
                    ('106', '5'): lst_rand_num(),
                    ('106', '6'): lst_rand_num(),
                    ('106', '7'): lst_rand_num(),



                    }






dct_work_cards_II = {('102', '1'): [14, 39, 22, 2, 19, 53, 20, 36],
                     ('102', '2'): [16, 12, 1, 00, 19, 35, 20, 12],
                     ('102', '3'): [15, 37, 00, 29, 20, 40, 21, 35]
                     }


