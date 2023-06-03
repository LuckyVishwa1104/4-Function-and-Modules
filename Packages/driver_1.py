# Packages: in general packages are the folders containing sub_folders and furthers files.
# for a folder it is compulsory to contain one __init__.py file it is empty file
# every sub floder also contain init file and further files

# imoert the package and its sub package along with the module
import Package_1.subpac1.greet
import Package_1.subpac2.quote
# using the function of modules
Package_1.subpac1.greet.grt()
Package_1.subpac2.quote.qut()