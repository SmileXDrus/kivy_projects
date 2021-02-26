import kivy
from random import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color


class BoxLayoutMenu(App):
    def build(self):
        layout = BoxLayout()
        names = ['Вторые блюда', 'Первые блюда', 'Салаты и закуски', 'Гарниры', 'Несладкая выпечка',
                 'Сладкая выпечка', 'Десерты без выпекания', 'Твороженые десерты', 'ПП торты и пироженые']
        for i in range(9):
            color = (random(), random(), random())
            btn = Button(text=names[i],
                         background_color=[*color]
                         )
            btn.color = color
            btn.bind(on_press=self.on_press_button)
            layout.add_widget(btn)
        return layout

    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')


if __name__ == "__main__":
    app = BoxLayoutMenu()
    app.run()
