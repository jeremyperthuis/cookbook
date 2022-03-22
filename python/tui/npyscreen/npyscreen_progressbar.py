import npyscreen


class ProcessBar(npyscreen.Slider):
    def __init__(self, *args, **keywords):
        super(ProcessBar, self).__init__(*args, **keywords)
        self.editable = False


class ProcessBarBox(npyscreen.BoxTitle):
    _contained_widget = ProcessBar


class TestApp(npyscreen.NPSApp):
    def main(self):
        self.F = npyscreen.Form(name="Welcome to Npyscreen", )
        self.s = self.F.add(ProcessBarBox, max_height=3, out_of=12, value=60, name="Text:")
        self.r = self.F.add(ProcessBarBox, max_height=3, out_of=12, value=60, name="Text:")


        #s.editable=False

        # This lets the user play with the Form.
        self.F.edit()
    def  while_editing(self):
        self.s.value = self.s.value+1


if __name__ == "__main__":
    App = TestApp()
    App.run()