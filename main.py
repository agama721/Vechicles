import sys
import base as bs
import pandas as pd


class Menu:

    def __init__(self):
        self.choices = {
                '1': self.add_c,
                '2': self.del_c,
                '3': self.view_c,
                '4': self.up_c,
                '5': self.exp_c,
                '6': self.quit_c
                }

    def display_menu(self):
        print(' Automotive Inventory \n'
              '----------------------\n'
              ' #1 Add Vehicle to Inventory \n'
              ' #2 Delete Vehicle from Inventory \n'
              ' #3 View Current Inventory \n'
              ' #4 Update Vehicle in Inventory \n'
              ' #5 Export Current Inventory \n'
              ' #6 Quit')

    ed = pd.read_csv('d_base.csv')

    def add_c(self):
        bs.c_base(), Menu().run()

    def del_c(self):
        if pd.DataFrame(self.ed).empty:
            no_data()
        else:
            bs.del_row(), Menu().run()

    def view_c(self):
        if pd.DataFrame(self.ed).empty:
            no_data()
        else:
            bs.view_data(), Menu().run()

    def up_c(self):
        if pd.DataFrame(self.ed).empty:
            no_data()
        else:
            bs.del_row(), bs.c_base(), Menu().run()

    def exp_c(self):
        if pd.DataFrame(self.ed).empty:
            no_data()
        else:
            bs.ex_data(), Menu().run()

    def quit_c(self):
        print('Thank you for using Automotive Inventory!')
        sys.exit()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print('{0} is not a valid choice'.format(choice))


def no_data():
    print('No Data In The Inventory!')
    print()
    Menu().run()


Menu().run()
