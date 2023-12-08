#Convert a txt file into a csv file. 


import os
import pandas as pd


read_file1 = pd.read_csv('TAD_Genomic_Length_of_genes.txt', sep='\t', names=['TAD_ID', 'Genomic length of genes'])
read_file1.to_csv('../Final_Data_for_spreadsheet_csv/TAD_Genomic_Length.csv', sep=',' , index=None )
