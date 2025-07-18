from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Kivy App: Dynamically create and display labels for a list of names."""
    def build(self):
        """Build the user interface of the app."""
        root = Builder.load_file("dynamic_labels.kv")
        names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
        for name in names:
            root.ids.main.add_widget(Label(text=name, font_size=24))
        return root


DynamicLabelsApp().run()
