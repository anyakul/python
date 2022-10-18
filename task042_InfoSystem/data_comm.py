import model
import menu
import json_model


def data_com():
    exit = True
    data = json_model.read_file()
    what = menu.get_menu_point()

    while exit == True:
        if what == 1:
            print(data)
        elif what == 2:
            model.search_user_data(data)
        elif what == 3:
            model.add_new_key(data)
        elif what == 4:
            model.delete_key(data)
        elif what == 5:
            model.add_new_user(data)
        elif what == 6:
            model.change_user_data(data)
        elif what == 7:
            model.delete_user_data(data)
        elif what == 8:
            model.save_data_in_file(data)
            exit = False
            break
        what = menu.get_menu_point()
