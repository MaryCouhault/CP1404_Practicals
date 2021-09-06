from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Abhi", "Shawl", "Dag", "Dog", "BRECK"]

    def build(self):
        self.title = "Dynamic Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_label(self):
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return


DynamicLabels().run()
