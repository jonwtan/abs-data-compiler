Python compiler for aggreggating specific data from the Australian Bureau of Statistics (ABS) .csv datafiles of statistical areas.
by J. Tan

The ABS provides CSV datafiles for almost every local statistical area, with a rich amount of data. Statistics include population by age, gender, total population, number of businesses, income, and over several hundred fields for particular years too numerous to list.
This large amount of data can mean that obtaining specific fields for a particular aggregated area... say the yearly population for statistical areas in the state of Victoria, or the number of businesses per statistical area in the Adelaide region... can be tedious. This Python script aims to simplify the process by automating it, and producing a CSV output file which can then be used for analytics.


++ HOW IT WORKS ++ :

When executed, the python script takes all CSV datafiles contained in the same folder, & produces an output CSV file with the compiled statistical field.
Alternatively, instead of running the Python script/file via command prompt, one can use the Jupyter .ipynb notebook.


++ INCLUDED IN THIS GITHUB ++ :

1) "SampleOutput" folder = Contains two examples of compiled output CSV files, in this case... the yearly total population of selected statistical areas in the Melbourne Metropolitan Area, and yearly total of passenger vehicles of selected areas in the Melbourne Metropolitan Area

2) "Sample ABS Datafiles and Script" folder:
Contains;
(i)   Python file (filemaker.py).
(ii)  Jupyter notebook file & folder. These can alternatively be used instead of running the Python file.
(iii) CSV datafiles of selected statistical areas in the Melbourne region.

3) Readme.txt


++ REQUIREMENTS ++ :

1. Python 3
2. Pandas Python data science package & dependencies
3. Anaconda/Miniconda terminal
4. (Optional) Jupyter notebook & related packages (if one wishes to use the .ipynb notebook)


++ INSTRUCTIONS ++ :

1. Download this Github package onto the computer. It is assumed the user has the requirements above installed.
2. Create a folder named "Output". This is where the compiled CSV output file will be created & written to.
3. Create a folder called "Input". This is where the input CSV datafiles from the ABS, and where the Python file and/or Jupyter file will be placed.
4. Into the folder "Input", copy the .CSV datafiles from the ABS to be compiled.
5. Into the folder "Input", copy the Python file "filemaker.py". Alternatively, the .ipynb file & corresponding folder can be copied instead if one wishes to use the Jupyter notebook.


6. In the "Input" folder, open one of the .csv datafiles with Microsoft Excel or similar spreadsheet software.
Find the 'Measure' key for the statistic to be compiled, and the years that data is available for.

7. Open the Python file "filemaker.py", or Jupyter file "filemaker.ipynb". Edit the following lines that are flagged with the comment "# TO USER: ..." :

a) The pathname of the output CSV file to be created
b) The fields containing the suburb & available years, that will be in the output CSV file.
c) The key/measure to be compiled.
   (example: 'ERP_P_20' for total resident population, 'MVC_14' for number of vehicles)


8. Save the Python file, or Jupyter file.

9. Run the Python file, or Juypter cells.

10. The created compiled CSV output file should be in the "Output" folder.

   
++ IMPORTANT ++

1. It is best practice to have the compiled output CSV files in a separate folder.
2. Ensure the input folder contains only ABS .CSV datafiles to be compiled. Improper .csv files may cause the Python script/Juypter notebook to create an error when executed.



++ DISCLAIMER ++

The scripts contain no malicious code. The author however is absolved of any responsibility for any unintended effects to the user's system or anything else.

