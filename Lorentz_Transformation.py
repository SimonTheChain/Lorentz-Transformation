# imports the modules needed
from math import sqrt
from decimal import Decimal
from Tkinter import *


# allows creation of the app object
class Application:
    def __init__(self, master):
        """initializes the app"""
        self.master = master
        self.c = 1
        self.max_mass = 1
        self.max_length = 1

        master.title("Lorentz Transformation")

        # creates menus
        menu1 = Menu(master)
        master.config(menu=menu1, padx=20, pady=20)
        submenu1 = Menu(menu1)
        menu1.add_cascade(label="About",
                          menu=submenu1)
        submenu1.add_command(label="About the Lorentz Transformation...",
                             command=self.text_factor)
        submenu1.add_command(label="About this Program...",
                             command=self.text_program)
        submenu1.add_separator()
        submenu1.add_command(label="Exit",
                             command=self.master.quit)

        # creates frames for the widgets
        for y in range(4):
            self.master.rowconfigure(y, weight=1)
        self.master.rowconfigure(4, minsize=150, weight=2)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.frame_speed = Frame(master)
        self.frame_mass = Frame(master)
        self.frame_length = Frame(master)
        self.frame_process = Frame(master, pady=20)
        self.frame_results = LabelFrame(master, bd=4, relief=SUNKEN)
        self.frame_speed.grid(row=2, column=0, columnspan=3, sticky=N + S + E + W)
        self.frame_mass.grid(row=1, column=0, sticky=N + S + E + W)
        self.frame_length.grid(row=1, column=2, sticky=N + S + E + W)
        self.frame_process.grid(row=3, column=0, columnspan=3, sticky=N + S + E + W)
        self.frame_results.grid(row=4, column=0, columnspan=3, sticky=N + S + E + W)

        # selection of units for velocity
        self.unit_velocity = StringVar()
        label_unit_velocity = Label(self.frame_speed,
                                    text="Select the unit to be used for speed:",
                                    pady=6).pack()
        radio1 = Radiobutton(self.frame_speed,
                             text="Kilometers per second",
                             variable=self.unit_velocity,
                             value="km/s",
                             indicatoron=0,
                             command=self.c_value).pack()
        radio2 = Radiobutton(self.frame_speed,
                             text="Miles per second",
                             variable=self.unit_velocity,
                             value="mile/s",
                             indicatoron=0,
                             command=self.c_value).pack()

        self.speed_text = StringVar()
        self.speed_text.set("\n")
        label_speed = Label(self.frame_speed,
                            width=50,
                            textvariable=self.speed_text).pack()

        # selection of units for mass
        self.unit_mass = StringVar()
        label_unit_mass = Label(self.frame_mass,
                                text="Select the unit to be used for mass:",
                                pady=6).pack()
        radio3 = Radiobutton(self.frame_mass,
                             text="Kilograms",
                             variable=self.unit_mass,
                             value="kg",
                             indicatoron=0,
                             command=self.mass_entry).pack()
        radio4 = Radiobutton(self.frame_mass,
                             text="Pounds",
                             variable=self.unit_mass,
                             value="lbs",
                             indicatoron=0,
                             command=self.mass_entry).pack()

        self.mass_text = StringVar()
        self.mass_text.set("\n")
        label_mass = Label(self.frame_mass,
                           width=50,
                           textvariable=self.mass_text).pack()

        # selection of units for length
        self.unit_length = StringVar()
        label_unit_length = Label(self.frame_length,
                                  text="Select the unit to be used for length:",
                                  pady=6).pack()
        radio5 = Radiobutton(self.frame_length,
                             text="Centimeters",
                             variable=self.unit_length,
                             value="cm",
                             indicatoron=0,
                             command=self.length_entry).pack()
        radio6 = Radiobutton(self.frame_length,
                             text="Inches",
                             variable=self.unit_length,
                             value="inches",
                             indicatoron=0,
                             command=self.length_entry).pack()

        self.length_text = StringVar()
        self.length_text.set("\n")
        label_length = Label(self.frame_length,
                             width=50,
                             textvariable=self.length_text).pack()

        # creates the sliders
        self.speed = IntVar()
        self.entry_speed = Scale(self.frame_speed,
                                 from_=1,
                                 to=self.c,
                                 length=680,
                                 sliderlength=10,
                                 orient=HORIZONTAL,
                                 variable=self.speed,
                                 state=DISABLED)
        self.entry_speed.pack(fill=X)

        self.mass = IntVar()
        self.entry_mass = Scale(self.frame_mass,
                                from_=1,
                                to=self.max_mass,
                                length=300,
                                orient=HORIZONTAL,
                                variable=self.mass,
                                state=DISABLED)
        self.entry_mass.pack(fill=X)

        self.length = IntVar()
        self.entry_length = Scale(self.frame_length,
                                  from_=1,
                                  to=self.max_length,
                                  length=300,
                                  orient=HORIZONTAL,
                                  variable=self.length,
                                  state=DISABLED)
        self.entry_length.pack(fill=X)

        # creates the process button
        process_button = Button(self.frame_process,
                                text="Process",
                                fg="white",
                                bg="black",
                                padx=10,
                                pady=5,
                                relief=RAISED,
                                command=self.process).pack()

        # displays the results
        self.text_results = StringVar()
        self.label_results = Label(self.frame_results,
                                   pady=20,
                                   justify=CENTER,
                                   textvariable=self.text_results)
        self.label_results.pack(fill=BOTH, expand=TRUE)

    def c_value(self):
        """adjusts the value of c"""
        if self.unit_velocity.get() == "km/s":
            self.c = Decimal(299792458)
        elif self.unit_velocity.get() == "mile/s":
            self.c = Decimal(186282)
        self.speed_text.set("\nEnter your speed in %s"
                            % (self.unit_velocity.get()))
        self.entry_speed.config(to=self.c, state=NORMAL)
        return self.c

    def mass_entry(self):
        """adjusts the max value for mass"""
        if self.unit_mass.get() == "kg":
            self.max_mass = 225
        elif self.unit_mass.get() == "lbs":
            self.max_mass = 500
        self.mass_text.set("\nEnter your weight in %s"
                           % (self.unit_mass.get()))
        self.entry_mass.config(to=self.max_mass, state=NORMAL)
        return self.max_mass

    def length_entry(self):
        """adjusts the max value for length"""
        if self.unit_length.get() == "cm":
            self.max_length = 215
        elif self.unit_length.get() == "inches":
            self.max_length = 84
        self.length_text.set("\nEnter your height in %s"
                             % (self.unit_length.get()))
        self.entry_length.config(to=self.max_length, state=NORMAL)
        return self.max_length

    def percent(self):
        percent_speed = ((self.speed,get() / self.c) * 100)
        return percent_speed

    def process(self):
        """calculates the results"""
        if self.c == 1 or self.max_mass == 1 or self.max_length == 1:
            self.text_results.set("Please select units for all categories.")
            self.label_results.config(bg="red")
        else:
            try:
                gamma = Decimal(1 / Decimal(sqrt(1 - ((self.speed.get() / self.c) ** 2))))
                if (self.mass.get() * gamma) == self.mass.get() \
                        and (self.length.get() / gamma) == self.length.get() \
                        and (1 * gamma) == 1:
                    self.text_results.set("You're not moving fast enough to display changes.")
                    self.label_results.config(bg="red")
                else:
                    self.text_results.set("You are travelling at %s percent the speed of light.\n"
                                          % (format("{0:.2f}".format((self.speed.get() / self.c) * 100))) +
                                          "According to Special Relativity:\n" +
                                          "Your mass is now %s %s;\n"
                                          % ((self.mass.get() * gamma), self.unit_mass.get()) +
                                          "If you travel lying down in the direction of movement,\n" +
                                          "to someone not moving your height is now %s %s;\n"
                                          % ((self.length.get() / gamma), self.unit_length.get()) +
                                          "1 year to you is %s years to someone not moving."
                                          % (1 * gamma))
                    self.label_results.config(bg="white")
            except ZeroDivisionError:
                self.text_results.set("Speed too close to the speed of light, does not compute.")
                self.label_results.config(bg="red")

    def text_factor(self):
        """displays the lorentz factor info window"""
        factor_window = Toplevel()
        factor_window.title("About the Lorentz Transformation")
        text_factor = "The transformations describe how measurements related to events "\
                      + "in space and time by two observers, in inertial frames moving "\
                      + "at constant velocity with respect to each other, are related. "\
                      + "They reflect the fact that observers moving at different velocities "\
                      + "may measure different distances, elapsed times, "\
                      + "and even different orderings of events. (Wikipedia)"
        msg_factor = Message(factor_window,
                             justify=CENTER,
                             padx=20,
                             pady=20,
                             text=text_factor)
        msg_factor.pack()
        button_factor = Button(factor_window,
                               text="Close",
                               command=factor_window.destroy).pack()

    def text_program(self):
        """displays the program info window"""
        program_window = Toplevel()
        program_window.title("About this Program")
        text_program = "This program calculates some of the effects "\
                       + "of Einstein's Theory of Special Relativity. "\
                       + "It was written in Python 2 in November 2015 by Simon Lachaine."
        msg_program = Message(program_window,
                              justify=CENTER,
                              padx=20,
                              pady=20,
                              text=text_program)
        msg_program.pack()
        button_program = Button(program_window, text="Close", command=program_window.destroy).pack()


def __main__():
    """main program"""
    root = Tk()
    app = Application(root)
    root.mainloop()


if __name__ == __main__():
    __main__()
