from tkinter import *
import numpy
import pandas
import sympy
from tkinter.messagebox import showerror
import os  # used to open files in default programs

# creating GUI main window called root
root = Tk()
root.title("Combustion of Gaseous Fuels")

# Adding author details
author_details = Text(root, height=4, width=60)
separator_frame_1 = Frame(root, height=10)
separator_frame_1.grid(row=8, column=1)
author_details.grid(row=9, column=3, sticky=W, columnspan=3)
separator_frame_2 = Frame(root, height=10)
separator_frame_2.grid(row=10, column=1)
author_details.insert(END,"   Authors: Dishant Beniwal, Jhalak    ")
upes_logo = PhotoImage(file="upes_logo.png")
author_details.image_create(END, image=upes_logo)
author_details.config(state=DISABLED)

# creating fuel component table with option menu and entry widgets
fuel_frame = Frame(root)  # creating the frame in main window 'root' to hold fuel input data

fuel_heading_1 = Label(fuel_frame, text="Fuel Component")  # Heading in fuel frame
fuel_heading_2 = Label(fuel_frame, text="Ratio(mol%)")

# creating list with fuel components that will be available to user to choose from
fuel_list = ["Methane", "Carbon Monoxide", "Hydrogen", "Ethane", "Ethylene", "Propane",
             "Butane", "Acetylene", "Hydrogen Sulphide", "Carbon Dioxide", "Nitrogen", "Oxygen"]

# creating option menu with drop down list
f_option_1 = StringVar()
f_option_1.set(fuel_list[0])  # setting default value of 1st option menu to "Methane"
f_menu_1 = OptionMenu(fuel_frame, f_option_1, *fuel_list)  # creating a drop down menu for option 1 with fuel list
f_option_2 = StringVar()
f_menu_2 = OptionMenu(fuel_frame, f_option_2, *fuel_list)
f_option_3 = StringVar()
f_menu_3 = OptionMenu(fuel_frame, f_option_3, *fuel_list)
f_option_4 = StringVar()
f_menu_4 = OptionMenu(fuel_frame, f_option_4, *fuel_list)
f_option_5 = StringVar()
f_menu_5 = OptionMenu(fuel_frame, f_option_5, *fuel_list)
f_option_6 = StringVar()
f_menu_6 = OptionMenu(fuel_frame, f_option_6, *fuel_list)
f_option_7 = StringVar()
f_menu_7 = OptionMenu(fuel_frame, f_option_7, *fuel_list)
f_option_8 = StringVar()
f_menu_8 = OptionMenu(fuel_frame, f_option_8, *fuel_list)

# creating entry widgets to take user input
f_entry_1 = Entry(fuel_frame, width=6)  # Creating entry widget for taking user input
f_entry_1.insert(END, "100.00")  # setting default value of 1st fuel entry as 100%
f_entry_2 = Entry(fuel_frame, width=6)
f_entry_2.insert(END, "0.00")
f_entry_3 = Entry(fuel_frame, width=6)
f_entry_3.insert(END, "0.00")
f_entry_4 = Entry(fuel_frame, width=6)
f_entry_4.insert(END, "0.00")
f_entry_5 = Entry(fuel_frame, width=6)
f_entry_5.insert(END, "0.00")
f_entry_6 = Entry(fuel_frame, width=6)
f_entry_6.insert(END, "0.00")
f_entry_7 = Entry(fuel_frame, width=6)
f_entry_7.insert(END, "0.00")
f_entry_8 = Entry(fuel_frame, width=6)
f_entry_8.insert(END, "0.00")

# assigning position to all the widgets
fuel_heading_1.grid(padx=2, pady=2)  # assigning position to fuel heading 1
fuel_heading_2.grid(row=0, column=1, padx=2, pady=2)
f_menu_1.grid(row=1, column=0, sticky=E)
f_entry_1.grid(row=1, column=1)
f_menu_2.grid(row=2, column=0, sticky=E)
f_entry_2.grid(row=2, column=1)
f_menu_3.grid(row=3, column=0, sticky=E)
f_entry_3.grid(row=3, column=1)
f_menu_4.grid(row=4, column=0, sticky=E)
f_entry_4.grid(row=4, column=1)
f_menu_5.grid(row=5, column=0, sticky=E)
f_entry_5.grid(row=5, column=1)
f_menu_6.grid(row=6, column=0, sticky=E)
f_entry_6.grid(row=6, column=1)
f_menu_7.grid(row=7, column=0, sticky=E)
f_entry_7.grid(row=7, column=1)
f_menu_8.grid(row=8, column=0, sticky=E)
f_entry_8.grid(row=8, column=1)

# creating air component table
air_frame = Frame(root)  # creating a frame for air in main window 'root'

air_heading_1 = Label(air_frame, text="Air Component")  # creating heading for air frame
air_heading_2 = Label(air_frame, text="Ratio(mol%)")

# creating list with air components that will be available to user to choose from
air_list = ["Nitrogen", "Oxygen", "Carbon Dioxide", "Moisture(H2O)", "Argon"]

# creating option menu with drop down list
a_option_1 = StringVar()  # creating option 1
a_option_1.set(air_list[0])  # setting default value of option 1 to 1st element of air list
a_menu_1 = OptionMenu(air_frame, a_option_1, *air_list)  # creating a drop down menu for option 1
a_option_2 = StringVar()
a_option_2.set(air_list[1])
a_menu_2 = OptionMenu(air_frame, a_option_2, *air_list)
a_option_3 = StringVar()
a_menu_3 = OptionMenu(air_frame, a_option_3, *air_list)
a_option_4 = StringVar()
a_menu_4 = OptionMenu(air_frame, a_option_4, *air_list)
a_option_5 = StringVar()
a_menu_5 = OptionMenu(air_frame, a_option_5, *air_list)

# creating entry widgets to take user input
a_entry_1 = Entry(air_frame, width=6)  # creating entry 1
a_entry_1.insert(END, "79.00")  # setting default value of entry 1 to 79.00
a_entry_2 = Entry(air_frame, width=6)
a_entry_2.insert(END, "21.00")
a_entry_3 = Entry(air_frame, width=6)
a_entry_3.insert(END, "0.00")
a_entry_4 = Entry(air_frame, width=6)
a_entry_4.insert(END, "0.00")
a_entry_5 = Entry(air_frame, width=6)
a_entry_5.insert(END, "0.00")

# arranging all the widgets in air frame
air_heading_1.grid(padx=2, pady=2)
air_heading_2.grid(row=0, column=1, padx=2, pady=2)
a_menu_1.grid(row=1, column=0, sticky=E)
a_entry_1.grid(row=1, column=1)
a_menu_2.grid(row=2, column=0, sticky=E)
a_entry_2.grid(row=2, column=1)
a_menu_3.grid(row=3, column=0, sticky=E)
a_entry_3.grid(row=3, column=1)
a_menu_4.grid(row=4, column=0, sticky=E)
a_entry_4.grid(row=4, column=1)
a_menu_5.grid(row=5, column=0, sticky=E)
a_entry_5.grid(row=5, column=1)

# creating a frame for user to input flow properties
flow_frame = Frame(root)  # creating a frame for flow properties in main window 'root'

fl_heading_1 = Label(flow_frame, text="Flow Property")  # creating heading in flow frame
fl_heading_2 = Label(flow_frame, text="Value")
fl_heading_3 = Label(flow_frame, text="Units")

# creating flow frame widgets
f_flow_label = Label(flow_frame, text="Fuel Flow Rate")  # creating label for fuel flow rate
f_flow_entry = Entry(flow_frame, width=6)  # creating entry widget to take user input for fuel flow rate
f_flow_unit = Label(flow_frame, text="m3/min")  # creating label to denote the unit of fuel flow rate
f_flow_entry.insert(END, "8.00")  # setting default value of fuel flow rate to 8.00

eq_ratio_label = Label(flow_frame, text="Equivalence Ratio")
eq_ratio_entry = Entry(flow_frame, width=6)
eq_ratio_entry.insert(END, "1.00")

f_temp_label = Label(flow_frame, text="Fuel Temp.")
f_temp_entry = Entry(flow_frame, width=6)
f_temp_unit = Label(flow_frame, text="deg C")
f_temp_entry.insert(END, "25.0")

a_temp_label = Label(flow_frame, text="Air Temp.")
a_temp_entry = Entry(flow_frame, width=6) 
a_temp_unit = Label(flow_frame, text="deg C")
a_temp_entry.insert(END, "25.0")

# arranging all the widgets in flow frame
fl_heading_1.grid(row=0, column=0, padx=1, pady=1)
fl_heading_2.grid(row=0, column=1, padx=1, pady=1)
fl_heading_3.grid(row=0, column=2, padx=1, pady=1)
f_flow_label.grid(row=1, column=0, padx=1, pady=1, sticky=E)
f_flow_entry.grid(row=1, column=1, padx=1, pady=1)
f_flow_unit.grid(row=1, column=2, padx=1, pady=1, sticky=W)
eq_ratio_label.grid(row=2, column=0, padx=1, pady=1, sticky=E)
eq_ratio_entry.grid(row=2, column=1, padx=1, pady=1)
f_temp_label.grid(row=3, column=0, padx=1, pady=1, sticky=E)
f_temp_entry.grid(row=3, column=1, padx=1, pady=1)
f_temp_unit.grid(row=3, column=2, padx=1, pady=1, sticky=W)
a_temp_label.grid(row=4, column=0, padx=1, pady=1, sticky=E)
a_temp_entry.grid(row=4, column=1, padx=1, pady=1)
a_temp_unit.grid(row=4, column=2, padx=1, pady=1, sticky=W)

# _____________________________________________________________________________________________
# arranging and configuring all the frames in main 'root' window
separator_1 = Frame(root, width=10)  # creating a blank frame for separation
separator_1.grid(row=0, column=0)  # arranging this separation in main 'root' window

separator_2 = Frame(root, height=5)
title_label = Label(separator_2, text="Combustion of Gaseous Fuels", font="bold")  # creating frame title
title_label.grid()
separator_2.grid(row=0, column=1, columnspan=5)

fuel_frame.grid(row=1, column=1)  # arranging fuel frame in main 'root' window
fuel_frame.config(borderwidth=2, relief=RAISED)     # configuring fuel frame

separator_3 = Frame(root, height=5)
separator_3.grid(row=2, column=1)

air_frame.grid(row=3, column=1)
air_frame.config(borderwidth=2, relief=RAISED)

separator_4 = Frame(root, height=5)
separator_4.grid(row=4, column=1)

flow_frame.grid(row=5, column=1)
flow_frame.config(borderwidth=2, relief=RAISED)

# configuring column sizes to ensure all frames line up and don't expand/contract on option selection
flow_frame.columnconfigure(0, minsize=129)
air_frame.columnconfigure(0, minsize=150)
fuel_frame.columnconfigure(0, minsize=150)

blank_canvas = Canvas(root, width=1020, height=587, bg="white")  # creating a blank canvas in main 'root' window
blank_canvas.grid(row=1, column=2, sticky=N, rowspan=5, columnspan=4, padx=10)


# ______________________________________________________________________________________________________________________
# Defining a function to perform all the calculations
def calculate():  # this function is executed on clicking "Calculate" button

    # Taking air, fuel and output flue gas line pressure as 1 atm
    global a_P
    a_P = 1     # air Pressure
    global f_P
    f_P = 1     # fuel Pressure
    global o_P
    o_P = 1     # combustion process is assumed to occur at constant pressure = 1 atm
    
    # Molar percentage of all fuel components are read -> converted to float -> stored in an array
    global f_entry_array
    f_entry_array = [float(f_entry_1.get()), float(f_entry_2.get()), float(f_entry_3.get()),
                     float(f_entry_4.get()), float(f_entry_5.get()), float(f_entry_6.get()),
                     float(f_entry_7.get()), float(f_entry_8.get())]
    
    global f_entry_total
    f_entry_total = round(sum(f_entry_array), 0)  # summation of molar percentage of all fuel components
    
    # All fuel components are read -> stored in an array as strings
    global f_fuel_array
    f_fuel_array = [f_option_1.get(), f_option_2.get(), f_option_3.get(), f_option_4.get(),
                    f_option_5.get(), f_option_6.get(), f_option_7.get(), f_option_8.get()]
    
    # Molar percentage of all air components are read -> converted to float -> stored in an array
    global a_entry_array
    a_entry_array = [float(a_entry_1.get()), float(a_entry_2.get()), float(a_entry_3.get()),
                     float(a_entry_4.get()), float(a_entry_5.get())]
    
    global a_entry_total
    a_entry_total = round(sum(a_entry_array), 0)  # summation of molar percentage of all air components
    
    # All air components are read -> stored in an array as strings
    global a_air_array
    a_air_array = [a_option_1.get(), a_option_2.get(), a_option_3.get(), a_option_4.get(), a_option_5.get()]

    # ___________________________________________________________________________________________________
    # Making a function to perform mass and energy balance
    def calc_display():  # this function makes all the calculations: mass balance and energy balance

        def f_mol_ratio(fuel_name):  # function to calculate molar ratio of any fuel component
            i = f_fuel_array.index(fuel_name)
            y = f_entry_array[i]/100
            return y
        
        def a_mol_ratio(air_name):  # function to calculate molar ratio of any air component
            i = a_air_array.index(air_name)
            y = a_entry_array[i]/100
            return y

        # __________________
        # Step1: finding molar ratio of each fuel component
        try:  # try to execute below mentioned code
            f_x_ch4 = f_mol_ratio("Methane")  # calculate molar ratio of ch4
        except ValueError:  # if try returns error, then execute below code
            f_x_ch4 = 0  # if error is found i.e. 'methane' is not in input fuel, mole of ch4 = zero
        
        try:
            f_x_co = f_mol_ratio("Carbon Monoxide")
        except ValueError:
            f_x_co = 0
        
        try:
            f_x_h2 = f_mol_ratio("Hydrogen")
        except ValueError:
            f_x_h2 = 0
        
        try:
            f_x_c2h6 = f_mol_ratio("Ethane")
        except ValueError:
            f_x_c2h6 = 0
        
        try:
            f_x_c2h4 = f_mol_ratio("Ethylene")
        except ValueError:
            f_x_c2h4 = 0
            
        try:
            f_x_c3h8 = f_mol_ratio("Propane")
        except ValueError:
            f_x_c3h8 = 0
            
        try:
            f_x_c4h10 = f_mol_ratio("Butane")
        except ValueError:
            f_x_c4h10 = 0
        
        try:
            f_x_c2h2 = f_mol_ratio("Acetylene")
        except ValueError:
            f_x_c2h2 = 0
            
        try:
            f_x_h2s = f_mol_ratio("Hydrogen Sulphide")
        except ValueError:
            f_x_h2s = 0
        
        try:
            f_x_co2 = f_mol_ratio("Carbon Dioxide")
        except ValueError:
            f_x_co2 = 0
        
        try:
            f_x_n2 = f_mol_ratio("Nitrogen")
        except ValueError:
            f_x_n2 = 0
        
        try:
            f_x_o2 = f_mol_ratio("Oxygen")
        except ValueError:
            f_x_o2 = 0

        # __________________
        # Step 2: finding molar ratios of each air component
        try:
            a_x_n2 = a_mol_ratio("Nitrogen")  # try to calculate molar ratio of Nitrogen
        except ValueError:
            a_x_n2 = 0  # if error is returned, put moles of nitrogen = zero
        
        try:
            a_x_o2 = a_mol_ratio("Oxygen")
        except ValueError:
            a_x_o2 = 0
        
        try:
            a_x_co2 = a_mol_ratio("Carbon Dioxide")
        except ValueError:
            a_x_co2 = 0
        
        try:
            a_x_h2o = a_mol_ratio("Moisture(H2O)")
        except ValueError:
            a_x_h2o = 0
        
        try:
            a_x_ar = a_mol_ratio("Argon")
        except ValueError:
            a_x_ar = 0

        # __________________
        # Step 3: Reading input flow properties from user input
        global f_flow_rate
        f_flow_rate = float(f_flow_entry.get())
        global eq_ratio
        eq_ratio = float(eq_ratio_entry.get())
        global f_temp
        f_temp = float(f_temp_entry.get()) + 273.15  # converting deg C to Kelvin
        global a_temp
        a_temp = float(a_temp_entry.get()) + 273.15

        global R_n  # Universal gas constant: assigning R_n variable as a global variable
        R_n = 0.00008205  # m3.atm/mol.K (value of R used for calculating moles)

        # __________________
        # Step 4: Mass Balance
        # finding moles of each fuel component - Basis is 1 minute of flow
        global n_fuel
        n_fuel = (f_P * f_flow_rate)/(R_n * f_temp)  # calculate total fuel moles: using ideal gas equation
        f_n_ch4 = f_x_ch4 * n_fuel  # moles of a fuel component = (mole fraction of the component) * (total fuel moles)
        f_n_co = f_x_co * n_fuel
        f_n_h2 = f_x_h2 * n_fuel
        f_n_c2h6 = f_x_c2h6 * n_fuel
        f_n_c2h4 = f_x_c2h4 * n_fuel
        f_n_c3h8 = f_x_c3h8 * n_fuel
        f_n_c4h10 = f_x_c4h10 * n_fuel
        f_n_c2h2 = f_x_c2h2 * n_fuel
        f_n_h2s = f_x_h2s * n_fuel
        f_n_co2 = f_x_co2 * n_fuel
        f_n_n2 = f_x_n2 * n_fuel
        f_n_o2 = f_x_o2 * n_fuel

        # storing moles of each fuel component in an array
        global f_n_array
        f_n_array = [f_n_ch4, f_n_co, f_n_h2, f_n_c2h6, f_n_c2h4, f_n_c3h8, f_n_c4h10, f_n_c2h2, f_n_h2s,
                     f_n_co2, f_n_n2, f_n_o2]

        # calculating total amount of oxygen required for complete combustion
        global n_o2_total_required
        n_o2_total_required = 2*f_n_ch4 + 0.5*f_n_co + 0.5*f_n_h2 + 3.5*f_n_c2h6 + 3*f_n_c2h4 +\
            5*f_n_c3h8 + 6.5*f_n_c4h10 + 2.5*f_n_c2h2 + 1.5*f_n_h2s
                        
        # calculating oxygen required from air for complete combustion since fuel might contain some oxygen
        global n_o2_air_required
        n_o2_air_required = n_o2_total_required - f_n_o2  # total oxygen requirement - oxygen i/p from fuel

        # calculating theoretical moles of air required for complete combustion of fuel
        global n_air_theoretical
        n_air_theoretical = n_o2_air_required/a_x_o2

        # calculating actual amount of air supplied using equivalence ratio
        global n_air_actual
        n_air_actual = n_air_theoretical * eq_ratio  # if equivalence ratio=1, no excess air is used

        # calculating flow rate of air by finding moles of air supplied per minute (remember basis was 1 minute)
        global a_flow_rate
        a_flow_rate = (n_air_actual * R_n * a_temp)/a_P  # converting air moles into air volume (m3/min)

        # calculating moles of each air component
        a_n_n2 = a_x_n2 * n_air_actual  # moles of nitrogen = mole fraction of nitrogen * total moles of air
        a_n_o2 = a_x_o2 * n_air_actual  # moles of oxygen molecule
        a_n_co2 = a_x_co2 * n_air_actual  # moles of co2
        a_n_h2o = a_x_h2o * n_air_actual  # moles of h2o
        a_n_ar = a_x_ar * n_air_actual  # moles of argon

        # storing moles of all air components in an array
        global a_n_array
        a_n_array = [a_n_n2, a_n_o2, a_n_co2, a_n_h2o, a_n_ar]
        
        # Finding output gas components i.e. combustion products using stoichiometric conservation of elements
        out_n_n2 = f_n_n2 + a_n_n2  # nitrogen balance: input n2 moles = output n2 moles (INERT)

        out_n_co2 = f_n_ch4 + f_n_co + 2*f_n_c2h6 + 2*f_n_c2h4 + 3*f_n_c3h8 + 4*f_n_c4h10 + 2*f_n_c2h2 + f_n_co2 + \
            a_n_co2  # carbon balance: i/p C = o/p C
        
        out_n_h2o = 2*f_n_ch4 + f_n_h2 + 3*f_n_c2h6 + 2*f_n_c2h4 + 4*f_n_c3h8 + 5*f_n_c4h10 + f_n_c2h2 + f_n_h2s + \
            a_n_h2o  # hydrogen balance: i/p H = o/p H
                  
        out_n_o2 = f_n_o2 + a_n_o2 - n_o2_total_required  # oxygen balance
        out_n_so2 = f_n_h2s  # sulphur balance
        out_n_ar = a_n_ar  # argon balance (INERT)

        # creating an array with strings denoting moles of each output gas component
        global out_n_list
        out_n_list = ["n(N2)", "n(CO2)", "n(H2O)", "n(O2)", "n(SO2)", "n(Ar)"]

        # storing moles of all output gas components in an array
        global out_n_array
        out_n_array = [out_n_n2, out_n_co2, out_n_h2o, out_n_o2, out_n_so2, out_n_ar]

        # calculating total moles of output gas (combustion products)
        global out_n_total
        out_n_total = round(sum(out_n_array), 0)

        # calculating molar percentage of each output gas component
        out_percent_n2 = (out_n_n2/out_n_total)*100
        out_percent_co2 = (out_n_co2/out_n_total)*100
        out_percent_h2o = (out_n_h2o/out_n_total)*100
        out_percent_o2 = (out_n_o2/out_n_total)*100
        out_percent_so2 = (out_n_so2/out_n_total)*100
        out_percent_ar = (out_n_ar/out_n_total)*100

        # storing the molar percentage of each output gas component in an array
        global out_value_array
        out_value_array = [out_percent_n2, out_percent_co2, out_percent_h2o, out_percent_o2, out_percent_so2,
                           out_percent_ar]

        # storing the full name of all possible output gas components in an array
        global out_component_array
        out_component_array = ["Nitrogen", "Carbon Dioxide", "Moisture(H2O)", "Oxygen", "Sulphur Dioxide", "Argon"]
        
        # Reading thermodynamic data from excel file using panda library to read thermo data sheet
        # First row of excel sheet is taken as column headers
        h_data = pandas.read_excel("thermo_Data.xlsm", sheetname="enthalpy")
    
        # fuel and air temp array for multiplication with respective enthalpy terms
        # H(T) - H(298) = AT + BT^2 + C(1/T) + D(T^0.5) + ET^3 + F
        f_temp_array = [f_temp, f_temp**2, 1/f_temp, f_temp**0.5, f_temp**3, 1]
        a_temp_array = [a_temp, a_temp**2, 1/a_temp, a_temp**0.5, a_temp**3, 1]
        
        # ______________________
        # Step5: Heat Balance
        # calculating SENSIBLE HEAT IN FUEL
        # We can call column values by using column headers 
        # e.g. h_data["Methane"] calls in all values in column with "Methane" column header and saves it as an array
        # numpy.multiply(x,y) performs element wise multiplication between x and y array
        # creating a function to calculate sensible heat of any component by feeding the name of the gas
        def f_h_sens(gas_name):
            sens_heat = sum(numpy.multiply(h_data[gas_name], f_temp_array))
            return sens_heat

        # calculating sensible heat of each fuel component
        f_h_sens_ch4 = f_n_ch4 * f_h_sens("Methane")  # sensible heat of a component=no. of moles * sensible heat/mole
        f_h_sens_co = f_n_co * f_h_sens("Carbon Monoxide")
        f_h_sens_h2 = f_n_h2 * f_h_sens("Hydrogen")
        f_h_sens_c2h6 = f_n_c2h6 * f_h_sens("Ethane")
        f_h_sens_c2h4 = f_n_c2h4 * f_h_sens("Ethylene")
        f_h_sens_c3h8 = f_n_c3h8 * f_h_sens("Propane")
        f_h_sens_c4h10 = f_n_c4h10 * f_h_sens("Butane")
        f_h_sens_c2h2 = f_n_c2h2 * f_h_sens("Acetylene")
        f_h_sens_h2s = f_n_h2s * f_h_sens("Hydrogen Sulphide")
        f_h_sens_co2 = f_n_co2 * f_h_sens("Carbon Dioxide")
        f_h_sens_n2 = f_n_n2 * f_h_sens("Nitrogen")
        f_h_sens_o2 = f_n_o2 * f_h_sens("Oxygen")

        # storing sensible heat of each fuel component in an array
        global f_h_sens_array
        f_h_sens_array = [f_h_sens_ch4, f_h_sens_co, f_h_sens_h2, f_h_sens_c2h6, f_h_sens_c2h4, f_h_sens_c3h8,
                          f_h_sens_c4h10, f_h_sens_c2h2, f_h_sens_h2s, f_h_sens_co2, f_h_sens_n2, f_h_sens_o2]

        # finding total sensible heat of fuel by adding sensible heat of each component
        global f_h_sens_total
        f_h_sens_total = sum(f_h_sens_array)

        # calculating SENSIBLE HEAT IN AIR
        # creating a function to calculate sensible heat of any air component by feeding the gas name
        def a_h_sens(gas_name):
            sens_heat = sum(numpy.multiply(h_data[gas_name], a_temp_array))
            return sens_heat

        # calculating sensible heat of each air component
        a_h_sens_n2 = a_n_n2 * a_h_sens("Nitrogen")  # sensible heat of a component=no. of moles * sensible heat/mole
        a_h_sens_o2 = a_n_o2 * a_h_sens("Oxygen")
        a_h_sens_co2 = a_n_co2 * a_h_sens("Carbon Dioxide")
        a_h_sens_h2o = a_n_h2o * a_h_sens("Moisture(H2O)")
        a_h_sens_ar = a_n_ar * a_h_sens("Argon")

        # storing sensible heat of each component in an array
        global a_h_sens_array
        a_h_sens_array = [a_h_sens_n2, a_h_sens_o2, a_h_sens_co2, a_h_sens_h2o, a_h_sens_ar]

        # calculating total sensible heat of air by adding sensible heat of each air component
        global a_h_sens_total
        a_h_sens_total = sum(a_h_sens_array)

        # calculating total sensible heat of input i.e. fuel+air
        global H_sens_total
        H_sens_total = f_h_sens_total+a_h_sens_total

        # __________________________
        # Step 6: Calculating heat of combustion (calorific value) of each fuel component
        # Reading heat of formation values from thermodynamic database in 'thermo_Data.xlsm' excel file
        # Note-1st row in excel read as column headers
        dhf_data = pandas.read_excel("thermo_Data.xlsm", sheetname="dHf")

        # calculating heat of combustion of each combustible fuel component
        # heat of combustion = heat of formation of products - heat of formation of reactants
        # Note: heat of combustion is being stored as positive values (taking absolute)
        h_comb_ch4 = float(abs(dhf_data["CO2"] + 2*dhf_data["H2O"] - 2*dhf_data["O2"] - dhf_data["CH4"]))
        h_comb_co = float(abs(dhf_data["CO2"] - 0.5*dhf_data["O2"] - dhf_data["CO"]))
        h_comb_h2 = float(abs(dhf_data["H2O"] - 0.5*dhf_data["O2"] - dhf_data["H2"]))
        h_comb_c2h6 = float(abs(2*dhf_data["CO2"] + 3*dhf_data["H2O"] - 3.5*dhf_data["O2"] - dhf_data["C2H6"]))
        h_comb_c2h4 = float(abs(2*dhf_data["CO2"] + 2*dhf_data["H2O"] - 3*dhf_data["O2"] - dhf_data["C2H4"]))
        h_comb_c3h8 = float(abs(3*dhf_data["CO2"] + 4*dhf_data["H2O"] - 5*dhf_data["O2"] - dhf_data["C3H8"]))
        h_comb_c4h10 = float(abs(4*dhf_data["CO2"] + 5*dhf_data["H2O"] - 6.5*dhf_data["O2"] - dhf_data["C4H10"]))
        h_comb_c2h2 = float(abs(2*dhf_data["CO2"] + dhf_data["H2O"] - 2.5*dhf_data["O2"] - dhf_data["C2H2"]))
        h_comb_h2s = float(abs(dhf_data["H2O"] + dhf_data["SO2"] - 1.5*dhf_data["O2"] - dhf_data["H2S"]))
        
        # storing MOLAR heat of combustion of each fuel component in an array
        global H_molar_comb_array  
        H_molar_comb_array = [h_comb_ch4, h_comb_co, h_comb_h2, h_comb_c2h6, h_comb_c2h4, h_comb_c3h8, h_comb_c4h10, 
                              h_comb_c2h2, h_comb_h2s]

        # storing TOTAL heat of combustion of each fuel component in an array
        global h_comb_array
        h_comb_array = [f_n_ch4*h_comb_ch4, f_n_co*h_comb_co, f_n_h2*h_comb_h2, f_n_c2h6*h_comb_c2h6,
                        f_n_c2h4*h_comb_c2h4, f_n_c3h8*h_comb_c3h8, f_n_c4h10*h_comb_c4h10,
                        f_n_c2h2*h_comb_c2h2, f_n_h2s*h_comb_h2s]
        
        global f_h_comb_total
        f_h_comb_total = float(f_n_ch4*h_comb_ch4 + f_n_co*h_comb_co + f_n_h2*h_comb_h2 + f_n_c2h6*h_comb_c2h6 +
                               f_n_c2h4*h_comb_c2h4 + f_n_c3h8*h_comb_c3h8 + f_n_c4h10*h_comb_c4h10 +
                               f_n_c2h2*h_comb_c2h2 + f_n_h2s*h_comb_h2s)

        # _____________________________
        # Step 6: calculating SENSIBLE HEAT IN OUTPUT GASES
        # assigning symbol class to 'aft' using sympy so that a mathematical equation can be created
        # 'aft' as a symbol represents that it is a variable in an equation and is to be calculated
        global aft
        aft = sympy.Symbol("aft")

        # creating a function (with gas name as input) to make terms which prefix different termperature terms in
        # equation for sensible heat of that component
        # term 1=prefix for T, term 2=prefix for T^2
        def out_h_sens_term(term_no):
            term = (out_n_n2*h_data["Nitrogen"][term_no-1] + out_n_co2*h_data["Carbon Dioxide"][term_no-1] +
                    out_n_h2o*h_data["Moisture(H2O)"][term_no-1] + out_n_o2*h_data["Oxygen"][term_no-1] +
                    out_n_so2*h_data["Sulphur Dioxide"][term_no-1] + out_n_ar*h_data["Argon"][term_no-1])
            return term

        # creating equations for sensible heat of each output gas component
        term_1 = out_h_sens_term(1)  # prefix for T
        term_2 = out_h_sens_term(2)  # prefix for T^2
        term_3 = out_h_sens_term(3)  # prefix for 1/T
        term_4 = out_h_sens_term(4)  # prefix for sqrt(T)
        term_5 = out_h_sens_term(5)  # prefix for T^3
        term_6 = out_h_sens_term(6)  # constant F
        
        # __________________________________
        # Step 7: CALCULATING Adiabatic Flame temperature
        T = 298.15  # initiating the value of T as room T

        # creating a function to calculate error value for any Temperature value
        def error_evaluate(T):
            error = term_1*T + term_2*(T**2) + term_3*(1/T) + term_4*(T**0.5) + \
               term_5*(T**3) + term_6 - f_h_comb_total - f_h_sens_total - a_h_sens_total
            return error
        
        # creating loops for iterations to find AFT value where error == 0
        # i.e  T at which: Sensible heat of output gases = Total input sensisble heat(fuel+air) + combustion heat
        while error_evaluate(T) < 0:
            T = T+100
        else:
            T = T-100
            while error_evaluate(T) < 0:
                T = T+10
            else:
                T = T-10
                while error_evaluate(T) < 0:
                    T = T+1
                else:
                    T = T-1
                    while error_evaluate(T) < 0:
                        T = T+0.1
                    else:
                        T = T-0.1
                        while error_evaluate(T) < 0:
                            T = T+0.01

        aft = T-273.15  # converting Kelvins into deg C

        global o_flow_rate
        o_flow_rate = (out_n_total * R_n * T)/o_P  # flow rate of o/p gas at AFT temperature: ideal gas equation

        # ______________________________
        # Step 8: Display process layout containing calculated data
        display_layout()  # execute the 'display_layout' function which has been created below
        # So when calculate button pressed, 'display_layout' function will also be executed

    # _______________________________
    # creating some lists which are later used in the program while displaying mass/energy balance and hess diagram
    global out_value_list
    out_value_list = ["% N2 = ", "% CO2 = ", "% H2O = ", "% O2 = ", "% SO2 = ", "% Ar = "]

    global rxns_list
    rxns_list = ["CH4 + 2 O2 = CO2 + 2 H2O",
                 "CO + 0.5 O2 = CO2",
                 "H2 + 0.5 O2 = H2O",
                 "C2H6 + 3.5 O2 = 2 CO2 + 3 H2O",
                 "C2H4 + 3 O2 = 2 CO2 + 2 H2O",
                 "C3H8 + 5 O2 = 3 CO2 + 4 H2O",
                 "C4H10 + 6.5 O2 = 4 CO2 + 5 H2O",
                 "C2H2 + 2.5 O2 = 2 CO2 + H2O",
                 "H2S + 1.5 O2 = SO2 + H2O", "", "", ""]

    global a_n_list
    a_n_list = ["n(N2)", "n(O2)", "n(CO2)", "n(H2O)", "n(Ar)"]

    global f_n_list
    f_n_list = ["n(CH4)", "n(CO)", "n(H2)", "n(C2H6)", "n(C2H4)", "n(C3H8)", "n(C4H10)", "n(C2H2)", "n(H2S)",
                "n(CO2)", "n(N2)", "n(O2)"]

    global out_list
    out_list = ["n(N2)_o/p_gas = n(N2)_fuel + n(N2)_air",
                "n(CO2)_o/p_gas = n(CO2)_fuel + n(CO2)_combustion + n(CO2)_air",
                "n(H2O)_o/p_gas = n(H2O)_combustion + n(H2O)_air",
                "n(O2)_o/p_gas = n(O2)_air_actual - n(O2)_air_required",
                "n(SO2)_o/p_gas = n(H2S)_fuel", "n(Ar)_o/p_gas = n(Ar)_air"]

    # __________________________________________
    # Error handling: When user input for mole percent of fuel/air components don't add up to 100
    if f_entry_total != 100 or a_entry_total != 100:
        if f_entry_total != 100 and a_entry_total != 100:
            showerror(title="Error", message="Mole % of air and fuel components don't add up to 100%.")
        else:
            if f_entry_total != 100:
                showerror(title="Error", message="Mole % of fuel components don't add up to 100")
            else:
                showerror(title="Error", message="Mole % of air components don't add up to 100")

    else:
        calc_display()  # function executed when molar percentages of both fuel and air components add up to 100
    

# _____________________________________________________________________________________________________________________
# Creating a function to display process layout
def display_layout():
    layout_frame = Frame(root, width=1020, height=587)  # creating a frame that will contain process layout
    layout_frame.grid(row=1, column=2, sticky=N, rowspan=5, columnspan=4, padx=10)  # arranging layout frame

    # creating a canvas in layout frame where process data will be written later
    layout_canvas = Canvas(layout_frame, width=1020, height=587, bg="white", scrollregion=(0, 0, 1100, 600))
    layout_canvas.pack(side=RIGHT, expand=True, fill=BOTH)  # arranging canvas

    # adding process layout image to the canvas
    my_image = PhotoImage(file="layout_feed.gif")  # assigns the image to a variable
    layout_canvas.create_image(0, 0, anchor=NW, image=my_image)  # adding image to the canvas

    # creating a function to display the input fuel data in layout canvas
    def display_f_table():
        index = numpy.nonzero(f_entry_array)[0]  # gets the index of all non-zero elements in the f_entry_array
        count = 0  # initiating count with zero value
        for n in index:  # loop runs for values stored in index array
            x1 = 110
            y1 = 35+15*count
            layout_canvas.create_text(x1, y1, text=f_fuel_array[n], anchor="e")
                
            x2 = x1+15
            y2 = y1
            layout_canvas.create_text(x2, y2, text=f_entry_array[n], anchor="w")
            
            count = count+1
                
        layout_canvas.create_text(x1, 20, text="Fuel Component", anchor="e", fill="magenta")
        layout_canvas.create_text(x2, 20, text="Molar Ratio(%)", anchor="w", fill="magenta")

    # creating a function to display the input air table in layout canvas
    def display_a_table():
        index = numpy.nonzero(a_entry_array)[0]
        count = 0
        for n in index:
            x1 = 110
            y1 = 515+15*count
            layout_canvas.create_text(x1, y1, text=a_air_array[n], anchor="e")
                
            x2 = x1+15
            y2 = y1
            layout_canvas.create_text(x2, y2, text=a_entry_array[n], anchor="w")
                
            count = count+1
        layout_canvas.create_text(x1, 500, text="Air Component", anchor="e", fill="magenta")
        layout_canvas.create_text(x2, 500, text="Molar Ratio(%)", anchor="w", fill="magenta")

    # creating a function to display the output gas composition table
    def display_o_table():
        index = numpy.nonzero(out_value_array)[0]
        count = 0
        for n in index:
            x1 = 910
            y1 = 35+15*count  # line spacing will be equal to 15 pixels
            layout_canvas.create_text(x1, y1, text=out_component_array[n], anchor="e")
        
            x2 = x1+15
            y2 = y1
            layout_canvas.create_text(x2, y2, text=round(out_value_array[n], 1), anchor="w")
                
            count = count+1
        layout_canvas.create_text(x1, 20, text="Flue Gas Component", anchor="e", fill="magenta")
        layout_canvas.create_text(x2, 20, text="Molar Ratio(%)", anchor="w", fill="magenta")

    # creating a function to display the flow rates (i/p fuel/air, o/p gas)
    def display_flow_rates():
        layout_canvas.create_text(350, 18, text="Fuel Flow Rate = " + str(f_flow_rate) + " m3/min", fill="red")
        layout_canvas.create_text(350, 33, text="Fuel Temperature = " + str(f_temp_entry.get()) + " deg C", fill="red")
        layout_canvas.create_text(120, 265, text="Air Flow Rate = " + str(round(a_flow_rate, 2)) + " m3/min",
                                  fill="blue")
        layout_canvas.create_text(120, 280, text="Air Temperature = " + str(a_temp_entry.get()) + " deg C", fill="blue")
        layout_canvas.create_rectangle(410, 428, 550, 458, fill="cyan")
        layout_canvas.create_text(477, 442, text="Equivalence Ratio = " + str(eq_ratio))
        layout_canvas.create_rectangle(633, 215, 755, 255, fill="cyan")
        layout_canvas.create_text(693, 235, text="AFT = " + str(round(aft, 2)) + " deg C")
        layout_canvas.create_text(660, 40, text="Flue Gas\nFlow Rate", fill="orange")
        layout_canvas.create_text(732, 42, text=" = " + str(round(o_flow_rate, 2)) + " m3/min", fill="orange")

    # executing all the functions that were defined above
    display_f_table()
    display_a_table()
    display_o_table()
    display_flow_rates()
    layout_canvas.mainloop()


# ********************************************************************************
# Display step-wise mass balance calculations on canvas
def display_mass_balance():  # function to display mass balance data on canvas
    mass_balance_canvas = Canvas(root, width=1020, height=587, bg="white")  # creating canvas for mass balance display
    mass_balance_canvas.grid(row=1, column=2, sticky=N, rowspan=5, columnspan=4, padx=10)  # arranging canvas

    # _________________________________
    # Step 1: creating function to display step 1 of mass balance
    def display_step1():
        x1 = 20  # reference x co-ord value on canvas
        y1 = 20  # reference y co-ord value on canvas

        # displaying text on canvas
        mass_balance_canvas.create_text(x1, y1, text="Step 1: Calculate total fuel moles ", anchor="w", fill="blue")
        mass_balance_canvas.create_text(x1, y1+15, text="Fuel P = " + str(f_P) + " atm", anchor="w")
        mass_balance_canvas.create_text(x1, y1+30, text="Air P = " + str(a_P) + " atm", anchor="w")
        mass_balance_canvas.create_text(x1, y1+45, text="Fuel T = " + str(f_temp)+" K", anchor="w")
        mass_balance_canvas.create_text(x1, y1+60, text="Air T = " + str(a_temp)+" K", anchor="w")

        mass_balance_canvas.create_text(x1, y1+75, text="R = " + str(R_n) + " (m3.atm)/(mol.K)", anchor="w")

        mass_balance_canvas.create_text(x1, y1+90, text="Fuel Flow Rate = " + str(f_flow_rate)+" m3/min", anchor="w")
        mass_balance_canvas.create_text(x1, y1+110, text="Calculation Basis : 1 min", anchor="w", fill="magenta")
        
        mass_balance_canvas.create_text(x1, y1+125, text="n(fuel) = (fuel P x fuel flow)/(R * fuel T)", anchor="w")
        mass_balance_canvas.create_text(x1+38, y1+140, text="= " + str(round(n_fuel, 2)) + " mol", anchor="w")
        mass_balance_canvas.create_rectangle(10, 10, 250, 190)

    # _____________________________________
    # Step 2: creating function to display step 2 of mass balance
    def display_step2():
        x1 = 300
        y1 = 20

        # displaying text on canvas
        mass_balance_canvas.create_text(x1, y1, text="Step 2: Calculate moles of each fuel component", anchor="w",
                                        fill="blue")
        mass_balance_canvas.create_text(x1, y1+15, text="n(fuel component)= n(fuel) x (% mol ratio/100)", anchor="w")
        mass_balance_canvas.create_text(x1, y1+30, text="Fuel Component", anchor="w", fill="magenta")
        mass_balance_canvas.create_text(x1+150, y1+30, text="No. of moles", anchor="w", fill="magenta")

        index = numpy.nonzero(f_n_array)[0]  # stores index of non-zero elements in f_n_array
        count = 0
        for n in index:  # loop runs for all values stored in index array
            x1 = x1
            y1 = 65+15*count  # y value increased by 15 in every loop - 15 pixel line spacing as a result
            mass_balance_canvas.create_text(x1, y1, text=f_n_list[n] + " = ", anchor="w")
            
            x2 = x1+150
            y2 = y1
            mass_balance_canvas.create_text(x2, y2, text=round(f_n_array[n], 2), anchor="w")
            
            count = count+1
        
        mass_balance_canvas.create_rectangle(290, 10, 570, 190)

    # _____________________________________
    # Step 3: creating function to display step 3 on canvas
    def display_step3():
        x1 = 620
        y1 = 20
        mass_balance_canvas.create_text(x1, y1, text="Step 3: List all combustion reactions", anchor="w", fill="blue")

        # creating a list of all possible combustion rxns - order of rxns is same as that of f_n_array
        global rxns_list
        rxns_list = ["CH4 + 2 O2 = CO2 + 2 H2O",
                     "CO + 0.5 O2 = CO2",
                     "H2 + 0.5 O2 = H2O",
                     "C2H6 + 3.5 O2 = 2 CO2 + 3 H2O",
                     "C2H4 + 3 O2 = 2 CO2 + 2 H2O",
                     "C3H8 + 5 O2 = 3 CO2 + 4 H2O",
                     "C4H10 + 6.5 O2 = 4 CO2 + 5 H2O",
                     "C2H2 + 2.5 O2 = 2 CO2 + H2O",
                     "H2S + 1.5 O2 = SO2 + H2O", "", "", ""]

        # displaying rxns that occur in the user selected system
        index = numpy.nonzero(f_n_array)[0]  # finding indices of all non-zero fuel components
        count = 0
        for n in index:  # running loop for all values present in 'index' to write data in canvas
            x1 = x1
            y1 = 35+15*count
            mass_balance_canvas.create_text(x1, y1, text=rxns_list[n], anchor="w")
            count = count+1
        mass_balance_canvas.create_rectangle(610, 10, 900, 150)

    # ________________________________________
    # Step 4: creating a function to display step 4 in mass balance canvas
    def display_step4():
        x1 = 620
        y1 = 200

        # creating an array (string expressions) with stoichiometric information of O2 required for combustion
        global o2_req_array
        o2_req_array = ["[2*n(CH4)]", "[0.5*n(CO)]", "[0.5*n(H2)]", "[3.5*n(C2H6)]", "[3*n(C2H4)]", "[5*n(C3H8)]",
                        "[6.5*n(C4H10)]", "[2.5*n(C2H2)]", "[1.5*n(H2S)]", "", "", ""]

        # finding the indices of all non-zero fuel components
        index = numpy.nonzero(f_n_array)[0]

        line1 = "n(O2) required=" + o2_req_array[index[0]]
        
        length = len(index)
        i = 1
        while i < 4 and i < length:
            line1 = line1 + "+" + o2_req_array[index[i]]
            i = i+1

        line2 = ""
        while i < 8 and i < length:
            line2 = line2 + "+" + o2_req_array[index[i]]
            i = i+1
        
        line3 = "n(O2)_required=" + str(round(n_o2_total_required, 2))
        
        if f_n_array[11] == 0:  # checking if oxygen is present in fuel
            line4 = "n(O2)_fuel=0"
        else:
            line4 = "n(O2)_fuel=" + str(round(f_n_array[11], 2)) + " moles"
        
        line5 = "n(O2)_air_required = n(O2)_required - n(O2)_fuel"
        line6 = "= "+str(round(n_o2_air_required, 2)) + " moles"
        line7 = "n(air)_theoretical = (100 / % O2 in air)* [n(O2)_air_required)]"
        line8 = "= "+str(round(n_air_theoretical, 2)) + " moles"
        line9 = "n(air)_actual = (equivalence ratio)* n(air)_theoretical"
        line10 = "= "+ str(round(n_air_actual, 2)) + " moles"
        line11 = "Air flow rate = [{n(air)_actual} * R * (air T)] / (air P)"
        line12 = "= " + str(round(a_flow_rate, 2))+ " m3/min"
        
        mass_balance_canvas.create_text(x1, y1, text="Step 4: Calculate O2/air requirement and actual air moles",
                                        anchor="w", fill="blue")
        mass_balance_canvas.create_text(x1, y1+15, text=line1, anchor="w")
        mass_balance_canvas.create_text(x1+20, y1+30, text=line2, anchor="w")
        mass_balance_canvas.create_text(x1, y1+45, text=line3, anchor="w")
        mass_balance_canvas.create_text(x1, y1+60, text=line4, anchor="w")
        mass_balance_canvas.create_text(x1, y1+75, text=line5, anchor="w")
        mass_balance_canvas.create_text(x1+98, y1+90, text=line6, anchor="w")
        mass_balance_canvas.create_text(x1, y1+105, text=line7, anchor="w")
        mass_balance_canvas.create_text(x1+92, y1+120, text=line8, anchor="w")
        mass_balance_canvas.create_text(x1, y1+135, text=line9, anchor="w")
        mass_balance_canvas.create_text(x1+68, y1+150, text=line10, anchor="w")
        mass_balance_canvas.create_text(x1, y1+165, text=line11, anchor="w")
        mass_balance_canvas.create_text(x1+68, y1+180, text=line12, anchor="w")

        mass_balance_canvas.create_rectangle(610, 190, 1000, 400)

    def display_step5():
        x1 = 620
        y1 = 450
        mass_balance_canvas.create_text(x1, y1, text="Step 5: Calculate moles of each air component", anchor="w",
                                        fill="blue")
        mass_balance_canvas.create_text(x1, y1+15, text="n(air component)= n(air) x (% mol ratio/100)", anchor="w")
        mass_balance_canvas.create_text(x1, y1+30, text="Air Component", anchor="w", fill="magenta")
        mass_balance_canvas.create_text(x1+150, y1+30, text="No. of moles", anchor="w", fill="magenta")
        

        index = numpy.nonzero(a_entry_array)[0]
        count = 0
        for n in index:
            x1 = x1
            y1 = 495+15*count
            mass_balance_canvas.create_text(x1, y1, text=a_n_list[n] + " = ", anchor="w")
            
            x2 = x1+150
            y2 = y1
            mass_balance_canvas.create_text(x2, y2, text=round(a_n_array[n], 2), anchor="w")
            count=count+1
        
        mass_balance_canvas.create_rectangle(610, 440, 1000, 570)
         
    def display_step6():
        x1 = 20
        y1 = 240
        mass_balance_canvas.create_text(x1, y1, text="Step 6: Calculate flue gas composition and flue gas flow rate",
                                        anchor="w", fill="blue")
        
        index = numpy.nonzero(out_n_array)[0]
        count = 0
        for n in index:
            x1 = x1
            y1 = 265+15*count
            mass_balance_canvas.create_text(x1, y1, text=out_list[n] + " = " + str(round(out_n_array[n], 2))+ " moles",
                                            anchor="w")
            count = count+1
        
        mass_balance_canvas.create_text(x1, y1+30, text="Total moles of flue gas= " + str(round(sum(out_n_array), 2)) +
                                                        " moles", anchor="w")
        mass_balance_canvas.create_text(x1, y1+60, text="Flue gas component ", anchor="w", fill="magenta")
        mass_balance_canvas.create_text(x1+150, y1+60, text="Mol % ", anchor="w", fill="magenta")
        
        y1 = y1+60
        y2 = y1
        count = 0
        for n in index:
            x1 = x1
            y1 = y1+15
            mass_balance_canvas.create_text(x1, y1, text=out_value_list[n], anchor="w")
            mass_balance_canvas.create_text(x1+150, y1, text=str(round(out_value_array[n], 2))+" %", anchor="w")
            count = count+1
            
        mass_balance_canvas.create_rectangle(10, 220, 570, 530)
        
        mass_balance_canvas.create_text(x1+230, y2, text="Flow Rate(Flue gas) = {n(flue gas) * R * AFT}/(flue_gas_P)",
                                        anchor="w")
        mass_balance_canvas.create_text(x1+335, y2+15, text="= "+str(round(o_flow_rate, 2))+" m3/min", anchor="w")
        
    def create_arrows():
        mass_balance_canvas.create_line(250, 95, 290, 95, arrow="last")
        mass_balance_canvas.create_line(570, 95, 610, 95, arrow="last")
        mass_balance_canvas.create_line(750, 150, 750, 190, arrow="last")
        mass_balance_canvas.create_line(750, 400, 750, 440, arrow="last")
        mass_balance_canvas.create_line(610, 500, 570, 380, arrow="last")

    display_step1()
    display_step2()
    display_step3()
    display_step4()
    display_step5()
    display_step6()
    create_arrows()
    mass_balance_canvas.mainloop() 


#******************************************************************************
# Display Energy balance calculations on canvas

def display_energy_balance():
    energy_balance_canvas = Canvas(root, width=1020, height=587, bg="white")
    energy_balance_canvas.grid(row=1, column=2, sticky=N, rowspan=5, columnspan=4, padx=10)
    
    h_s_fuel_list = ["H_s(CH4)", "H_s(CO)", "H_s(H2)", "H_s(C2H6)", "H_s(C2H4)", "H_s(C3H8)",
                     "H_s(C4H10)", "H_s(C2H2)", "H_s(H2S)", "H_s(CO2)", "H_s(N2)", "H_s(O2)"]

    def display_step1():
        x1 = 20
        y1 = 20
        energy_balance_canvas.create_text(x1, y1, text="", anchor="w")
        energy_balance_canvas.create_text(x1, y1, text="Step1: Calculate sensible heat i/p (fuel+air)", anchor="w", fill="blue")
        energy_balance_canvas.create_text(x1, y1+15, text="Fuel T = "+str(round(f_temp, 2))+" K", anchor="w")
        energy_balance_canvas.create_text(x1, y1+30, text="Air T = "+str(round(a_temp, 2))+" K", anchor="w")
        energy_balance_canvas.create_text(x1, y1+45, text="H_s(i) = n(i)* {H(T,i)-H(298,i)}", anchor="w")
        energy_balance_canvas.create_text(x1, y1+60, text="; where: H_s(i)=Sensible heat of component i", anchor="w")
        energy_balance_canvas.create_text(x1, y1, text="", anchor="w")
        
        # write H_s(fuel) formulae
        index = numpy.nonzero(f_n_array)[0]
        length = len(index)
        line1 = "H_s(fuel) = "+h_s_fuel_list[index[0]]     
        
        i = 1
        while i < 4 and i < length:
            line1 = line1+"+"+h_s_fuel_list[index[i]]
            i = i+1

        line2 = ""
        while i < 8 and i < length:
            line2 = line2+"+"+h_s_fuel_list[index[i]]
            i = i+1
                
        h_s_air_list = ["H_s(N2)", "H_s(CO2)", "H_s(H2O)", "H_s(O2)", "H_s(SO2)", "H_s(Ar)"]

        index = numpy.nonzero(a_n_array)[0]
        length = len(index)
        line3 = "H_s(air) = "+h_s_air_list[index[0]]
        
        i = 1
        while i < 4 and i < length:
            line3 = line3+"+"+h_s_air_list[index[i]]
            i = i+1

        line4 = ""
        while i < 6 and i < length:
            line4 = line4+"+"+h_s_air_list[index[i]]
            i = i+1
            
        energy_balance_canvas.create_text(x1, y1+80, text=line1, anchor="w")
        energy_balance_canvas.create_text(x1+10, y1+95, text=line2, anchor="w")
        energy_balance_canvas.create_text(x1, y1+110, text=line3, anchor="w")
        energy_balance_canvas.create_text(x1, y1+125, text=line4, anchor="w")
        
        if f_temp == 298.15:
            h_s_fuel = 0
            energy_balance_canvas.create_text(x1, y1+140, text="H_s(fuel)= "+ str(h_s_fuel), anchor="w")
        else:
            h_s_fuel = f_h_sens_total
            energy_balance_canvas.create_text(x1, y1+140, text="H_s(fuel)= "+str(round(h_s_fuel, 2))+" calories",
                                              anchor="w")
                
        if a_temp == 298.15:
            h_s_air = 0
            energy_balance_canvas.create_text(x1, y1+155, text="H_s(air)= "+str(h_s_air), anchor="w")
        else:
            h_s_air = a_h_sens_total
            energy_balance_canvas.create_text(x1, y1+155, text="H_s(air)= "+str(round(h_s_air, 2))+" calories",
                                              anchor="w")
        global h_s_total
        h_s_total = h_s_air + h_s_fuel
        energy_balance_canvas.create_text(x1, y1+170, text="H_s(Total)= "+str(round(h_s_total, 2))+" calories",
                                          anchor="w")
        energy_balance_canvas.create_rectangle(x1-10, y1-10, 305, 205)
        
    def display_step2():
        x1 = 20
        y1 = 255
        
        energy_balance_canvas.create_text(x1, y1, text="Step2: Calculate combustion heat released", anchor="w",
                                          fill="blue")
        energy_balance_canvas.create_text(x1, y1+15, text="H_c(i)=H_f(products)- H_f(reactants)", anchor="w")
        energy_balance_canvas.create_text(x1, y1+30, text="; where: H_c(i)=Heat of combustion of i", anchor="w")
        energy_balance_canvas.create_text(x1+53, y1+45, text="H_f = Heat of formation", anchor="w")
        
        h_comb_list = ["H_c(CH4)", "H_c(CO)", "H_c(H2)", "H_c(C2H6)", "H_c(C2H4)", "H_c(C3H8)",
                       "H_c(C4H10)", "H_c(C2H2)", "H_c(H2S)", "H_c(CO2)", "H_c(N2)", "H_c(O2)"]
        
        index = numpy.nonzero(f_n_array)[0]
        length = len(index)
        line1 = "H_c(total)= "+h_comb_list[index[0]]
        
        i = 1
        while i < 4 and i < length:
            line1 = line1+"+"+h_comb_list[index[i]]
            i = i+1

        line2 = ""
        while i < 8 and i < length:
            line2 = line2+"+"+h_comb_list[index[i]]
            i = i+1
        
        energy_balance_canvas.create_text(x1, y1+65, text=line1, anchor="w")
        energy_balance_canvas.create_text(x1, y1+80, text=line2, anchor="w")
        energy_balance_canvas.create_text(x1, y1+100, text= "H_c(total)= "+str(round(f_h_comb_total, 2))+" calories",
                                          anchor="w")
        
        h_input_total = h_s_total+f_h_comb_total
        energy_balance_canvas.create_text(x1, y1+120, text="H_input(total)= "+str(round(h_input_total, 2))+" calories",
                                          anchor="w")
        
        energy_balance_canvas.create_rectangle(x1-10, y1-10, 305, 390)

    def display_step3():
        x1 = 20
        y1 = 440
        energy_balance_canvas.create_text(x1, y1, text="Step3: Write expression for flue gas sensible heat", anchor="w",
                                          fill="blue")
        energy_balance_canvas.create_text(x1, y1+20, text="H_s(i)=H(AFT,i)-H(298K,i)", anchor="w")
        energy_balance_canvas.create_text(x1, y1+35, text="; where: AFT=Adiabatic Flame Temp.", anchor="w")
        energy_balance_canvas.create_text(x1, y1+85, text="Only variable here is AFT", anchor="w", fill="green")

        h_out_list = ["H_s(N2)", "H_s(CO2)", "H_s(H2O)", "H_s(O2)", "H_s(SO2)", "H_s(Ar)"]
        
        index=numpy.nonzero(out_n_array)[0]
        length = len(index)
        
        line1 = "H_s_flue gas(total)= "+h_out_list[index[0]]
        
        i = 1
        while i < 3 and i < length:
            line1 = line1+"+"+h_out_list[index[i]]
            i = i+1

        line2 = ""
        while i < 6 and i < length:
            line2 = line2+"+"+h_out_list[index[i]]
            i = i+1
        
        energy_balance_canvas.create_text(x1, y1+55, text=line1, anchor="w")
        energy_balance_canvas.create_text(x1+30, y1+70, text=line2, anchor="w")
        energy_balance_canvas.create_rectangle(x1-10, y1-10, 305, 550)

    def display_step4():
        x1 = 400
        y1 = 20
        energy_balance_canvas.create_rectangle(x1-20, y1-15, 850, 580)
    algo_image = PhotoImage(file="algo.png")
    energy_balance_canvas.create_image(380, 8, anchor=NW, image=algo_image)
    
    display_step1()
    display_step2()
    display_step3()
    display_step4()
    
    # create arrows
    energy_balance_canvas.create_line(150, 205, 150, 245, arrow="last")
    energy_balance_canvas.create_line(150, 390, 150, 430, arrow="last")
    energy_balance_canvas.create_line(305, 490, 380, 490, arrow="last")

    # create button to display thermodynamic data
    # lambda function used because otherwise command executed automatically without button press
    thermo_data_button = Button(energy_balance_canvas, text="Show Thermodynamic \n Data",
                                command=lambda: os.startfile("thermo_Data_display.xlsm"))
    # packing the button in a window since otherwise canvas shrinks to button size
    energy_balance_canvas.create_window(865, 50, anchor=NW, window=thermo_data_button)

    energy_balance_canvas.mainloop()


# **************************************************************************
# create a function to display Hess Diagram
def display_hess_diag():
    hess_canvas = Canvas(root, width=1020, height=587, bg="white")
    hess_canvas.grid(row=1, column=2, sticky=N, rowspan=5, columnspan=4, padx=10)
    
    def hess_input_data():
        # STEP1: Draw INPUT DATA
        
        xor = 80  # origin x coord
        xmax = 950  # maximum x coord
        yor = 540  # origin y coord
        ymin = 30  # minimum y coord
        x0fuel = 150  # time=0 x coord fuel
        x0air = 250  # time=0 x coord air
        x100 = 820  # completion x coord
        yrT = 490  # room temp y coord
        
        hess_canvas.create_line(xor, yor, xor, ymin, arrow="last")  # draw y axis
        hess_canvas.create_line(xor, yor, xmax, yor, arrow="last")  # draw x axis
        hess_canvas.create_line(xmax, yor, xmax, ymin)
        hess_canvas.create_line(xor, ymin, xmax, ymin)
        hess_canvas.create_text(xor-60, 0.8*(yor-ymin), text="Temperature (deg Celcius)", anchor="nw", angle=90)
        hess_canvas.create_text(0.5*(xmax-xor), yor+20, text="Completion (%)", anchor="nw")  # label y-axis
        
        hess_canvas.create_line(xor, yrT, x100, yrT, dash=(1, 5))  # 25 degC dashed line
        hess_canvas.create_oval(xor-2, yrT-2, xor+2, yrT+2, fill="black")
        hess_canvas.create_text(xor-10, yrT, text="25")  # 25 degC label
        
        hess_canvas.create_text(x0fuel-10, yor+30, text="0 %: Reactants", anchor="nw")
        hess_canvas.create_text(x0fuel-10, yor+10, text="Fuel", anchor="nw")
        hess_canvas.create_oval(x0fuel-2, yor-2, x0fuel+2, yor+2, fill="black")  # starting point fuel
        hess_canvas.create_text(x0air-7, yor+10, text="Air", anchor="nw")
        hess_canvas.create_oval(x0air-2, yor-2, x0air+2, yor+2, fill="black")  # starting point air

        hess_canvas.create_text(x100-30, yor+10, text="100 %: Products", anchor="nw")
        hess_canvas.create_oval(x100-2, yor-2, x100+2, yor+2, fill="black")
        hess_canvas.create_line(x100, yor, x100, yrT, dash=(1, 5))  # 25 degC dashed line

        hess_canvas.create_oval(x0fuel-3, yrT-3, x0fuel+3, yrT+3, fill="orange")
        hess_canvas.create_oval(x0air-3, yrT-3, x0air+3, yrT+3, fill="blue")

        if f_temp == 298.15 and a_temp == 298.15:
            yfuelT = yrT
            yairT = yrT
            hess_canvas.create_text(x0fuel, yfuelT-10, text="Input Fuel", fill="orange")
            hess_canvas.create_text(x0fuel, yfuelT+25, text="Fuel sensible \n   heat=0", fill="orange")
            hess_canvas.create_text(x0air, yairT-10, text="Input Air", fill="blue")
            hess_canvas.create_text(x0air, yairT+25, text="Air sensible \n   heat=0", fill="blue")

        if f_temp == 298.15 and a_temp > 298.15:
            yairT = 300
            yfuelT = yrT
            hess_canvas.create_text(xor-20, yairT, text=str(a_temp-273.15))
            hess_canvas.create_oval(xor-2, yairT-2, xor+2, yairT+2)
            hess_canvas.create_oval(x0fuel-3, yfuelT-3, x0fuel+3, yfuelT+3, fill="orange")
            hess_canvas.create_oval(x0air-3, yairT-3, x0air+3, yairT+3, fill="blue")
            hess_canvas.create_line(x0air, yairT, x0air, yrT, arrow="last", fill="blue")
            hess_canvas.create_line(xor, yairT, x0air, yairT, dash=(1, 5))
            hess_canvas.create_text(x0fuel, yfuelT-10, text="Input Fuel", fill="orange")
            hess_canvas.create_text(x0air, yairT-10, text="Input Air", fill="blue")
            hess_canvas.create_text(x0fuel, yfuelT+25, text="Fuel sensible \n   heat=0", fill="orange")
            hess_canvas.create_text(x0air, yairT+100, text="Air sensible heat=\n"+str(round(a_h_sens_total, 2)) +
                                                           " calories", fill="blue", angle=90)

        if a_temp == 298.15 and f_temp > 298.15:
            yfuelT = 300
            yairT = yrT
            hess_canvas.create_text(xor-20, yfuelT, text=str(f_temp-273.15))
            hess_canvas.create_oval(xor-2, yfuelT-2, xor+2, yfuelT+2, fill="black")
            hess_canvas.create_oval(x0fuel-3, yfuelT-3, x0fuel+3, yfuelT+3, fill="orange")
            hess_canvas.create_oval(x0air-3, yairT-3, x0air+3, yairT+3, fill="blue")
            hess_canvas.create_line(x0fuel, yfuelT, x0fuel, yrT, arrow="last", fill="orange")
            hess_canvas.create_line(xor, yfuelT, x0fuel, yfuelT, dash=(1, 5))
            hess_canvas.create_text(x0fuel, yfuelT-10, text="Input Fuel", fill="orange")
            hess_canvas.create_text(x0air, yairT-10, text="Input Air", fill="blue")
            hess_canvas.create_text(x0air, yairT+25, text="Air sensible \n   heat=0", fill="blue")
            hess_canvas.create_text(x0fuel, yfuelT+100, text="Fuel sensible heat=\n"+str(round(f_h_sens_total, 2)) +
                                                             " calories", fill="orange", angle=90)
            
        if a_temp > 298.15 and f_temp > 298.15:
            if a_temp > f_temp:
                yairT = 220
                yfuelT = 360
                hess_canvas.create_text(xor-20, yairT, text=str(a_temp-273.15))
                hess_canvas.create_text(xor-20, yfuelT, text=str(f_temp-273.15))
                hess_canvas.create_oval(xor-2, yairT-2, xor+2, yairT+2, fill="black")
                hess_canvas.create_oval(xor-2, yfuelT-2, xor+2, yfuelT+2, fill="black")
                hess_canvas.create_oval(x0fuel-3, yfuelT-3, x0fuel+3, yfuelT+3, fill="orange")
                hess_canvas.create_oval(x0air-3, yairT-3, x0air+3, yairT+3, fill="blue")
                hess_canvas.create_line(x0fuel, yfuelT, x0fuel, yrT, arrow="last", fill="orange")
                hess_canvas.create_line(x0air, yairT, x0air, yrT, arrow="last", fill="blue")
                hess_canvas.create_line(xor, yairT, x0air, yairT, dash=(1, 5))
                hess_canvas.create_line(xor, yfuelT, x0fuel, yfuelT, dash=(1, 5))
                hess_canvas.create_text(x0fuel, yfuelT-10, text="Input Fuel", fill="orange")
                hess_canvas.create_text(x0air, yairT-10, text="Input Air", fill="blue")
                hess_canvas.create_text(x0air, yairT+100, text="Air sensible heat=\n"+str(round(a_h_sens_total, 2)) +
                                                               " calories", fill="blue", angle=90)
                hess_canvas.create_text(x0fuel, yfuelT+115, text="Fuel sensible heat=\n"+str(round(f_h_sens_total, 2)) +
                                                                 " calories", fill="orange", anchor="w", angle=90)

            elif a_temp < f_temp:
                yairT = 320
                yfuelT = 250
                hess_canvas.create_text(xor-20, yairT, text=str(a_temp-273.15))
                hess_canvas.create_text(xor-20, yfuelT, text=str(f_temp-273.15))
                hess_canvas.create_oval(xor-2, yairT-2, xor+2, yairT+2, fill="black")
                hess_canvas.create_oval(xor-2, yfuelT-2, xor+2, yfuelT+2, fill="black")
                hess_canvas.create_oval(x0fuel-3, yfuelT-3, x0fuel+3, yfuelT+3, fill="orange")
                hess_canvas.create_oval(x0air-3, yairT-3, x0air+3, yairT+3, fill="blue")
                hess_canvas.create_line(x0fuel, yfuelT, x0fuel, yrT, arrow="last", fill="orange")
                hess_canvas.create_line(x0air, yairT, x0air, yrT, arrow="last", fill="blue")
                hess_canvas.create_line(xor, yairT, x0air, yairT, dash=(1, 5))
                hess_canvas.create_line(xor, yfuelT, x0fuel, yfuelT, dash=(1, 5))
                hess_canvas.create_text(x0fuel, yfuelT-10, text="Input Fuel", fill="orange")
                hess_canvas.create_text(x0air, yairT-10, text="Input Air", fill="blue")
                hess_canvas.create_text(x0air, yairT+80, text="Air sensible heat=\n"+str(round(a_h_sens_total, 2)) +
                                                              " calories", fill="blue", angle=90)
                hess_canvas.create_text(x0fuel, yfuelT+140, text="Fuel sensible heat=\n"+str(round(f_h_sens_total, 2))
                                                                 + " calories", fill="orange", angle=90)
          
            elif a_temp == f_temp:
                yairT = 300
                yfuelT = 300
                hess_canvas.create_text(xor-20, yairT, text=str(a_temp-273.15))
                hess_canvas.create_oval(xor-2, yairT-2, xor+2, yairT+2, fill="black")  # dot: temp on y axis
                hess_canvas.create_oval(x0fuel-3, yfuelT-3, x0fuel+3, yfuelT+3, fill="orange")  # dot: fuel i/p
                hess_canvas.create_oval(x0air-3, yairT-3, x0air+3, yairT+3, fill="blue")  # dot: air i/p
                hess_canvas.create_line(x0fuel, yfuelT, x0fuel, yrT, arrow="last", fill="orange")  # line:fuel to room T
                hess_canvas.create_line(x0air, yairT, x0air, yrT, arrow="last", fill="blue")  # line: air goes to room T
                hess_canvas.create_line(xor, yairT, x0air, yairT, dash=(1, 5))  # dotted line: for air and fuel T
                hess_canvas.create_text(x0fuel, yfuelT-10, text="Input Fuel", fill="orange")
                hess_canvas.create_text(x0air, yairT-10, text="Input Air", fill="blue")
                hess_canvas.create_text(x0air, yairT+100, text="Air sensible heat=\n"+str(round(a_h_sens_total, 2)) +
                                                               " calories", fill="blue", angle=90)
                hess_canvas.create_text(x0fuel, yfuelT+100, text="Fuel sensible heat=\n"+str(round(f_h_sens_total, 2))
                                                                 + " calories", fill="orange", angle=90)
        
        hess_canvas.create_line(x0fuel, yor, x0fuel, yrT, dash=(1, 5))  # 25 degC dashed line
        hess_canvas.create_line(x0air, yor, x0air, yrT, dash=(1, 5))

        # write the air and fuel components along with moles input
        index = numpy.nonzero(f_n_array)[0]
        count = 0
        for n in index:
            y1 = yfuelT-25-15*count
            hess_canvas.create_text(x0fuel, y1, text=f_n_list[n] + " = ", fill="orange", anchor="e")
            hess_canvas.create_text(x0fuel+30, y1, text=round(f_n_array[n], 2), fill="orange", anchor="e")
            count = count+1

        index = numpy.nonzero(a_entry_array)[0]
        count = 0
        for n in index:
            y1 = yairT-25-15*count
            hess_canvas.create_text(x0air, y1, text=a_n_list[n] + " = ", fill="blue", anchor="e")
            hess_canvas.create_text(x0air+38, y1, text=round(a_n_array[n], 2), fill="blue", anchor="e")
            count = count+1

        # STEP2: Draw COMBUSTION DATA
        xcomb1 = x0air+80
        xcomb2 = x100-120
        hess_canvas.create_line(xcomb1, yrT, xcomb2, yrT, arrow="last", fill="red", width="2")
        hess_canvas.create_text(xcomb1+50, yrT-15, text="Total combustion heat released= "+str(round(f_h_comb_total, 2))
                                                        + " calories", fill="red", anchor="w")
        hess_canvas.create_text(xcomb1+100, yrT-30, text="Fuel + Air ----> Combustion products", fill="red", anchor="w")
        hess_canvas.create_text(xcomb1+150, yrT-45, text="COMBUSTION", fill="red", anchor="w")
        hess_canvas.create_line(xcomb1+145, yrT-38, xcomb1+233, yrT-38)

        index = numpy.nonzero(f_n_array)[0]
        count = 0
        for n in index:
            ycomb1 = yrT-70-15*count
            hess_canvas.create_text(xcomb1+50, ycomb1, text=rxns_list[n], anchor="w", fill="red")
            hess_canvas.create_text(xcomb1+250, ycomb1, text=str(round(h_comb_array[n], 2)), anchor="w", fill="red")
            count = count+1
        
        hess_canvas.create_text(xcomb1+120, ycomb1-20, text="Combustion Reaction", fill="red")
        hess_canvas.create_text(xcomb1+280, ycomb1-20, text="Combustion Heat", fill="red")
        
        # STEP3: Draw OUTPUT DATA
        xout = x100
        hess_canvas.create_oval(xout-3, yrT-3, x100+3, yrT+3, fill="purple")
        hess_canvas.create_text(xout-10, yrT+10, text="Combustion Products", fill="purple")
        
        index = numpy.nonzero(out_n_array)[0]
        count = 0
        for n in index:
            xout = x100+15
            yout = yrT-15-15*count
            hess_canvas.create_text(xout, yout, text=out_n_list[n]+"= "+str(round(out_n_array[n], 2)), fill="purple",
                                    anchor="w")
            count = count+1
        
        yaft = 120
        hess_canvas.create_line(x100, yrT, x100, yaft, arrow="last", fill="purple", width="2")
        hess_canvas.create_oval(xor-2, yaft-2, xor+2, yaft+2, fill="black")
        hess_canvas.create_line(xor, yaft, x100, yaft, dash=(1, 5))
        hess_canvas.create_text(xor-15, yaft, text="AFT", fill="purple")
        hess_canvas.create_text(x100-25, yaft-15, text="Flame components", fill="purple")

        index = numpy.nonzero(out_n_array)[0]
        count = 0
        for n in index:
            xflame = x100+35
            yflame = yaft+10-15*count
            hess_canvas.create_text(xflame, yflame, text=out_value_list[n]+str(round(out_value_array[n], 2))+" %",
                                    fill="purple", anchor="w")
            count = count+1
            
        hess_canvas.create_text(x100-15, yrT-100, text="Sensible Heat of flame= f(AFT)", fill="purple", angle=90,
                                anchor="w")
        hess_canvas.create_text(xor+350, 40, text="Energy Balance", fill="magenta", anchor="w")
        hess_canvas.create_line(xor+345, 49, xor+435, 49)
        hess_canvas.create_text(xor+100, 60, text="Fuel Sensible Heat + ", fill="orange", anchor="w")
        hess_canvas.create_text(xor+210, 60, text="Air Sensible Heat + ", fill="blue", anchor="w")
        hess_canvas.create_text(xor+313, 60, text="Combustion Heat Released =", fill="red", anchor="w")
        hess_canvas.create_text(xor+470, 60, text="Sensible heat of flame components at AFT ", fill="purple",
                                anchor="w")

    hess_input_data()
    
    hess_canvas.mainloop()

# --------------------------------------------------------------------------------
# Fuel analysis - plotting graphs to show quick comparison between fuels
# Creating a function to compare calorific values of different fuels

# --------------------------------------------------------------------------------
# Creating a function to compare AFT of different fuels under user selected parameters

# --------------------------------------------------------------------------------
# Creating a function to show effect of equivalence ratio on AFT and calorific value

# ---------------------------------------------------------------------------------
# Creating Butttons
calc_button = Button(root, text="Calculate & show process layout", command=calculate, bg="grey", fg="white")
calc_button.grid(row=6, column=1, padx=10, pady=5, sticky=N)

layout_button = Button(root, text="Process Layout", command=display_layout)
layout_button.grid(row=6, column=2, padx=10, pady=5, sticky=N)

mass_balance_button = Button(root, text="Mass Balance", command=display_mass_balance)
mass_balance_button.grid(row=6, column=3, padx=10, pady=5, sticky=N)

energy_balance_button = Button(root, text="Energy Balance", command=display_energy_balance)
energy_balance_button.grid(row=6, column=4, padx=10, pady=5, sticky=N)

hess_diag_button = Button(root, text="Graphical Energy Balance", command=display_hess_diag)
hess_diag_button.grid(row=6, column=5, padx=10, pady=5, sticky=N)

# *******************************************************************************


root.state("zoomed")  # opens maximized GUI window by default

root.mainloop()