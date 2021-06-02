#-------------------------------------------------------------------------------
# Name:        Vendor Profiling ( Prototype for Plastic Sheet)
# Purpose:
#
# Author:      Shahazureen Ikwan
#
# Created:     29/01/2020
# Copyright:   (c) ILLEGEAR LAGUNA 2020
# Licence:     :)
#-------------------------------------------------------------------------------


import pandas
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

# Load The Dataset
data = "Vendor(Plastic).csv"
names = ['COMPANY','TYPE','ADDRESS','EMAIL','PHONE NO.','FAX NO.', 'H/P NO.',
        'NAME','POSITION','REMARKS','PROFIT']
dataset = pandas.read_csv(data)

# Make Array of the data
array = dataset.to_numpy()
Company = array[1:,1]

print(Company)