import py_cui

class mainTUI:
    def __init__(self, master):
        self.master = master
        self.menu = self.master.add_scroll_menu('menu_1', 0, 0, row_span=7, column_span=2)
        self.menu.add_form("command_1")
        self.menu.add_key_command(py_cui.keys.KEY_ENTER, self.menu1_command_handler)

    def menu1_command_handler(self):
        self.menu.add_item("command_2")



root = py_cui.PyCUI(10, 10)
root.set_title('CUI TODO List')
s = mainTUI(root)
root.start()