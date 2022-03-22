import py_cui


class mainTUI:

    def __init__(self, master):
        self.master = master
        self.master.set_title("menu example 2")
        self.widget_set_A = self.master.create_new_widget_set(10, 10)
        self.widget_set_B = self.master.create_new_widget_set(10, 10)

        # MENU 1
        self.menu1 = self.widget_set_A.add_scroll_menu('menu_1', 0, 0, row_span=7, column_span=2)
        self.menu1.add_key_command(py_cui.keys.KEY_ENTER, self.handlecommand)
        self.master.apply_widget_set(self.widget_set_A)
        self.colorbutton = self.menu1.add_item("toggle red")
        self.menu1.add_item("tes2")

        # MENU 2
        self.menu2 = self.widget_set_B.add_scroll_menu('menu_2', 0, 0, row_span=7, column_span=2)
        self.menu2.add_key_command(py_cui.keys.KEY_ENTER, self.toggle_widget_1)


    def toggle_widget_1(self):
        self.master.apply_widget_set(self.widget_set_A)

    def toggle_widget_2(self):
        self.master.apply_widget_set(self.widget_set_B)

    def handlecommand(self):
        if "toggle red" in self.menu1.get():
            self.colorbutton.set_color(py_cui.RED_ON_BLACK)

root = py_cui.PyCUI(10, 10)
root.set_title('CUI TODO List')
s = mainTUI(root)
root.start()