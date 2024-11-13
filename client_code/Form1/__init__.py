from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    uploaded_file = self.file_loader_1.file  # This is the file uploaded through the FileLoader component
        
        # If there's no file uploaded, alert the user
    if not uploaded_file:
      alert("Please upload a file before submitting.")
      return
        
        # Get the values from the text boxes
      sheetname = self.text_box_2.text
      output_file = self.text_box_3.text
      low_confidence_score = float(self.text_box_4.text)  # Assuming these values are numeric
      xmed_confidence_score = float(self.text_box_5.text)

      # Call the server function and pass the file
      result = anvil.server.call('standardize',
                                  uploaded_file,  # Pass the uploaded file object
                                  sheetname,
                                  output_file,
                                  low_confidence_score,
                                  xmed_confidence_score
                                )

      # You can use `result` to display feedback to the user if needed
      alert(result)
    

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
            self.text_box_1.text = file.name
