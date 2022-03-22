# imports
import py_cui
import time
import os
import threading    # We will need the threading library when we want to use the loading popups

class PopupExample:

    def __init__(self, master):

        # This is a reference to our top level CUI object
        self.master = master

        # buttons for control - each simply spawns the linked popup
        self.show_message_popup = self.master.add_button('Show Message Popup', 0, 0,            command=self.show_message)
        self.show_yes_no_popup  = self.master.add_button('Show Yes No Popup',  1, 0,            command=self.show_yes_no)
        self.show_loading_icon_popup = self.master.add_button('Show Loading Icon Popup', 2, 0,  command=self.show_loading_icon)
        self.show_loading_bar_popup = self.master.add_button('Show Loading Bar Popup', 0,1,     command = self.show_loading_bar)
        self.show_text_box_popup = self.master.add_button('Show Text Box Popup', 1,1,           command = self.show_text_box)
        self.show_menu_popup = self.master.add_button('Show Scroll Menu Popup', 2,1,            command = self.show_menu_popup_fun)


    def show_message(self):
        """ Displays a simple message popup """

        self.master.show_message_popup('Hello!', 'This is a message popup. You can also spawn warnings and errors.')

    ################################################
    # YES NO POPUP

    def quit_cui(self, to_quit):
        # THis is the function given to the yes no popup. The to_quit parameter will be true if y is pressed, or False if n is pressed
        if to_quit:
            exit()
        else:
            self.master.show_message_popup('Cancelled', 'The quit operation was cancelled.')


    def show_yes_no(self):
        """ Displays a yes no popup asking if the user would like to quit """

        # For the yes/no popup, the 'command' parameter must take a function that requires a single boolean parameter
        self.master.show_yes_no_popup('Are you sure you want to quit?', self.quit_cui)

    ################################################

    ################################################
    # TEXTBOX POPUP

    def reset_title(self, new_title):
        self.master.set_title(new_title)


    def show_text_box(self):
        """ Displays a textbox popup asking the user for a new window title """

        # A textbox popup requires a prompt and a function reference. The function must take a single string parameter that will return
        # whatever is within the text box when the ENTER key is pressed
        self.master.show_text_box_popup('Please enter a new window title', self.reset_title)

    ################################################

    ################################################
    # SCROLL MENU POPUP

    def change_button_color(self, new_color):
        """ Function called when ENTER pressed in menu popup. Takes string as parameter """

        color = py_cui.WHITE_ON_BLACK
        if new_color == "RED":
            color = py_cui.RED_ON_BLACK
        elif new_color == "CYAN":
            color = py_cui.CYAN_ON_BLACK
        elif new_color == "MAGENTA":
            color = py_cui.MAGENTA_ON_BLACK
        for key in self.master.widgets.keys():
            if isinstance(self.master.get_widgets()[key], py_cui.widgets.Button):
                self.master.get_widgets()[key].set_color(color)

    def show_menu_popup_fun(self):
        """ Opens scroll menu for selecting button colors """

        # Spawning a menu popup must recieve a list of strings as menu options, and a function reference that takes a string parameter
        menu_choices = ['RED', 'CYAN', 'MAGENTA']
        self.master.show_menu_popup('Please select a new button color', menu_choices, self.change_button_color)

    ################################################

    def show_loading_icon(self):
        """ Function that shows the usage for spwaning a loading icon popup """

        # The loading popup will remain onscreen until the stop loading function is called. Call this before a large operation, and call
        # stop after the operation is finished. Note that for these long operations, you must use a different thread
        # to not block the draw calls.
        self.master.show_loading_icon_popup('Please Wait', 'Loading')
        operation_thread = threading.Thread(target=self.long_operation)
        operation_thread.start()


    def show_loading_bar(self):
        """ Function that shows the usage for spawning a loading bar popup """

        self.master.show_loading_bar_popup('Incrementing a counter...', 100)
        operation_thread = threading.Thread(target=self.long_operation)
        operation_thread.start()


    def long_operation(self):
        """ A simple function that demonstrates a long callback operation performed while loading popup is open """

        counter = 0
        for i in range(0, 100):
            time.sleep(0.1)
            counter= counter +1
            self.master.status_bar.set_text(str(counter))
            # When using a bar indicator, we will increment the completed counter. Will be ignored for loading icon popup
            self.master.increment_loading_bar()
        # This is what stops the loading popup and reenters overview mode
        self.master.stop_loading_popup()


# Create the CUI, pass it to the wrapper object, and start it
root = py_cui.PyCUI(3, 2)
root.set_title('CUI Popups Example')
s = PopupExample(root)
root.start()