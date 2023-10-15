from view import *
from db import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
            info = get_info()
            write_data(info)
        if ans == 2:
            search_delit = delit_data()
            delite_data(search_delit)
        if ans == 3:
            search = change_data()
            change(search)



            



main()