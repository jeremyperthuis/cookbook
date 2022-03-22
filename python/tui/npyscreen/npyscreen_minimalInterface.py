import npyscreen

"""
Basic menu navigation with 3 forms ans values passing between Forms
"""

# Top app where forms are registered
class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm())
        self.registerForm("screen1", Screen1())
        self.registerForm("screen2", Screen2())

    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")

    def change_form(self, name):
        self.switchForm(name)

# Main Form with 2 buttons
class MainForm(npyscreen.Form):
    def on_ok(self):
        self.parentApp.switchForm(None)

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def changeToSecondForm(self):
        self.parentApp.change_form("screen2")

    def changeToFirstForm(self):
        self.parentApp.change_form("screen1")

    def create(self):
        self.title = self.add(npyscreen.TitleText, name="MAIN SCREEN", value="Hello World!")
        self.button1 = self.add(npyscreen.ButtonPress, when_pressed_function=self.changeToFirstForm, name="screen1")
        self.button1 = self.add(npyscreen.ButtonPress, when_pressed_function=self.changeToSecondForm, name="screen2")


class Screen1(npyscreen.ActionForm):
    def create(self):
        self.title = self.add(npyscreen.TitleText, name="screen1", value="Hello World!")
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")

    def on_ok(self):
        toMain = self.parentApp.getForm("MAIN")
        toMain.title.value = "Hello World Modified from screen1!"
        toMain = self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        toMain = self.parentApp.getForm("MAIN")
        toMain.title.value = "Hello World !"
        toMain = self.parentApp.switchForm("MAIN")


class Screen2(npyscreen.ActionForm):
    def create(self):
        self.title = self.add(npyscreen.TitleText, name="screen2", value="Hello World!")
    def afterEditing(self):
        self.parentApp.setNextForm("MAIN")

    def on_ok(self):
        toMain = self.parentApp.getForm("MAIN")
        toMain.title.value = "Hello World Modified from screen2!"
        toMain = self.parentApp.switchForm("MAIN")

    def on_cancel(self):
        toMain = self.parentApp.getForm("MAIN")
        toMain.title.value = "Hello World !"
        toMain = self.parentApp.switchForm("MAIN")

if __name__ == "__main__":
    tui = App()
    tui.run()