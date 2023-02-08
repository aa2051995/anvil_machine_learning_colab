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
    res = anvil.server.call('check_files')
    if res == "no":
      self.evaluation1.text = "please upload the train data.xlsx and test data.xlsx files  " +res 
      return 
   
    if self.features_txt.text !='':
      features = self.features_txt.text.split(',')
    else:
       features = ''
    results,name,params = anvil.server.call('calculate_model',features)
    self.evaluation1.text = name 
    self.bootstrapPaparam.text = params['bootstrap']
    self.num_estimators.text = params['n_estimators']
    self.maxdepth.text = params['max_depth']
    self.maxfeatures.text = params['max_features']
    self.out = results
    self.params_txt.text = "(bootstrap="+str(params['bootstrap'])+", n_estimators="+ str(params['n_estimators'])+", max_depth="+str(params['max_depth'])+", max_features="+str(params['max_features'])+")"
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      # files = ["train","test"]
      for i,name in enumerate(self.file_loader_1.files):
        ff = self.file_loader_1.files[i]
        res = anvil.server.call('upload_excel_data', ff,ff.name)
      

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
    self.eval_with_param.text = ""
    if self.features_txt.text !='':
      features = self.features_txt.text.split(',')
    else:
      features = ''
    try:
      num_estimators = int(self.num_estimators.text)
      maxdepth = int(self.maxdepth.text)
      bootstrab = True if self.bootstrapPaparam.text == 'True' else False
      if self.maxfeatures.text in  ["auto", "log2", "sqrt"]:
        maxfeatures = self.maxfeatures.text
      else:
        self.eval_with_param.text = "enter parameter maxfeatures in the right format [auto, log2, sqrt]"
        return 
      self.eval_with_param.text = "calculate..."
      results,eval = anvil.server.call('calculate_model_withparam',features,
                                     num_estimators,
                                     maxdepth, 
                                     maxfeatures, 
                                     bootstrab )
      self.eval_with_param.text = eval 
      self.out = results
    except Exception as e:
      
      self.eval_with_param.text = str(e) #"enter the parameters in the right format" +e
      
      
    

  def download_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    m = self.out
    anvil.media.download(m)

    



      





