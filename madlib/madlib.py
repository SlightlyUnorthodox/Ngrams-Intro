# Project: Madlib Generator
# Created By: UF Computational Linguistics Club
# Team: ____
#

import Tkinter
import tkFont
import sentenceGenerator

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
    	
    	#number of sentences to generate (i.e. size of paragraph)
    	global size
    	size = 5

    	global it
    	it = 0

    	#Generate madlib
        self.madlibSetup(size)

        #Gui config
        self.customFont = tkFont.Font(family="arial", size=14)
        self.grid()
        
        #Upper Banner
        self.posVariable = Tkinter.StringVar()
        self.posVariable.set(u"Welcome to the Madlib Generator")
        welcomeBanner = Tkinter.Label(self,textvariable=self.posVariable,anchor="w",fg="black",bg="white",font = self.customFont)   
        welcomeBanner.grid(column=0,row=0,columnspan=2,sticky="EW")

        #Word entry field
        self.entryVariable = Tkinter.StringVar()
        self.entryVariable.set(u"press 'Enter' to begin.")
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable,font = self.customFont)
        self.entry.grid(column=0,row=1,sticky='EW')
        self.entry.bind("<Return>",lambda event: self.OnPressEnter(event, 0))

        #"Start New Madlib Button"
        button = Tkinter.Button(self,text=u"Start new madlib", command=self.OnButtonClick,font = self.customFont)
        button.grid(column=1,row=1)

        #Word entered field
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w",fg="black",bg="white",font = self.customFont)
        label.grid(column=0,row=2,columnspan=2,sticky="EW")

        self.grid_columnconfigure(0,weight=5)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
    	#Resets everything
        self.initialize()

    def OnPressEnter(self,event,it):

        if it < size: 
            #POS directions field
            if pos[it] == "adjective":
                self.posVariable.set("Enter an " + pos[it])
            else:
                self.posVariable.set("Enter a " + pos[it])

        if it > 0:
            #Replace word in madlib
            temp = sentences[it-1].split()
            temp[it-1] = self.entryVariable.get()
            sentences[it-1] = ' '.join(temp)

            #Value entered tag line
            if pos[it-1] == "adjective":
                self.labelVariable.set("You entered " + self.entryVariable.get() + " as an " + pos[it-1])
            else:
                self.labelVariable.set("You entered " + self.entryVariable.get() + " as a " + pos[it-1])

        #Clear text entry field
        self.entryVariable.set("")

        #Catch end condition
        if it == size:
            self.printResults(event,it)

        it += 1

        #Catch value entered
        self.entry.bind("<Return>",lambda event: self.OnPressEnter(event,it))

    def printResults(self,event,it):
        #Set fields to end values
        self.posVariable.set("Click the button to start a new Madlib")
        self.entryVariable.set("")

        root2 = Tkinter.Tk()
        root2.minsize(width=400, height=250)
        root2.maxsize(width=400, height=250)
        root2.title("Your Madlib")
        for i in range(0,size):
            Tkinter.Label(root2, text =sentences[replace[i]],borderwidth=1,font =tkFont.Font(family="arial", size=14)).grid(row=i,column=0)
        root2.mainloop
        

    def madlibSetup(self,size):
    	
    	#Text string for madlib sentences
    	global sentences #ex/
    	sentences = []

    	#Corresponding text string for sentence text
    	global sentencesPOS
    	sentencesPOS = []

    	#Index of word/pos to replace
        global replace
        replace = [] #ex/

        #Text part of speech of word to replace
        global pos
        pos = []
       
        for i in range(0,size):
        	#Run sentence generator
        	x = sentenceGenerator.generateSentence(1,size)
        	#Store sentences and sentencesPOS (as parts-of-speech)
        	sentences.append(x[0])
        	sentencesPOS.append(x[1])
        	#Identify word from each sentence to replace, store indices
        	replace.append(sentenceGenerator.wordReplacer(sentencesPOS[i]))
        	#Identify part-of-speech of each replacement word
        	pos.append(sentencesPOS[i].split()[replace[i]])

if __name__ == "__main__":
    madlib = madlibGUI(None)
    madlib.title('Madlib Demo')
    madlib.mainloop()
