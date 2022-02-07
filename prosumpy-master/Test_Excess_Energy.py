# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:32:44 2022

@author: Dell
"""


from prosumpy import dispatch as dis
from prosumpy import analysis as an
from prosumpy import plot as pl
import pandas as pd

demand = pd.read_csv('tests/data/demand_example.csv', index_col=0, header=None, 
                     parse_dates=True, squeeze=True)
pv_1kW = pd.read_csv('tests/data/pv_example.csv', index_col=0, header=None, 
                     parse_dates=True, squeeze=True)


pv_size = 10

param_tech = {'BatteryCapacity': 20,
              'BatteryEfficiency': .9,
              'InverterEfficiency': .85,
              'timestep': .25,
              'MaxPower': 20
             }

pv = pv_1kW * pv_size

E1 = dis.dispatch_max_sc(pv, demand, param_tech, return_series=False)

print(E1.keys())

an.print_analysis(pv, demand, param_tech, E1)
pl.plot_dispatch(pv, demand, E1, week=18)