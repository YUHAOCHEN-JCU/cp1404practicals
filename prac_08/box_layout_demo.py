from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """A simple Kivy App that demonstrates the use of BoxLayout
    with input, output, and button event handling."""
    def build(self):
        """Build the root widget from the KV file and set the app title."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greeting action by updating the output label with the user's input."""
        print("test")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
         """Clear the input TextInput and output Label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
