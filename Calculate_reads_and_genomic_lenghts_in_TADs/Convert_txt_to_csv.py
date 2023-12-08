#Convert a txt file into a csv file. 


import os
import pandas as pd


read_file1 = pd.read_csv('TADs_Reads_LacZ_rep1.txt', sep='\t', names=['TAD_ID', 'Reads'])
read_file1.to_csv('./Final_Data_for_spreadsheet_csv/TADs_Reads_LacZ_rep1.csv', index=None, sep=',')
 
read_file2 = pd.read_csv('TADs_Reads_LacZ_rep2.txt', sep='\t', names=['TAD_ID', 'Reads'])
read_file2.to_csv('./Final_Data_for_spreadsheet_csv/TADs_Reads_LacZ_rep2.csv', index=None, sep=',')

read_file3 = pd.read_csv('TADs_Reads_Lam_rep1.txt', sep='\t', names=['TAD_ID', 'Reads'])
read_file3.to_csv('./Final_Data_for_spreadsheet_csv/TADs_Reads_Lam_rep1.csv', index=None, sep=',')

read_file4 = pd.read_csv('TADs_Reads_Lam_rep2.txt', sep='\t',  names=['TAD_ID', 'Reads'])
read_file4.to_csv('./Final_Data_for_spreadsheet_csv/TADs_Reads_Lam_rep2.csv', index=None, sep=',')
