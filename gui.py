import func
import FreeSimpleGUI as fsg

lable = fsg.Text("type in a todo")
input_box = fsg.InputText('enter todo')
add_buttom = fsg.Button('add')

window =fsg.Window('My To-Do app' , layout=[[lable,input_box , add_buttom]])
window.read()
window.close()