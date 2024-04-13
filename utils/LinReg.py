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

    def plot_line(self, ax, range = None):
        f = lambda x, a, b: a * x + b
        xs = self.xs
        ys = self.ys
        if range:
            xs = self.xs[range[0]:range[1]]
            ys = self.ys[range[0]:range[1]]
        popt, pcov = curve_fit(f, xs, ys)
        # xs_fit = np.sort(np.array([xs[-1], xs[0], -popt[1]/popt[0]]))
        xs_fit = np.array([xs[0],xs[-1]])
        print(10**(-popt[1]/popt[0]))
        ys_fit = popt[0] * xs_fit + popt[1]
        ax.plot(xs_fit, ys_fit, color = 'r', linestyle='--',
                label=f'slope: {popt[0]:0.3e} \nintercept: {popt[1]:0.3e} ')
        

    def plot(self, ax, origin=True):
        # fig, ax = plt.subplots(1,1)
        ax.set_title(self.title)

        ax.set_xlabel(rf'{self.header[0]} [{self.unit[0]}]')
        ax.set_ylabel(rf'{self.header[1]} [{self.unit[1]}]')
        ax.grid()
        ax.scatter(self.xs, self.ys)
        xs_fit = np.array([self.xs[0], self.xs[-1]])
        ys_fit = self.slope * xs_fit + self.intercept
        if origin:
            ax.set_xlim(0)
            ax.set_ylim(0)
        # ax.plot(xs_fit, ys_fit, color = 'r', linestyle='-.',label=f'slope: {self.slope:0.3e} ({self.unit[1]}/{self.unit[0]})\nintercept: {self.intercept:0.3e} ({self.unit[1]})')
        ax.legend()
        # fig.savefig(self.filename[:-4]+'.svg')


# L1 = LinReg('logGlogf.csv')
# fig, ax = plt.subplots(1,1)
# L1.plot_line(ax,range=[0,3])
# L1.plot_line(ax,range=[-10,-1])
# L1.plot(ax, origin=False)
# # ax.set_ylim(-1)
# # ax.set_xlim(-0.5,1.5)
# ax.plot([0,1],[0,0], color='r',linestyle='--')
# ax.set_title('log G - log f graph of High-pass + Low-pass')
# fig.savefig('logGlogf.svg')
        
# linreg = LinReg('shot.csv')
# fig, ax = plt.subplots(1,1)
# linreg.plot_line(ax)
# linreg.plot(ax, origin=False)
# ax.legend()
# fig.savefig('shot.svg')

# linreg = LinReg('calibrator.csv')
# fig, ax = plt.subplots(1,1)
# linreg.plot_line(ax)
# linreg.plot(ax, origin=True)
# ax.legend()
# fig.savefig('calobrator.svg')