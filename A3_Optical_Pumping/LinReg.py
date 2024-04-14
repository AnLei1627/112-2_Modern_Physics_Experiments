import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv


class LinReg:
    def __init__(self, csv_filename):
        self.filename = csv_filename
        self.xs = []
        self.ys = []
        self.intercept = 0.
        self.slope = 0.
        self.title = ''
        self.header = ['','']
        self.unit = ['','']
        with open(self.filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            self.title = next(reader)[0]
            self.header = next(reader)
            self.unit = next(reader)
            for row in reader:
                self.xs.append(float(row[0]))
                self.ys.append(float(row[1]))

        f = lambda x, a, b: a * x + b
        popt, pcov = curve_fit(f, self.xs, self.ys)
        self.xs_fit = np.array([self.xs[0],self.xs[-1]])
        self.ys_fit = popt[0] * self.xs_fit + popt[1]
        self.slope = popt[0]
        self.intercept = popt[1]

    # def plot_line(self, ax, range = None):

    #     ax.plot(xs_fit, ys_fit, color = 'r', linestyle='--',
    #             label=f'slope: {popt[0]:0.3e} \nintercept: {popt[1]:0.3e} ')
        

    def plot(self, origin=True):
        fig, ax = plt.subplots(1,1,figsize=(8,6))
        ax.set_title(self.title)

        ax.set_xlabel(rf'{self.header[0]} ({self.unit[0]})')
        ax.set_ylabel(rf'{self.header[1]} ({self.unit[1]})')
        ax.grid()
        ax.scatter(self.xs, self.ys, label='data')
        if origin:
            ax.set_xlim(0)
            ax.set_ylim(0)
        ax.plot(self.xs_fit, self.ys_fit, color = 'r', linestyle='-.',label=f'slope: {self.slope:0.3e} \nintercept: {self.intercept:0.3e} ')
        plt.legend()