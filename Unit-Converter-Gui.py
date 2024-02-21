import tkinter as tk
unicode_char = "\u00B2"
count = 0
def on_dropdown_change(event):
    selected_value = dropdown_var.get()
    choice = int(selected_value[0])
    # Convert the value for Centimeter to Feets
    

        
    if choice == 1:
        def centimeter_to_feets():
           
            centimeter = ent_centimeter.get()
            feets = float(centimeter)/30.48
            lbl_result["text"] = f"{round(feets, 2)} Ft"
            
        label = tk.Label(window,text="Centimeter to Feets")
        label.grid(row=2,column=1)

        frm_entry = tk.Frame(master=window)
        ent_centimeter = tk.Entry(master=frm_entry, width=10)
        lbl_centimeter = tk.Label(master=frm_entry,text="Cm")

        # Layout the temperature Entry and Label in frm_entry
        # using the .grid() geometry manager
        ent_centimeter.grid(row=3, column=0, sticky="e")
        lbl_centimeter.grid(row=3, column=1, sticky="w")

        # Create the conversion Button and result display Label
        btn_convert = tk.Button(
            master=window,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=centimeter_to_feets
        )
        lbl_result = tk.Label(master=window, text="Ft")

        #Set up the layout using the .grid() geometry manager
        frm_entry.grid(row=3, column=0, padx=10)
        btn_convert.grid(row=3, column=1, pady=10)
        lbl_result.grid(row=3, column=2, padx=10)

        

    # Convert the value for Feets to Inches
    elif choice == 2 :
        def feet_to_inches():
            feet = ent_feet.get()
            inches = float(feet) * 12
            lbl_result["text"] = f'{round(inches,2)} " '
        
        label = tk.Label(window,text="Feets to Inches")
        label.grid(row=2,column=1)
        # Create the Feets entry frame with an Entry
        # widget and label in it
        frm_entry = tk.Frame(master=window)
        ent_feet = tk.Entry(master=frm_entry, width=10)
        lbl_Inches = tk.Label(master=frm_entry,text='Ft')

        # Layout the temperature Entry and Label in frm_entry
        # using the .grid() geometry manager
        ent_feet.grid(row=3, column=0, sticky="e")
        lbl_Inches.grid(row=3, column=1, sticky="w")

        # Create the conversion Button and result display Label
        btn_convert = tk.Button(
            master=window,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=feet_to_inches
        )
        lbl_result = tk.Label(master=window, text='"')

        frm_entry.grid(row=3, column=0, padx=10)
        btn_convert.grid(row=3, column=1, pady=10)
        lbl_result.grid(row=3, column=2, padx=10)

        #Convert the value for Feets to Inches 
    elif choice == 3 :
        def sqft_to_sqmtrs():
            sqft = ent_sqft.get()
            sqmtrs = float(sqft) / 10.764
            
            lbl_result["text"] = f"{round(sqmtrs,2)} m {unicode_char} "

        label = tk.Label(window,text="Sqft to Sqmtrs")
        label.grid(row=2,column=1,sticky="e")

        frm_entry = tk.Frame(master=window)
        ent_sqft = tk.Entry(master=frm_entry, width=10)
        lbl_sqft = tk.Label(master=frm_entry,text='ft' + unicode_char) 


        # Layout the sqmtrs Entry and Label in frm_entry
        # using the .grid() geometry manager
        ent_sqft.grid(row=3, column=0, sticky="e")
        lbl_sqft.grid(row=3, column=1, sticky="w")

        # Create the conversion Button and result display Label
        btn_convert = tk.Button(
            master=window,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=sqft_to_sqmtrs
        )
        lbl_result = tk.Label(master=window, text="m" + unicode_char)

        # Set up the layout using the .grid() geometry manager
        frm_entry.grid(row=3, column=0, padx=10)
        btn_convert.grid(row=3, column=1, pady=10)
        lbl_result.grid(row=3, column=2, padx=10)         
 

    # Convert the value for sqft to Hectres or Acers
    elif choice == 4 :
        def sqft_to_hectres_or_acres():
            sqft1 = ent_sqft1.get()
            hectres = float(sqft1) / 107600
            acres = float(sqft1) / 43560
            lbl_result["text"] = f"{round(hectres,2)} ha"
            lbl1_result["text"] = f"{round(acres,2)} ac "

        label= tk.Label(window,text="Sqft to Hectres/Acers")
        label.grid(row=2,column=1)

        frm_entry = tk.Frame(master=window)
        ent_sqft1 = tk.Entry(master=frm_entry, width=10)
        lbl_sqft1 = tk.Label(master=frm_entry,text='Ft' + unicode_char) 


        # Layout the sqmtrs Entry and Label in frm_entry
        # using the .grid() geometry manager
        ent_sqft1.grid(row=3, column=0, sticky="e")
        lbl_sqft1.grid(row=3, column=1, sticky="w")

        # Create the conversion Button and result display Label
        btn_convert = tk.Button(
            master=window,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=sqft_to_hectres_or_acres
        )
        lbl_result = tk.Label(master=window, text="ha")
        lbl1_result = tk.Label(master=window, text="ac")


        # Set up the layout using the .grid() geometry manager
        frm_entry.grid(row=3, column=0, padx=10)
        btn_convert.grid(row=3, column=1, pady=10)
        lbl_result.grid(row=3, column=2, padx=10)
        lbl1_result.grid(row=3, column=3, padx=10)

# Set up the window
window = tk.Tk()
window.title("Unit Converter")
window.resizable(width=True, height=True)

# set dropdown variable
dropdown_var = tk.StringVar(window)

#create list of options
options = ["1.Centimeter to Feet","2. Feet to Inches","3. Sqft to Sqmtrs" ,"4.Sqft to Hectre or Acres"]

#set default value to the dropdown
dropdown_var.set("Choose one unit convertion")
dropdown_menu = tk.OptionMenu(window, dropdown_var, *options)
dropdown_menu.grid(row=1 ,column =1, padx=10 ,pady=10)

dropdown_menu.bind("<Configure>", on_dropdown_change)

# Run the application
window.mainloop()