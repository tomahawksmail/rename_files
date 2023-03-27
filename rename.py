#
# This Script renamed files
# Made by Maksym Tsybulskyi
# 3.2023
#
# import shutil
import os
import sys
# directory = r'C:\Users\smoke\Pictures\magma\new\Klarity Kratom\Capsules'
directory = r'C:\Users\smoke\Pictures\magma\new'

for subdir, dirs, files in os.walk(directory):
    subdirectoryPath = os.path.relpath(subdir, directory)
    if not os.path.isdir(subdirectoryPath):
        print('')
        print('-------------------------------------------')
        i = 1
        for filename in files:
            if filename.find('.JPG') > 0:
                newfilename = subdirectoryPath.split("\\")[-1] +'_'+ str(i) + '.JPG'
                # newfilename = filename + " > " + newfilename
                # print("newfilename = " + newfilename) # print new file name converting
                print(os.path.abspath(newfilename))







    #
                # old_path_string = os.path.join(directory, filename)
                # new_path_string = os.path.join(directory, newfilename)
                # print(old_path_string) # print full old path
                # print(new_path_string)  # print full new path
    #             try:
    #                 os.rename(old_path_string, new_path_string)  # rename your file
    #             except Exception as E:
    #                 print(E)
            i+=1
