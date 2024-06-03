from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


KV = """
MyBL:
        orientation: "vertical"
	    size_hint: (0.95, 0.95)
	    pos_hint: {"center_x": 0.5, "center_y":0.5}


        Label:
                font_size: "30sp"
                text: root.data_label
        Button:
                text: "Поиск по названию"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()

        Button:
                text: "Поиск по описанию"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback2()

        Button:
                text: "Случайный"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback3()

        Button:
                text: "Отправить"
                bold: True
                background_color:'#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback4()



"""

class MyBL(BoxLayout):

    data_label = StringProperty("Треугольник!")
	
	# 	threading.Thread(target=self.get_data).start()
def callback(self):
		print("Поиск по названию")
		# self.client.sendall(bytes("Поиск по названию",'UTF-8'))

def callback2(self):
		print("Поиск по описанию")
		# self.client.sendall(bytes("Поиск по описанию",'UTF-8'))
def callback3(self):
		print("Случайный")
		# self.client.sendall(bytes("Случайный",'UTF-8'))
def callback4(self):
		print("Отправить")
		# self.client.sendall(bytes(self.ids.Inp.text,'UTF-8'))



class MyApp(App):
	
	running = True
	def process(self):
		text = self.root.ids.Inp.text
	def build(self):

		return Builder.load_string(KV)

	def on_stop(self):
		self.running = False

MyApp().run()

