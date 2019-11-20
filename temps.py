#Griffin Georgiadis
#CS 21
#assignment 11
#Write a program that dispays a widow that calulate miles per gallon
import tkinter

class tempConverterGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()
        # Create three frames for different parts of window
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        # Create the boxes for the temp entry
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text='Enter Celcius temperature:')
        self.temp_entry = tkinter.Entry(self.top_frame, \
                                        width=10)




       # set widgets place
        self.prompt_label.pack(side='left')
        self.temp_entry.pack(side='left')


        

        # Create lable to display temp in fahrenheit
        self.descr_label = tkinter.Label(self.mid_frame, \
                                         text='Converted celsius to fahrenheit:')

        # set StringVar 
        self.value = tkinter.StringVar()

        # Create a label with stringvar
        self.miles_label = tkinter.Label(self.mid_frame, \
                                         textvariable=self.value)
        # Pack the middle frame's widgets.
        self.descr_label.pack(side='top')
        self.miles_label.pack(side='top')
        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, \
                                          text='Convert', \
                                          command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', \
                                          command=self.main_window.destroy)
        # set buttons
        self.calc_button.pack(side='right')
        self.quit_button.pack(side='right')

    
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        # enter loop
        tkinter.mainloop()

        
    def convert(self):
#calculat mpg
        try:
            cel = float(self.temp_entry.get())
     
           
            total_temp = cel * (9/5)+ 32
            
            total = format(total_temp,'.1f') + " miles"
        except:
            total = "invalid"
    
        self.value.set(total)



temp_conv = tempConverterGUI()
