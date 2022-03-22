import npyscreen

class app(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="TEST", lines = 20, columns = 20)
        self.addForm("SECOND", secondForm, name="TEST2")

class MainForm(npyscreen.Form):
    def create(self):
        #self.show_atx = 5
       # self.show_aty = 5
        self.add(npyscreen.Textfield, value="TEST")
    def afterEditing(self):
        self.parentApp.setNextForm("SECOND")

class secondForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.BoxBasic, name="Basic Box:", max_width=30, relx=2, max_height=3)
        self.footer = "This is a footer"

        self.box = self.add(npyscreen.BoxBasic, name="Basic Box:", rely=2, relx=32,
                   max_width=30, max_height=3)




if __name__ == '__main__':
    app =app().run()