#Griffin Georgiadis
#CS 21
#assignment 11
#Write a program that dispays a widow that calulate miles per gallon
import tkinter

class mpgConverterGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()
        # Create three frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        # Create the boxes for the miles entry and the gas entry
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text='Enter a distance in miles:')
        self.miles_entry = tkinter.Entry(self.top_frame, \
                                        width=10)

        self.prompt = tkinter.Label(self.top_frame, \
                                          text='Enter gallons of gas:')
        self.gas_entry = tkinter.Entry(self.top_frame, \
                                        width=10)



       # set widgets place
        self.prompt_label.pack(side='left')
        self.miles_entry.pack(side='left')


        self.prompt.pack(side='left')
        self.gas_entry.pack(side='left')
        

        # Create lable to display mgp
        self.descr_label = tkinter.Label(self.mid_frame, \
                                         text='Converted to miles per gallon:')

        # set StringVar 
        self.value = tkinter.StringVar()

        # Create a label with stringvar
        self.miles_label = tkinter.Label(self.mid_frame, \
                                         textvariable=self.value)
        # Pack the middle frame's widgets.
        self.descr_label.pack(side='left')
        self.miles_label.pack(side='left')
        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, \
                                          text='Convert', \
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        # set buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

    
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        # enter loop
        tkinter.mainloop()

        
    def convert(self):
#calculat mpg
        try:
            miles = float(self.miles_entry.get())
            gas = float(self.gas_entry.get())
           
            mpg = miles / gas
            
            f_miles = format(mpg,'.1f') + " miles"
        except:
            f_miles = "invalid"
    
        self.value.set(f_miles)



mpg_conv = mpgConverterGUI()

