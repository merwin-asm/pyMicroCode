import kivy
import micro_core_6 as pyMicroCode
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class window_contents(GridLayout):
    def __init__(self,**kwargs):
        super(window_contents,self).__init__(**kwargs)
        self.pyMicroCode = pyMicroCode.MicroCode()
        self.cols = 1
        self.rows = 3
        self.padding = 30
        self.spacing = 20
        self.add_widget(Label(text="Micro Code",font_size=37))
        self.main_content = GridLayout()
        self.main_content.cols = 2
        self.main_content.rows = 4
        self.add_widget(self.main_content)
        self.label_1 = Label(text="File Name : ",font_size=20)
        self.main_content.add_widget(self.label_1)
        self.inp_1 = TextInput(multiline=False)
        self.main_content.add_widget(self.inp_1)
        self.label_2 = Label(text="File Data : ", font_size=20)
        self.main_content.add_widget(self.label_2)
        self.inp_2 = TextInput(multiline=True)
        self.main_content.add_widget(self.inp_2)
        self.label_3 = Label(text="Password : ", font_size=20)
        self.main_content.add_widget(self.label_3)
        self.inp_3 = TextInput(multiline=False)
        self.main_content.add_widget(self.inp_3)
        self.label_4 = Label(text="                                                 Note : The password should be  6 letter.",color=(1,0,0,0.7), font_size=10,)
        self.main_content.add_widget(self.label_4)
        self.main_content.spacing = 10
        self.down_content = GridLayout()
        self.down_content.rows = 1
        self.down_content.cols = 2
        self.add_widget(self.down_content)
        self.submit_button = Button(text="Create",font_size=20,background_normal="",background_color=(0.305882353,233/255,163/255,1),size_hint_x=None,
                                    size_hint_y=None,height=100,width=200,)
        self.submit_button.bind(on_press=self.create)
        self.down_content.add_widget(self.submit_button)
        self.read_button = Button(text="Read",font_size=20,background_normal="",background_color=(0.305882353,233/255,163/255,1),size_hint_x=None,
                                    size_hint_y=None,height=100,width=200)
        self.read_button.bind(on_press=self.read_)
        self.down_content.padding = 40
        self.down_content.spacing = 260
        self.down_content.add_widget(self.read_button)
    def create(self,in_):
        print("Creating...")
        file_name = self.inp_1.text
        data = self.inp_2.text
        password = self.inp_3.text
        self.inp_1.text = ""
        self.inp_2.text = ""
        self.inp_3.text = ""
        print(f"File_name : {file_name} /// Data : {data} /// Password : {password}")
        try:
            self.pyMicroCode.write(file_name,data,password)
        except:
            pass
    def read_(self,in_):
        print("Reading...")
        file_name = self.inp_1.text
        password = self.inp_3.text
        self.inp_1.text = ""
        self.inp_2.text = ""
        self.inp_3.text = ""
        print(f"File_name : {file_name} /// Password : {password}")
        try:
            ret , data= self.pyMicroCode.read(file_name,password)
            if ret == False:
                self.label_4.text = "Password Wrong / Wrong Micro Code"
            else:
                self.label_4.text = data
        except:
            pass
class mainApp(App):
    def build(self):
        self.title = "Micro Code"
        return window_contents()

if __name__ == '__main__':
    app = mainApp()
    _fixed_size = (800, 600)  # desired fix size
    def reSize(*args):
        Window.size = _fixed_size
        return True
    Window.bind(on_resize=reSize)
    app.run()
