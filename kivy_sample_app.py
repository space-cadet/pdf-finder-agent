from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SampleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Hello, Kivy!")
        button = Button(text="Click Me")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"

if __name__ == "__main__":
    SampleApp().run()