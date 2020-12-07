import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
import numpy as np
import svgwrite
import math
from svgwrite import cm, mm   

focuserDiameterMm = 64.67





class FocuserProtract():
    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Focuser Protractor Creator")

        self.ANGLES=[]
        self.SIZES=[]
        self.OPTIONS=[]

        for x in range(1, 361):
            self.ANGLES.append(x)

        for i in np.arange(0.0, 20, 0.1):
            self.SIZES.append("{:.1f}".format(i))       

        self.frm_configuration = tk.Frame(master=self.window)
        self.frm_configuration.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        self.frm_diameter = tk.Frame(master=self.frm_configuration)
        self.frm_diameter.grid(row=0, column=0, sticky="nw")

        self.frm_angle = tk.Frame(master=self.frm_configuration)
        self.frm_angle.grid(row=1, column=0, sticky="nw", pady=1)

        self.frm_angleHighlight = tk.Frame(master=self.frm_configuration)
        self.frm_angleHighlight.grid(row=2, column=0, sticky="nw", pady=1)

        self.frm_graduationSize = tk.Frame(master=self.frm_configuration)
        self.frm_graduationSize.grid(row=3, column=0, sticky="nw", pady=1)

        self.frm_graduationSelect = tk.Frame(master=self.frm_configuration)
        self.frm_graduationSelect.grid(row=4, column=0, sticky="nw", pady=1)

        self.frm_fontSelect = tk.Frame(master=self.frm_configuration)
        self.frm_fontSelect.grid(row=5, column=0, sticky="nw", pady=1)

        self.frm_saveButton = tk.Frame(master=self.frm_configuration)
        self.frm_saveButton.grid(row=6, column=0, sticky="nw", padx=80, pady=5)

        self.lbl_diameter = tk.Label(master=self.frm_diameter, text="Focuser Diameter:")
        self.lbl_diameter.grid(row=0, column=0, sticky="nw")

        self.lbl_angle = tk.Label(master=self.frm_angle, text="Degrees")
        self.lbl_angle.grid(row=0, column=0, sticky="nw")

        self.lbl_split = tk.Label(master=self.frm_angle, text="Split Protractor:")
        self.lbl_split.grid(row=0, column=2, sticky="nw", padx=(5,0))

        self.lbl_split = tk.Label(master=self.frm_angleHighlight, text="Highlighted Angle:")
        self.lbl_split.grid(row=0, column=0, sticky="nw")

        self.ent_diameter = tk.Entry(master=self.frm_diameter, width=10)
        self.ent_diameter.grid(row=0, column=1, sticky="nw")

        self.lbl_diameterMm = tk.Label(master=self.frm_diameter, text="mm")
        self.lbl_diameterMm.grid(row=0, column=2, sticky="nw")

        self.lbl_graduationSize = tk.Label(master=self.frm_graduationSize, text="Size of Graduations in mm")
        self.lbl_graduationSize.grid(row=0, column=0, sticky="nw", pady=(5,0))

        self.lbl_graduationRegular = tk.Label(master=self.frm_graduationSelect, text="Regular:")
        self.lbl_graduationRegular.grid(row=0, column=0, sticky="nw")

        self.lbl_graduationHighlight = tk.Label(master=self.frm_graduationSelect, text="Highlighted:")
        self.lbl_graduationHighlight.grid(row=0, column=2, sticky="nw")

        self.lbl_fontSize = tk.Label(master=self.frm_fontSelect, text="Font Size:")
        self.lbl_fontSize.grid(row=0, column=0, sticky="nw")

        self.lbl_fontSize = tk.Label(master=self.frm_fontSelect, text="Invert Scale:")
        self.lbl_fontSize.grid(row=0, column=2, sticky="nw", padx=(5,0))

        self.angleVariable = tk.StringVar(self.window)
        self.angleVariable.set(180) # default value
        self.opt_angle = ttk.Combobox(self.frm_angle, textvariable=self.angleVariable, values=self.ANGLES, width=4)
        self.opt_angle.grid(row=0, column=1, sticky="nw")

        self.splitVariable = tk.StringVar(self.window)
        self.splitVariable.set('Yes') # default value
        self.opt_split = ttk.Combobox(self.frm_angle, textvariable=self.splitVariable, values=['Yes', 'No'], width=3)
        self.opt_split.grid(row=0, column=3, sticky="nw")

        self.highlightVariable = tk.StringVar(self.window)
        self.highlightVariable.set(5) # default value
        self.opt_highlight = ttk.Combobox(self.frm_angleHighlight, textvariable=self.highlightVariable, values=self.ANGLES, width=3)
        self.opt_highlight.grid(row=0, column=1, sticky="nw")

        self.regularSizeVariable = tk.StringVar(self.window)
        self.regularSizeVariable.set(5.0) # default value
        self.opt_regularSize = ttk.Combobox(self.frm_graduationSelect, textvariable=self.regularSizeVariable, values=self.SIZES, width=4)
        self.opt_regularSize.grid(row=0, column=1, sticky="nw")

        self.highlightSizeVariable = tk.StringVar(self.window)
        self.highlightSizeVariable.set(10.0) # default value
        self.opt_highlightSize = ttk.Combobox(self.frm_graduationSelect, textvariable=self.highlightSizeVariable, values=self.SIZES, width=4)
        self.opt_highlightSize.grid(row=0, column=3, sticky="nw")

        self.fontSizeVariable = tk.StringVar(self.window)
        self.fontSizeVariable.set(4.0) # default value
        self.opt_fontSize = ttk.Combobox(self.frm_fontSelect, textvariable=self.fontSizeVariable, values=self.SIZES, width=4)
        self.opt_fontSize.grid(row=0, column=1, sticky="nw")

        self.invertVariable = tk.StringVar(self.window)
        self.invertVariable.set('No') # default value
        self.opt_invert = ttk.Combobox(self.frm_fontSelect, textvariable=self.invertVariable, values=['Yes','No'], width=3)
        self.opt_invert.grid(row=0, column=3, sticky="nw")

        self.btn_save = tk.Button(self.frm_saveButton, text="Save As...", command=self.save_file)
        self.btn_save.grid(row=0, column=0, sticky="nw")

        self.window.grid_rowconfigure([0,1], weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.window.mainloop()

    def save_file(self):
        filepath = asksaveasfilename(
            defaultextension="svg",
            filetypes=[("Vector Image", "*.svg"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            self.configureSvg()
            self.createSvg()
            text = self.dwg.tostring()
            output_file.write(text)
        self.window.title(f"Focuser Protractor Creator - {filepath}")

    def createSvg(self):
        self.yCoor= 20.0
        self.loop = 0
        self.mmPerDegree= ((float(self.OPTIONS[0])*math.pi)/360)
        self.degreesToDraw = int(self.OPTIONS[1])
        self.degreesToHighlight = int(self.OPTIONS[3])
        self.regularLength = float(self.OPTIONS[4])
        self.highlightLength = float(self.OPTIONS[5])
        self.fontsize = float(self.OPTIONS[6])

        if(self.OPTIONS[7] == 'Yes'):
            self.shouldFlip = -1
            self.fontOffset = ((self.fontsize/2)/2.835)-0.5
        else:
            self.shouldFlip = 1
            self.fontOffset = ((self.fontsize/2)/2.835)+0.5

        self.documentSize = (int((self.yCoor*2)+(self.degreesToDraw*self.mmPerDegree))*mm, 
            int((self.yCoor*2)+self.highlightLength+(self.fontsize/2.835))*mm)

        self.dwg = svgwrite.Drawing(filename='focuser_guide.svg', size=self.documentSize, debug=True)
        self.vlines = self.dwg.add(self.dwg.g(id='vline', stroke='black', stroke_width=0.5))
        self.g = self.dwg.g(style="font-size:%s;font-family:sans-serif;stroke:black;stroke-width:0;fill:black;text-anchor:middle" 
            % (str(self.fontsize)))
        
        while self.loop <= self.degreesToDraw:
            self.xCoor = self.yCoor + self.loop*self.mmPerDegree
            self.textRotate = 'scale(%s)' % (self.shouldFlip)
            if (self.loop%self.degreesToHighlight):
                self.vlines.add(self.dwg.line(start=(self.xCoor*mm,self.yCoor*mm), 
                    end=(self.xCoor*mm, (self.yCoor+self.regularLength)*mm)))
            else:
                self.vlines.add(self.dwg.line(start=(self.xCoor*mm,self.yCoor*mm), 
                    end=(self.xCoor*mm, (self.yCoor+self.highlightLength)*mm)))
                
                if(self.OPTIONS[2]== 'Yes'):
                    if(self.loop<=self.degreesToDraw/2):
                        self.g.add(self.dwg.text(int(self.degreesToDraw/2-self.loop), insert = ((self.shouldFlip*self.xCoor)*mm, 
                            self.shouldFlip*(self.highlightLength+self.yCoor+self.fontOffset)*mm), transform=self.textRotate))
                    else:
                        self.g.add(self.dwg.text(int(self.loop-self.degreesToDraw/2), insert = ((self.shouldFlip*self.xCoor)*mm, 
                            self.shouldFlip*(self.highlightLength+self.yCoor+self.fontOffset)*mm), transform=self.textRotate))
                else:
                    self.g.add(self.dwg.text(self.loop, insert = ((self.shouldFlip*self.xCoor)*mm, 
                            self.shouldFlip*(self.highlightLength+self.yCoor+self.fontOffset)*mm), transform=self.textRotate))

            self.loop += 1
        
        self.dwg.add(self.g)
        self.OPTIONS.clear()

    def configureSvg(self):
        self.OPTIONS.append(self.ent_diameter.get())
        self.OPTIONS.append(self.opt_angle.get())
        self.OPTIONS.append(self.opt_split.get())
        self.OPTIONS.append(self.opt_highlight.get())
        self.OPTIONS.append(self.opt_regularSize.get())
        self.OPTIONS.append(self.opt_highlightSize.get())
        self.OPTIONS.append(self.opt_fontSize.get())
        self.OPTIONS.append(self.opt_invert.get())

if __name__ == '__main__':
    app = FocuserProtract()