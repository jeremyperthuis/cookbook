import npyscreen

"""
Basic menu navigation with 3 forms ans values passing between Forms
"""

# Top app where forms are registered
class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm(lines=47))

    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")

    def change_form(self, name):
        self.switchForm(name)

# Main Form with 2 buttons
class MainForm(npyscreen.Form):
    def on_ok(self):
        self.parentApp.switchForm(None)


    def computeStuff(self):
        vl = []
        for x in range(40):
            pass
            vl.append("Value %s" % x)
        self.add(npyscreen.MultiSelect, values=vl)

    def create(self):
        self.title = self.add(npyscreen.TitleText, name="MAIN SCREEN", value="Hello World!")
        self.add(npyscreen.Textfield, value='Testing Testing')
        t = F.add(MultiSelectWidgetTesting, max_height=7, name="Testing", values=value_list, slow_scroll=False)
        # self.add(npyscreen.Textfield, value='Testing Testing')
        #self.button1 = self.add(npyscreen.ButtonPress, when_pressed_function=self.computeStuff, name="compute")


if __name__ == "__main__":
    tui = App()
    tui.run()