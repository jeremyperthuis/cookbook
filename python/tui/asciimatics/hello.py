#!/usr/bin/env python3

from asciimatics.widgets import Frame, TextBox, Layout, Label, Divider, Text, \
    CheckBox, RadioButtons, Button, PopUpDialog, TimePicker, DatePicker, DropdownList, PopupMenu,Widget, ListBox
from asciimatics.effects import Background
from asciimatics.event import MouseEvent
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, NextScene, StopApplication, \
    InvalidFields
from asciimatics.parsers import AsciimaticsParser
import sys
import re
import datetime
import logging

logging.basicConfig(filename="forms.log", level=logging.INFO)


# Initial data for the form


class TestModel(object):
    def __init__(self):
        self.attr=[]

class MainFrame(Frame):
    def __init__(self, screen, model):
        super(MainFrame, self).__init__(screen,
                                        width=int(screen.width),
                                        height=int(screen.height),
                                        on_load=self._reload_list,
                                        has_shadow=True,
                                        name="My Form")
        self.set_theme("monochrome")
        self._model = model
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._list_view = ListBox(
                        Widget.FILL_FRAME,
                        [(x["name"], i) for i,x in enumerate(self._model.attr)],
                        name="contacts",
                        add_scroll_bar=True,)
        layout.add_widget(self._list_view)

        if bool(self.data):
            self._list_view_2 = ListBox(
                Widget.FILL_FRAME,
                ["testdzdzdz"],
                name="contacts2",
                add_scroll_bar=True, )
            layout.add_widget(self._list_view)


        layout2 = Layout([1,1])
        self.add_layout(layout2)
        layout2.add_widget(Button("Config", self._config), 0)
        layout2.add_widget(Button("Quit", self._quit), 1)

        self.fix()

    @staticmethod
    def _config():
        raise NextScene("Configuration")

    def _reload_list(self, new_value=None):
        self._list_view.options = [(x["name"], i) for i,x in enumerate(self._model.attr)]
        self._list_view.value = new_value
        logging.info("list_view options : {}".format(self._list_view.options))
        logging.info("list_view value : {}".format(self._list_view.value))
        logging.info("data : {}".format(self.data))
        if not bool(self.data):
            logging.info("none Data !")

    def _quit(self):
        self._scene.add_effect(
            PopUpDialog(self._screen,
                        "Are you sure?",
                        ["Yes", "No"],
                        has_shadow=True,
                        on_close=self._quit_on_yes))

    @staticmethod
    def _quit_on_yes(selected):
        # Yes is the first button
        if selected == 0:
            raise StopApplication("User requested exit")

class ConfigurationFrame(Frame):
    def __init__(self, screen, model):
        super(ConfigurationFrame, self).__init__(screen,
                                        width=int(screen.width/2),
                                        height=int(screen.height/2),

                                        has_shadow=True,
                                        name="My Form")
        self.set_theme("monochrome")
        self._model = model
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(Text("Name:", "name"))
        layout.add_widget(DropdownList(
            [("Item 1", "1"),
             ("Item 2", "2"),
             ("Item 3", "3")],
label="Nombre Box to display",name="item"))
        layout2 = Layout([1,1])
        self.add_layout(layout2)
        layout2.add_widget(Button("OK", self._ok),0)
        layout2.add_widget(Button("Quit", self._quit),1)

        self.fix()


    def _quit(self):
        raise NextScene("Main")

    def _ok(self):
        self.save()
        logging.info("data={}".format(self.data))
        self._model.attr.append(self.data)
        raise NextScene("Main")



def demo(screen, scene):
    scenes = [
        Scene([MainFrame(screen, model)], -1, name="Main"),
        Scene([ConfigurationFrame(screen, model)], -1, name="Configuration")
    ]

    screen.play(scenes, stop_on_resize=True, start_scene=scene, allow_int=True)

model = TestModel()
last_scene = None
while True:
    try:
        Screen.wrapper(demo, catch_interrupt=False, arguments=[last_scene])
        sys.exit(0)
    except ResizeScreenError as e:
        last_scene = e.scene