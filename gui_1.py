import pymysql
from tkinter import *
from tkinter.messagebox import *
import Pmw

import numpy as np
import random
import scipy
import scipy.integrate as integrate
from scipy.optimize import optimize

import sympy
from sympy import symbols, diff
import matplotlib.pyplot as plt

from numpy.polynomial import polynomial as poly


class QueryWindow(Frame):
    """GUI DB Query Frame"""

    def __init__(self):
        """QueryWindow constructor"""

        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand = YES, fill = BOTH)
        self.master.title(\
            "Enter Query, Click submit to see results.")
        self.master.geometry("600x600")

        # scrolled text pane for query string
        self.query = Pmw.ScrolledText(self, text_height = 5)
        self.query.pack(fill = X)

        #button to submit query
        self.submit = Button(self, text = "Submit Query",
                             command = self.submitQuery)
        self.submit.pack(padx = 10,pady = 10, side = LEFT)

        #button to reset
        self.reset = Button(self, text="Reset", command = self.resetQuery)
        self.reset.pack(padx = 10,pady = 10, side = LEFT)
        #button
        self.help = Button(self,text="Help")
        self.help.pack(padx = 10,pady = 10,side = LEFT)
        
        # Frame to display query results
        self.frame = Pmw.ScrolledFrame(self,
                                       hscrollmode="static",vscrollmode="static")
        self.frame.pack(expand = YES, fill = BOTH)

        self.panes = Pmw.PanedWidget(self.frame.interior(),
                                     orient = "vertical")
        self.panes.pack(expand = YES, fill = BOTH)
        
    def resetQuery(self):
        self.panes.destroy()
        self.panes = Pmw.PanedWidget(self.frame.interior(),
                                    orient = "horizontal")
        self.panes.pack(expand = YES, fill = BOTH)
        self.query.delete('1.0', END)   
        
    def submitQuery(self):
        """Execute user enterd Query"""
        #open connection, retrieve cursor and execute query

        try:
            connection = pymysql.connect(host='localhost', user='root',
                                         password='user', db='Banking',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

            cursor = connection.cursor()
            cursor.execute(self.query.get())
        except (pymysql.OperationalError):
            errorMessage = "Error"
            showerror("Error", errorMessage)
            return

        else:   
            data = cursor.fetchall()
            fields = cursor.description
            cursor.close()
            connection.close()



        self.panes.destroy()
        self.panes = Pmw.PanedWidget(self.frame.interior(),
                                    orient = "horizontal")
        self.panes.pack(expand = YES, fill = BOTH)

        for item in fields:

            self.panes.add(item[0])
            label = Label(self.panes.pane(item[0]),
                          text = item[0], relief = RAISED)
            label.pack(fill = X)

        
        for entry in data:

            for i in range(len(entry)):

                label = Label(self.panes.pane(fields[i][0]),
                              text = entry[fields[i][0]], anchor = W, 
                              relief = GROOVE, bg = "white")
                label.pack(fill = X)

            self.panes.setnaturalsize()

def main():
    QueryWindow().mainloop()

main()
