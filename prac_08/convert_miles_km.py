"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to km
Estimated Finish Time (Both .py and .kv): 20 min
Finish Time: 30min
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM_FACTOR = 1.60934

class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to kilometers """

    output_km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers."
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, text, change):
        """ Handle input incrementation. """
        result = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(result)


    def handle_calculate(self, text):
        """ Handle calculation (could be button press or other call), output result to label widget. """
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def update_result(self, miles):
       self.output_km = str(miles * MILES_TO_KM_FACTOR)

    @staticmethod
    def convert_to_number(text):
        """ Convert text into float or 0.0 if input invalid. """
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKmApp().run()