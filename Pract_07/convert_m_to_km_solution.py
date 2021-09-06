"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934


FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.updated_result(miles)

    def handle_increment(self, text, change):
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def updated_result(self, miles):
        print("update")
        self.output_km = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
