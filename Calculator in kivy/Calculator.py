from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)

Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text="0"
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def button_press(self,button):
        prior = self.ids.calc_input.text
        if prior=="0":
            self.ids.calc_input.text=""
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text=f"{prior}{button}"
    def add(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}+"
    def subtract(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}-"
    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}+"
    def multiply(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}*"
    def divide(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}/"
    def percent(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}%"

    def dot(self):
        prior = self.ids.calc_input.text
        if "." in prior:
            pass
        else:
            self.ids.calc_input.text = f"{prior}."
    def equals(self):
        prior = self.ids.calc_input.text
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for number in num_list:
                answer = answer + float(number)
                self.ids.calc_input.text = str(answer)
        elif "-" in prior:
            num_list = prior.split("-")
            answer = 0
            for number in num_list:
                answer -= float(number)
                self.ids.calc_input.text = str(answer)
        elif "*" in prior:
            num_list = prior.split("*")
            answer = 1
            for number in num_list:
                answer = answer * float(number)
                self.ids.calc_input.text = str(answer)
        elif "/" in prior:
            prior = self.ids.calc_input.text
            num_list = prior.split("/")
            answer = 1
            for number in num_list:
                answer = answer / float(number)
                self.ids.calc_input.text = str(answer)
        elif "%" in prior:
            prior = self.ids.calc_input.text
            num_list = prior.split("%")
            answer = 1
            for number in num_list:
                answer = answer * int(number)*0.1
                self.ids.calc_input.text = str(answer)
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__=="__main__":
    CalculatorApp().run()