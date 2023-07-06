# Packages: in general packages are the folders containing sub_folders and furthers files.
# through pakages we can access modules present in some other folders
# for a folder to be a pacakage it is compulsory to contain one __init__.py file which is empty file
# every sub floder also contain init file and further files

# import the package and its sub package along with the module
import Package_1.subpac1.greet
import Package_1.subpac2.quote
import Package_1.wlcm

# using the function of modules
Package_1.subpac1.greet.grt() # accesing the grt function
Package_1.subpac2.quote.qut() # accessing the qut funciton of subpac2 package
Package_1.wlcm.welcome()
print(Package_1.subpac1.greet.aa)
