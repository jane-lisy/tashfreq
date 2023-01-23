#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert any xlsx to csv
"""

import glob
import pandas as pd
import re

filenames = glob.glob('texts/*.xlsx')

for filename in filenames:
    df = pd.read_excel(filename)
    print(df.shape)
    csv_filename = re.sub('xlsx', 'csv', filename)
    df.to_csv(csv_filename, index = False)
