from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    input_file = self.file_loader_1.file  # The file loaded by the FileLoader
    sheetname = self.text_box_2.text
    output_file = self.text_box_3.text
    low_confidence_score = float(self.text_box_4.text)
    xmed_confidence_score = float(self.text_box_5.text)

    try:
      output_file = anvil.server.call(
          'standardize', 
          input_file, 
          sheetname, 
          output_file,  
          low_confidence_score,
          xmed_confidence_score
      )
      # Handle the returned output file (provide it for download)
      
    except Exception as e:
      # Handle errors
      return("error", e)

    self.download_link.visible = True
    self.download_link.text = "Download output file"
    self.download_link.file = output_file

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.text_box_1.text = file.name

  def download_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
