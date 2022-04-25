#OOP
#class
#__init__
#self
#def -  metode

#Vilcienu saraksts

class InfoSistema():
  def __init__(self):
    pass



import PySimpleGUI as sg

sg.theme('DarkAmber')   
layout = [  [sg.Text('Dzelzceļa informācijas sistēma')],
            [sg.Text('Sākumpunkts:'), sg.InputText()],
            [sg.Text('Galamērķis: '), sg.InputText()],
            [sg.Button('Meklēt')]] #Meklēšana failā

layout2 = [[sg.Text("Kaut kāds teksts")]]

tabgrp = [
  [
    sg.TabGroup([[
      sg.Tab("Maršruts",layout),
      sg.Tab('Visi maršruti',layout2)
    ]]),
    sg.Button('Aizvērt')
  ]
]

window = sg.Window('InfSistēma', tabgrp)
while True:
  event, values = window.read()
  
