"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""
from kivy.app import App
from kivy.lang import Builder


class MilesConverterApp(App):
    """ Kivy App: Convert miles to kilometres, warning-free version."""
    MILES_TO_KM = 1.60934

    def build(self):
        """Build the main user interface of the app."""
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_calculate(self):
        """Handle the conversion when the user clicks the 'Calculate' button."""
        miles = self.get_miles_input()
        km = self.convert_value(miles)
        self.display_result(km)

    def handle_increment(self, step):
        """Handle increment button clicks to increase or decrease the miles input."""
        miles = self.get_miles_input() + step
        self.root.ids.input_miles.text = str(miles)
        km = self.convert_value(miles)
        self.display_result(km)

    def get_miles_input(self):
        """Retrieve and validate the miles input from the text field."""
        text = self.root.ids.input_miles.text
        try:
            return float(text)
        except ValueError:
            return 0.0

    def convert_value(self, miles):
        """Convert miles to kilometres."""
        return miles * self.MILES_TO_KM

    def display_result(self, km):
        """Display the converted kilometres value in the output label."""
        self.root.ids.output_label.text = f"{km:.3f}"


MilesConverterApp().run()
