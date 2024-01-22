from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def build(self):
        # List of names (model/data)
        names = ["Alice", "Bob", "Charlie", "David"]

        # Root layout
        root = BoxLayout(orientation='vertical')

        # Child layout
        main_layout = BoxLayout(orientation='vertical')

        # Dynamically create Labels for each name and add to the layout
        for name in names:
            label = Label(text=name, size_hint_y=None, height=40)
            main_layout.add_widget(label)

        # Add the layout to the root layout
        root.add_widget(main_layout)

        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()