"""
CP1404 - Practical 8 box_layout_demo Task
Estimated finish time: 25 min
Finish time: 20 min
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """ Build GUI. """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """ Handles greet events updating GUI. """
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """ Handles clear events resetting GUI. """
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ''

BoxLayoutDemo().run()
