#!/usr/bin/env python3
from numpy.testing._private.utils import HAS_REFCOUNT
import pandas as pd

# use following lines to write to file instead of rendering to a window
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

def main():
    # output excel
    excel_file = './lab37_excelAndPandas/movies.xls'

    # create a dataframe (DF) object.
    movies = pd.read_excel(excel_file)
    # show the first five rows of your DF
    # DF has 5 rows and 24 columns (indexed by integer)
    print(movies.head())

    # read sheet 0
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, skiprows=10)
    print(movies_sheet1.head())

    movies_sheet2 =pd.read_excel(excel_file, sheet_name = 1, skiprows=10)
    print(movies_sheet2.head())

    movies_sheet3 =pd.read_excel(excel_file, sheet_name = 2, skiprows=10)
    print(movies_sheet3.head())

    # combine all DFs into a single DF called movies
    movies = pd.concat([movies, movies_sheet2, movies_sheet3])
    # number of rows and columns ()
    print(movies.shape)

    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)
    print(sorted_by_gross.head(10))

    sorted_by_gross["Gross Earnings"].head(10).plot(kind="barh")
    plt.savefig("stackedbar.pdf", bbox_inches = 'tight')
    sorted_by_gross.to_excel("myExcel.xls")

if __name__ == "__main__":
    main()