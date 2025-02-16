from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from pdf_agent import download_papers

class PDFAgentGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(PDFAgentGUI, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.title_input = TextInput(hint_text='Enter paper title or DOI', multiline=False)
        self.add_widget(self.title_input)

        self.download_button = Button(text='Download PDF')
        self.download_button.bind(on_press=self.download_pdf)
        self.add_widget(self.download_button)

        self.status_label = Label(text='')
        self.add_widget(self.status_label)

    def download_pdf(self, instance):
        paper_title = self.title_input.text
        if paper_title:
            self.status_label.text = f'Downloading: {paper_title}'
            download_papers([paper_title], 'downloaded_papers')
            self.status_label.text = f'Download complete for: {paper_title}'
        else:
            self.status_label.text = 'Please enter a title or DOI.'

class PDFAgentApp(App):
    def build(self):
        return PDFAgentGUI()

if __name__ == '__main__':
    PDFAgentApp().run()