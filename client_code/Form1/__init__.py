from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_file = self.text_box_1.text
    sheetname = self.text_box_2.text
    output_file = self.text_box_3.text
    low_confidence_score = self.text_box_4.text
    xmed_confidence_score = self.text_box_5.text
    Notification('hey').show()
    

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
