#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import tkFont
import numpy
#import sentenceGenerator

#Madlib GUI class
class madlibGUI(Tkinter.Tk):
    
    #Gui definition
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent

        self.initialize()
        
        #Set size bounds
        self.minsize(width=500, height=500)
        self.maxsize(width=500, height=500)
        
    #Gui initialization
    def initialize(self):

    	#Generate madlib
        self.madlibSetup()

        #Gui config
        self.customFont = tkFont.Font(family="arial", size=14)
        self.grid()
        
        #POS directions field
        self.posVariable = Tkinter.StringVar()
        self.posVariable.set("Enter a " + pos)
        posDirect = Tkinter.Label(self,textvariable=self.posVariable,anchor="w",fg="white",bg="black",font = self.customFont)
        posDirect.grid(column=0,row=0,columnspan=2,sticky='EW')

        #Word entry field
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable,font = self.customFont)
        self.entry.grid(column=0,row=1,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)

		#On start: standing text        
        self.entryVariable.set(u"Enter your first " + pos + " here.")

        #"Start New Madlib Button"
        button = Tkinter.Button(self,text=u"Start new madlib", command=self.OnButtonClick,font = self.customFont)
        button.grid(column=1,row=1)

        #Word entered field
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w",fg="white",bg="blue",font = self.customFont)
        label.grid(column=0,row=2,columnspan=2,sticky='EW')
        #self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0,weight=5)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.initialize()
        #self.labelVariable.set( self.entryVariable.get())
        #self.entry.focus_set()
        #self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
    	#Add word function here

        self.labelVariable.set("You entered " + self.entryVariable.get() + " as a " + pos)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        #Check end condition (after n sentences)

    def madlibSetup(self):
    	global sentences #ex/
    	sentences = []
    	global sentencesPOS
    	sentencesPOS = [] 
        global replace #ex/
        replace = []
        global pos
        pos = "noun"
        for i in range(1,10):
        	#test cases
        	sentences.append("Sentence" + str(i) + " is a demo sentence")
        	sentencesPOS.append("noun verb article adjective noun")
        	replace.append(3)
        #	sentences[i] = madlib.generateSentence()
        #	replace[i] = madlib.wordReplacer()
        #pos = replace[0]

if __name__ == "__main__":
    madlib = madlibGUI(None)
    madlib.title('Madlib Demo')
    madlib.mainloop()
