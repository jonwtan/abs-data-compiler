# credit goes to 'Adam Zalcman' & others at Stackoverflow for some code tips.
# When running this file, you need to have pandas & its dependencies installed. As of this version, this .py file must be in the same folder as the csv files you want to input
# USER INPUT: Lines 10, 13, 24

import glob
import csv
import pandas as pd


output_file = "C:/../ABS Data Compiler/SampleOutput/MelbournePopulation.csv"       # TO USER: enter the address of the output file to create

outfile = open(output_file, 'w')
outfile.write("Suburb , 2011, 2012, 2013, 2014 , 2015 , 2016 , 2017 \n")		   # TO USER: Enter fields in this file. This is the .csv's header

for filename in glob.glob('*.csv'):											# goes through each .csv file to input in the folder

	if filename == output_file: 											# Skips the file we're writing
		continue
		
	# creates dataframe 'X' from input csv file, assigns columns, and creates new dataframe 'Y' with only the measure you want
	X = pd.read_csv(filename, encoding = "latin1")							
	X.columns = ["Time", "Value", "Measure", "Description"]
	
	Y = X.loc[ X["Measure"] == "ERP_P_20" ]								# TO USER: Replace 'ERP_P_20' with the key/measure you want
	
	# edits the filename to remove the word '.csv' before writing into csv output file
	filename = filename.replace(".csv", "")
	outfile.write("%s ," % filename)
	
	# writes each element into the csv output file, plus a comma to separate it. Once done, it goes to the next line
	for a in Y["Value"]:
		outfile.write("%d ," % a)
	
	outfile.write("\n")
	

outfile.close()
