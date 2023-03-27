####################################################
#   This Script renamed files in path "directory"  #
#            Made by Maksym Tsybulskyi             #
#                    3.2023                        #
####################################################
import os
import sys
directory = r'C:\Users\smoke\Pictures\magma\new'

for subdir, dirs, files in os.walk(directory):
    print('')
    print('-------------------------------------------')
    i = 1
    for filename in files:
        if filename.find('.JPG') > 0:
            newfilename = subdir.split("\\")[-1] + '_' + str(i) + '.JPG'
            print(os.path.join(subdir, filename))
            print(os.path.join(subdir, newfilename))
            print(filename + " > " +newfilename)
            try:
                os.rename(os.path.join(subdir, filename), os.path.join(subdir, newfilename))  # rename your file
            except Exception as E:
                print(E)
            i += 1
