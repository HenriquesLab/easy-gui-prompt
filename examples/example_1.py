from easy_gui_prompt import EasyGUI

gui = EasyGUI("example_1")

gui.add_header("Questionaire")
gui.add_int_range("a_number", "Enter a number", vmin=1, vmax=100, remember_value=True)
