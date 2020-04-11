import tkinter as tk
from tkinter import *
from functools import partial
from matplotlib import style
import matplotlib
matplotlib.use('TkAgg')
style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
class tablegraph(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.c=container
        self.frames={}
        for F in (startpage, pageone):    
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky='nsew')
            
        self.show_frame(startpage)
        tk.Tk.wm_title(self, 'Solar Power Generation Predictor (SPGP)')
    def ter(self):
        print("tej")
        frame=pagetwo(self.c, self)
        self.frames[pagetwo]=frame
        frame.grid(row=0, column=0, sticky='nsew')
        frame=self.frames[pagetwo]
        frame.tkraise()
    def terr(self):
        frame=graph(self.c, self)
        self.frames[graph]=frame
        frame.grid(row=0, column=0, sticky='nsew')
        frame=self.frames[graph]
        frame.tkraise()       

    def show_frame(self, cont):
        frame=self.frames[cont]
        frame.tkraise()
    def quit_frame(self, cont):
        frame=self.frames[cont]
        frame.destroy()
        frame.quit()

class startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
                # Create a Tkinter variable
        # Create a Tkinter variable
        root=self
        tkvar = StringVar(root)
        # List with options of months
        choices = ['February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        popupMenu = OptionMenu(root, tkvar, *choices)
        Label(root, text="Choose Month", font=("Arial Bold", 20), fg='Red').grid(row = 1, column = 1)
        popupMenu.grid(row = 2, column =1)
        tkvar.set('January') # set the default option

        #Bad weather and Good weather6
        tkvar1 = StringVar(self)
        choices1 = ['Good weather']
        pop1 = OptionMenu(root, tkvar1, *choices1)
        Label(root, text="Choose weather condition", font=("Arial Bold", 20), fg='maroon2').grid(row=1, column=2)
        pop1.grid(row = 2, column = 2)
        tkvar1.set("Bad weather") #set the default option
        
        #calling a new window based on the month and the weather type!!
        def type(tkvar, tkvar1):
            global m
            global c
            m=tkvar.get()
            c=tkvar1.get()
            choices = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']
            choices1=['October', 'November', 'December']
            for month in choices:
                if(m==month):
                    print(m, c)
                    controller.show_frame(pageone)
                    
                    break
                elif(m==choices1[0]):
                    print(m, c)
                    controller.show_frame(pagetwo)
                    
                    break
                elif(m==choices1[1]):
                    print(m, c)
                    controller.show_frame(pagetwo)
                    
                    break
                elif(m==choices1[2]):
                    print(m, c)
                    controller.show_frame(pagetwo)
                    
                    break
        #giving two parameters
        type=partial(type, tkvar, tkvar1)
        #closing the main loop
        
        def closewin():
            self.destroy()
            #controller.quit_frame(startpage)
            controller.quit_frame(pageone)
            controller.quit_frame(pagetwo)
            
        Button(self, text='QUIT', command=closewin, font=('Arial BOld', 15)).grid(row=4, column=5)

        #Button for the window.
        Button(self, text="Open Portal", command=type, font=("Arial Bold", 20), fg='black', bg="white" ).grid(row=3, column=3)

class pageone(tk.Frame):
    

        
    def __init__(self, parent, controller):
        from tkinter import filedialog
        from tkinter import Label
    #label module for the labeling of the buttons and the printing the names.
        from tkinter import Canvas
        #canvas hepls us to algin window and the assign.
        import pandas as pd
        #pandas to export the data sets and create the tables of the data sets.
        import tkinter
        from tkinter import filedialog
        #filedialog box opens, for the file to export from the requried folder location in the computer.
        import numpy as np
        #NumPy is a general-purpose array-processing package.
        import matplotlib.pyplot as plt
        #matplotlib is a 2D plotting library, used in ipython and jupyter shells.
        import seaborn as sns
        #seaborn is a statistical visualization of the data and use in ipython and jupyter shells.
        from pandas import DataFrame
        #DataFrame module helps in constructing new tables and working out the classifications.
        from pandastable import Table
        #Table module used for the new window to display the table, which is formed by DataFrames.
        from tkinter import ttk
        tk.Frame.__init__(self, parent)
        #labels assinged for the values to be clicked after the labels assigned
        window=self
    
        def getExcel ():
        #defining a function named "getExcel"
        #this function takes the data set file
            
            global weth
            #making the weth variables a global variable so that easy access of the variable allowed
            
            import_file_path = filedialog.askopenfilename()
            #importing file using filedialog box
            
            weth = pd.read_excel (import_file_path)
            #weth variable assigned with the excel data that is given in the file dialogue box

            btn1.configure(text="FILE IMPORTED", fg='green')
            #btn1 is the button name that is configured after clicking on the button
            
        def getExcel2 ():
        #defining a function named "getExcel2
        #this fuction takes the testing data set file
            global test
            #making a global variable test
            
            import_file_path = filedialog.askopenfilename()
            #importing a file using file dialogue box
            
            test = pd.read_excel (import_file_path)
            #reading the file using pandas and excel
            #the global variable is assinged a value of the data sets
            
            btn7.configure(text="FILE IMPORTED")
            #btn7 is the button configured after clicking the btn7, changes to the "File IMPORTED"
            
        def getExcel3 ():
        #defining a function name getExcel3
        #this file takes the result data set
            
            global test1
            #assigning the globla variable test1 
            
            import_file_path = filedialog.askopenfilename()
            #importing using a file dialogue box
            
            test1 = pd.read_excel (import_file_path)
            #the test1 variable is assinged to a excel file and to read it.
            
            btn10.configure(text="FILE IMPORTED")
            #the btn10 label changes to "FILE IMPORTED"

        def Algo ():
            #constructor with parent parameter
            from sklearn.pipeline import Pipeline as pipe
            import pandas as pd
            data=weth
            data.columns
            l=data['Solar_irradiation']
            m=data['solar_power_gen']
            k=[]
            global i
            global j
            i=0
            for i in range(len(l)):
                if(l[i]==0):
                    k.append(0)
                else:
                    k.append((m[i]/l[i]))
            data.insert(2, "factor", k) 
            print(data.columns)
            x=test
            x_train=data[['declination_angle', 'Longitude', 'Latitude', 'Sunrise', 'Sunset',
                           'sin_solar_zenth', 'Solar_altitude', 'Solar_constant',
                           'Solar_irradiation_atm','Cloudiness', 'Temperature',
                           'Humidity', 'Wind_speed']]
            y_train=data['factor']
            x_test=x[['declination_angle', 'Longitude', 'Latitude', 'Sunrise', 'Sunset',
                           'sin_solar_zenth', 'Solar_altitude', 'Solar_constant',
                           'Solar_irradiation_atm', 'Cloudiness', 'Temperature',
                           'Humidity', 'Wind_speed']]
            y_test=x['Solar_irradiation']
            y_test2=x['solar_power_gen']
            l=y_test
            m=y_test2
            k=[]
            i=0
            for i in range(len(l)):
                if(l[i]==0):
                    k.append(0)
                else:
                   k.append((m[i]/l[i]))
            from sklearn.ensemble import RandomForestRegressor as RF
            from sklearn.preprocessing import PolynomialFeatures as PF, FunctionTransformer as FT
            rf1=pipe([('poly', PF()), ('rf', RF())])
            rf1.fit(x_train, y_train)
            prd_fac=rf1.predict(x_test)
            
                    #Solar power algorithm
            X=data[['id','declination_angle', 'Longitude', 'Latitude', 'Sunrise', 'Sunset','sin_solar_zenth', 'Solar_altitude', 'Solar_constant',
                       'Solar_irradiation_atm', 'Cloudiness', 'Temperature'
                           ,'Humidity', 'Wind_speed']]
            Y=data['Solar_irradiation']
            x=test
            x_test=x[['id','declination_angle', 'Longitude', 'Latitude', 'Sunrise', 'Sunset',
                           'sin_solar_zenth', 'Solar_altitude', 'Solar_constant',
                           'Solar_irradiation_atm', 'Cloudiness', 'Temperature',
                           'Humidity', 'Wind_speed']]
            y_test=x['Solar_irradiation']
            y_test2=x['solar_power_gen']
            from sklearn.metrics import r2_score
            from sklearn.ensemble import GradientBoostingRegressor
            rf2=RF(n_estimators =20,min_samples_split=24,min_samples_leaf=24)
            rf3=pipe([('poly', PF()), ('rf', rf2)])
            rf3.fit(X, Y)
            prediction1=rf3.predict(x_test)
            prediction=prd_fac*prediction1
            plt.figure(figsize=(20,12))
            plt.scatter(y_test, prediction)
            pre=[]
            act=[]
            i=0
            import tkinter as tk
            for i in range(len(prediction)):
                if(prediction[i]>0):
                    pre.append(prediction[i])
                    act.append(y_test2[i])
            prediction=list(prediction)
            global i1
            global j1
            i1=prediction.index(pre[0])
            j1=prediction.index(pre[-1])
            s=str("The solar power Generation occurs From "+str(i1+1)+":00 AM to "+str(j1+1-12)+":00 PM Hours (i.e. Power Generated for "+str(j1-i1)+" Hours) ")
            lb112=tk.Label(self, text=s)
            lb112.grid(row=7, column=1, columnspan=4)
                        #any negative prediction is turned into 0 value
            from sklearn import metrics
            from pandastable import Table, TableModel
           
            mean_sq_er = metrics.mean_squared_error(y_test2, prediction)
            root_mean_sq = np.sqrt(mean_sq_er)
            global df1
            df1 = pd.DataFrame({'Actual': act, 'Predicted': pre})
            print(df1)
            from pandastable import Table, TableModel
            f = Frame(self)
            f.grid(row=8, column=1, columnspan=4)
            self.table = pt = Table(f, dataframe=df1,
            showtoolbar=True, showstatusbar=True)
            pt.show()
            from sklearn.metrics import r2_score
            t=(100*round(r2_score(df1['Actual'], df1['Predicted']), 2))
            global txt
            txt=('The Accuracy of the Data is: '+str(t)+'% Note: we considered the regression score as the accuracy of the data')
            label=tk.Label(self, text=txt)
            label.grid(row=6, column=1, columnspan=4)
            return

        def Opt():
            btn10=Button(window, text="IMPORT result DATA",fg="red", command=getExcel3, font=('Arial Italic', 18), height = 1, width = 20)
            btn10.grid(row=4, column=2)
            
            btn21 =tk.Button(self, text="Disp-Table",fg="maroon2", command= controller.ter, font=('Arial Italic', 18), height=1, width=20)
        
            btn21.grid(row=4, column=1)
            btn22 =tk.Button(self, text="Disp-Graph",fg="maroon2", command= controller.terr, font=('Arial Italic', 18), height=1, width=20)
            
            btn22.grid(row=5, column=1)


        def closewin1():
            self.destroy()
        btn1=Button(window, text="IMPORT TRAINING DATA",fg="red", command=getExcel, font=("Arial Italic", 18), height = 1, width = 20)
        btn1.grid(row=2, column=1)
        #this returns the filedialogue box to choose the requiered file
        #used for only importing the data file
        #importing the training data

        

        btn7=Button(window, text="IMPORT TESTING DATA",fg="red", command=getExcel2, font=('Arial Italic', 18), height = 1, width = 20)
        btn7.grid(row=2, column=2)
        ##this returns the filedialogue box to choose the requiered file
        #used for only importing the data file
        #importing testing data

        ##this returns the filedialogue box to choose the requiered file
        #used for only importing the data file
        #importing resulting data

        btn8=Button(window, text='PREDICT SOLAR POWER', command=Algo, font=('Arial Italic', 18), fg='maroon2', height = 1, width = 20)
        btn8.grid(row=3, column=1)
        #defining the function with name nightt
        #this function gives "PREDICT the SOLAR POWER GENERATED" for the whole day

        btn5=Button(window, text='QUIT', command=closewin1, font=('Arial BOld', 15), height=1, width=15)
        btn5.grid(row=5, column=2)
        #button for closing the window
        
        btn6=Button(window, text='More-Options', command=Opt, font=('Arial BOld', 15), height=1, width=15)
        btn6.grid(row=3, column=2)

        btn2 =tk.Button(self, text="Back", command=lambda: controller.show_frame(startpage))
        
        btn2.grid(row=1, column=0)


class pagetwo(tk.Frame):
    
    def __init__(self, parent, controller):
        from tkinter import ttk
        tk.Frame.__init__(self, parent)
        s=str("Month: "+m+" and Weather Condition: "+c+".")
        from pandastable import Table, TableModel
        lbl=tk.Label(self, text=s, font=("Arial Bold", 18))
        lbl.grid(row=0, column=1)
        f = Frame(self)
        f.grid(row=2, column=0, columnspan=3)
        df = TableModel.getSampleData()
        print(type(df))
        self.table = pt = Table(f, dataframe=df1,
        showtoolbar=True, showstatusbar=True)
        pt.show()
        btn122=tk.Button(self, text="Back", command=lambda : controller.show_frame(pageone))
        btn122.grid(row=0, column=0)
        btn122=tk.Button(self, text='Go to Home', command=lambda : controller.show_frame(startpage))
        btn122.grid(row=3, column=1)
       
        label=tk.Label(self, text=txt)
        label.grid(row=1, column=0, columnspan=4)
        
        

        

class graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        f=Figure(figsize=(5, 5), dpi=100)
        a=f.add_subplot(111)
        x=range(len(df1['Actual']))
        t0, =a.plot(x, df1['Actual'], color="red", marker="o", linestyle="-")
        t1, =a.plot(x, df1['Predicted'], color="blue", marker="x", linestyle="-")
       
        a.set_ylabel('Solar power Generated in KW/H')
        a.set_xlabel('Hours')
        a.grid()
        f.legend((t0, t1), ('Actual', 'Predicted'), 'upper right')
        canvas=FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar=NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()
        
        label=tk.Label(self, text=txt)
        label.pack()
        btn=tk.Button(self, text="Back", command=lambda : controller.show_frame(pageone))
        btn.pack()
        btn1=tk.Button(self, text='Go to Home', command=lambda : controller.show_frame(startpage))
        btn1.pack()
        
app=tablegraph()
app.mainloop()
