"""
Basic App for listing names
Author: Cameron Lane
Estimated Finish Time: 25 min
Finish Time: 30 min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Main program - Basic Kivy app for dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # List of names
        self.names = ["Jeff", "Tom", "Sabrina", "Ella", "Mike", "Fred"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from names list and add them to GUI."""
        for name in self.names:
            # Create label for each name
            temp_label = Label(text=name)
            # Add label to "main" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()