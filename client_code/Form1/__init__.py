from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.out = ""
    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def create_param_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    results,name,params = anvil.server.call('calculate_model' )
    self.evaluation1.text = name 
    self.bootstrab = params.bootstrap
    self.num_estimators = params.n_estimators
    self.maxdepth = params.max_depth
    self.maxfeatures = params.max_features
    self.out = results
    # self.evaluation1.text = results

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      files = ["train","test"]
      for i,name in enumerate(files):
        ff = self.file_loader_1.files[i]
        res = anvil.server.call('upload_excel_data', ff,ff.name)
        self.text_box_1.text = res
    else:
      self.text_box_1.text = "nooo"

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    m = self.out
    anvil.media.download(m)

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def modelwithparams_btn_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    bootstrab = True if self.bootstrab.text == 'True' else False
    results,eval = anvil.server.call('calculate_model_withparam',
                                     int(self.num_estimators.text),
                                     int(self.maxdepth.text), 
                                     self.maxfeatures.text, 
                                     bootstrab )
    self.eval_with_param.text = eval 
    



      





