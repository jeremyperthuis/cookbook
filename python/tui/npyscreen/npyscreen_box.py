import npyscreen

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm)

class MainForm(npyscreen.FormBaseNew):
    def create(self):
        y, x = self.useable_space()
        self.box1 = self.add(Box1, name="box 1".format(str(x), str(y)), values=("test","test"), relx=2, max_width=x//3, rely=1, max_height=y//3)
        self.box2 = self.add(Box2, name="box 2".format(str(x), str(y)), footer = "footer", value=0, relx=(x//3)+3, max_width= -1, rely=1,max_height=y//3)
        self.box3 = self.add(Box3, name="box 3".format(str(x), str(y)), value=0, relx=2, max_width=-1, rely=(y//3)+1,max_height=-1)

class Box1(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLine

class Box2(npyscreen.BoxTitle):
    pass

class Box3(npyscreen.BoxTitle):
    pass

if __name__ == '__main__':
    app = App()
    app.run()