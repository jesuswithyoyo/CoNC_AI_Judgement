from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
# from kivymd.uix.dialog  import MDDialog
# from kivymd.utils import asynckivy as ak
from kivymd.uix.card import MDCard
from kivymd.toast import toast

from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.boxlayout import MDAdaptiveWidget

#AI imports
from requests import get
from transformers import pipeline
import torch.nn.functional as F
import time
import sys


#USED TO CREATE THE SCREENS IN .KV FILE
class cunt_or_NOTcunt(ScreenManager):
    # pass
    
    text = StringProperty("")
    answer = StringProperty("")

    #USED TO PRINT THE MASTER INPUT TEXT TO A WIDGET  
    def clear_master_text_display(self, instance):
        self.masterINPUTtext.text = 'INPUT TEXT WILL DISPLAY'

    def masterINPUTtext(self, widget):
        self.text = widget.text


    #NERD STUFF HAPPENDS HERE
    def onClick(self):
        #toast("data has been sent for judgement. plase wait")
        
        self.masterINPUTtext(self.ids.master_input_text)
        print("This text is now being judged.  ",self.text)

        text = self.text
   
        #AI Send 
        model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
        classifier = pipeline('sentiment-analysis', model=model_name)

        #AI Results
        results = classifier([(text)])

        #RETURNED DICT
        for results in results:
            results=results

        #TAKE THE VALUE OUT OF THE DICT
        for value in results.values():
            value=value

        #GIVE THE VALUE A MAKE OVER
        perc = (value)

        #NAME LA AFTER THE POS OR NEG RETURNED IN THE DICT
        la = results.get('label')

        #READ THE VALUE OF LA= CUNT OR NOT CUNT
        if (la == 'POSITIVE'):
            print('{:,.2%}'.format(perc) + "  NOT CUNT")
            #print("NOT A CUNT") IN TERMINAL
            answer = ('NOT CUNT')
            print("the answer = "+ answer)
            toast("NOT CUNT")
        else:
            print('{:,.2%}'.format(perc) + "  IS CUNT")
            answer = ('IS CUNT')
            print("the answer = "+ answer)
            toast("IS CUNT")

#     id: cunt
#     print("")
#     print("")
#     print:" ██████╗██╗   ██╗███╗   ██╗████████╗")
#     print:"██╔════╝██║   ██║████╗  ██║╚══██╔══╝")
#     print:"██║     ██║   ██║██╔██╗ ██║   ██║   ")
#     print:"██║     ██║   ██║██║╚██╗██║   ██║   ")
#     print:"╚██████╗╚██████╔╝██║ ╚████║   ██║   ")
#     print:" ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ")
#     print("")
#     print("")
###############################
###### MAIN APP THING ########
class Main(MDApp):
    def build(self):
        Builder.load_file("ui.kv")
    
        Window.soft_input_mode = "below_target"
        self.title = "CoNC AI Judgment"

        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.primary_hue = "A700"

        self.theme_cls.accent_palette = "Yellow"
        self.theme_cls.accent_hue = "A700"

        self.theme_cls.theme_style = "Dark"

        return cunt_or_NOTcunt()

Main().run()

