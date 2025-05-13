#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:18:51 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "IOM CREATE"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/25-IOM-GLO-1 - Raw_dataset"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/25-IOM-GLO-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

enumerator_name = 'Enumerator Name'
# Original column name for respondents' names (for anonymisation and duplicate removal)

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['start','end','start-geopoint','_start-geopoint_latitude','_start-geopoint_longitude','_start-geopoint_altitude',
'_start-geopoint_precision','today','username','deviceid','phonenumber',
 '1', '2-1', 'E1', '2-2', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7',
 '3', '4', '5', '6', '7', '7-o', '8', '8-o', '9-e', '9-e-o', '9-p', '9-p-o', '10', '11', '11-o',
 '12', '13', '14', '15', '16', '17', '18', 'omit1', '19', '19-o', '20', '21', '22-a-a',
 '22-a-1', '22-a-2', '22-a-3', '22-a-4', '22-a-5', '22-a-6', '22-a-7', '22-a-8','22-a-9', '22-a-o',
 '22-b-a', '22-b-1','22-b-2','22-b-3', '22-b-4', '22-b-5', '22-b-6', '22-b-7', '22-b-8', '22-b-9', '22-b-10', '22-b-o',
 '23', '24', '24-o', '25', '26', '27-a', '27-1', '27-2', '27-3', '27-4', '27-5', '27-6', '27-7', '27-o',
 '28-a', '28-1', '28-2', '28-3', '28-4', '28-5', '28-6', '28-7', '28-8', '28-9', '28-o',
 '29', '30-a','30-1', '30-2','30-3', '30-4', '30-5', '30-6', '30-7', '30-o',
 '31', '32', '33', '33-o', '34', '35', 'omit2', '36', '37', '38-a', '38-1', '38-2', '38-3', '38-4', '38-5', '38-6', '38-7', '38-o',
 '39-a', '39-1', '39-2', '39-3', '39-4', '39-5', '39-6', '39-o', '40', '41', '42-e-a', 
 '42-e-1', '42-e-2', '42-e-3', '42-e-4', '42-e-5', '42-p-a', '42-p-1', '42-p-2', '42-p-3', '42-p-4', '42-p-5','42-p-o',
 '43', '44', '44-o', '45', '46', '47', '48', '49', '50', '51-a', '51-1', '51-2', '51-3', '51-4', '51-5', '51-6', '51-o',
 '52', '53', '54', '55','56-a','56-1', '56-2', '56-3', '56-4', '56-5', '56-6', '56-o', '57', '57-o', 'omit3',
 '58', '59', '59-o', '60-a', '60-1', '60-2', '60-3', '60-4', '60-5', '60-6', '60-o', '61', '61-o', '62',
 '63-a', '63-1', '63-2', '63-3','63-4', '63-5', '63-6', '63-o', '64', '65', '65-o', '66', '67', '68', '69',
 'omit4', '70', '71', '72', '73-a', '73-1', '73-2', '73-3', '73-4', '73-5', '73-6', '73-o', '74', "75",
 'omit5', '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by', '__version__',
 '_tags', '_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['start','end','start-geopoint','_start-geopoint_latitude','_start-geopoint_longitude','_start-geopoint_altitude',
'_start-geopoint_precision','today','username','deviceid','phonenumber', 'E1', 'E2','E3','E4', 'E5','E6','E7','omit1', '22-a-a',
'22-b-a', '27-a',  '28-a',  '30-a','omit2', '38-a', '39-a', '42-e-a', '42-p-a','51-a', '56-a','omit3','60-a','63-a','omit4',               
'73-a','omit5','_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by', '__version__',
 '_tags', '_index']
# Specify the columns to be excluded from the data analysis

miss_col = ['1','4','5', '13','14','15','16','17','18']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['7-o', '8-o', '9-e-o', '9-p-o', '11-o', '19-o', '22-a-o', '22-b-o','24-o', '27-o', '28-o',
            '30-o', '33-o', '38-o', '39-o', '42-p-o','44-o', '51-o', '56-o','57-o','59-o','60-o','61-o',
            '63-o','65-o','69','73-o','75']
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = '3'
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['13', '14', '15','16', '17','18']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

mango = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, enumerator_name, open_cols, cols_new, age_col, diss_cols, del_type = 0, file_type=file_type)
mango.processing()