#!/usr/bin/env python3

#Procedure for calculating number of Hbonds from .gro coord file

import math
import sys

#open the coordinate.gro file to read

file = open(sys.argv[0],'rt')

#make empty list of 'total_hbonds', each entry is an int object for a different residue
total_hbonds = []
#make variable 'hbond_length', distance between 2 h-beads
hbond_length = 0.28
#make variable 'nmol', total number of residues
nmol = 100
#name of hbonding beads in question
hbonding_bead_1 = "c2"
hbonding_bead_2 = "c4"
hbonding_bead_3= "c6"
hbonding_bead_4 = "c8"
hbonding_bead_5 = "c10"
hbonding_bead_6 = "c12"


#function to break down file into large list
grofile = []
for line in file: 
   line_words = line.split( )
   for word in line_words:
      grofile.append(word)
      
      
      
      
#given only one object on the first 2 lines
#after each line is res#, resname, at.name, at.#, position (x,y,z), velocity (x,y,z)
#lets break down big list grofile into smaller lists
#first remove the first 2 entries to give just coordinate info
gro_info = [grofile[2:]]





#then to create list of each set of variables
res_numbers = [gro_info[range(0,10*nmol,10)]]
res_number_list = [float(v) for v in res_numbers]
res_names = [gro_info[range(1,10*nmol,10)]]
res_name_list = [str(v) for v in res_names]
bead_names = [gro_info[range(3,10*nmol,10)]]
bead_name_list = [str(v) for v in bead_names]
xs = [gro_info[range(5,10*nmol,10)]]
x_list = [float(v) for v in xs]
ys = [gro_info[range(6,10*nmol,10)]]
y_list = [float(v) for v in xs]
zs = [gro_info[range(7,10*nmol,10)]]
z_list = [float(v) for v in zs]
#now have lists of all variables ordered as in .gro file to draw from. Careful! They are mutable.








#finds # of hbonds for each residue
search_hbonds()
#sum all ints from 'total_hbonds' to give final value
sample_hbonds = sum(total_hbonds)
print('The total number hbeads hydrogen bonded at a radius of less than', str(hbond_length), 'is', str(sample_hbonds))
#close the coordinate.gro file
file.close()















#function to find hbonds
def search_hbonds():
#make variable 'hbonds', how many hbonds for residue1
   hbonds = 0
   current_residue = 1
   bead_number = 0
   next_bead = 1
   if current_residue <= nmol:
#search to create 3 variables 'x1' 'y1' 'z1' from a h-bead on a residue
      if res_numbers_list[bead_number] == current_residue:
         next_residue = current_residue + 1
         current_bead_search()
#search file to find a different residue # and h-bead and create 3 variables 'x2' 'y2' 'z2'
         if next_residue <= nmol:
             if res_numbers_list[next_bead] == next_residue:
               next_bond_search(x1,y1,z1)
             else: 
               next_residue = next_residue + 1
         else: 
           pass
      else:
#when all residues searched for the residue in question add 'hbond' to the list 'total_hbonds'
        total_hbonds.append(hbonds)
#restart search algorithm from residue+1
        current_residue = current_residue + 1
   else:
      pass







#function to find first hbonding bead and produce coordinates
def current_bead_search():
    if bead_name_list[bead_number] ==  hbonding_bead_1 or  hbonding_bead_2 or hbonding_bead_3 or hbonding_bead_4 or hbonding_bead_5 or hbonding_bead_6:
      x1 = float(x_list[bead_number])
      y1 = float(y_list[bead_number])
      z1 = float(z_list[bead_number])
      bead_number = bead_number + 1
    else:
      bead_number = bead_number + 1







#function to search another residue for hbonding beads and check with last bead
def next_bond_search(x1,y1,z1):
    if bead_name_list[next_bead] == hbonding_bead_1 or hbonding_bead_2 or hbonding_bead_3 or hbonding_bead_4 or hbonding_bead_5 or hbonding_bead_6:
      x2 = float(x_list[next_bead])
      y2 = float(y_list[next_bead])
      z2 = float(z_list[next_bead])
#uses pythagoras to workout the distance
      pythag(x1,x2,y1,y2,z1,z2)
#if 'bond_length' =< 'hbond_length', 'hbond' +1
      is_hbond(bond_length)
      next_bead = next_bead + 1
#add 1 to the value of secondary residue and repeat search
    else:
      next_bead = next_bead + 1







#function to calculate 'bond_length'
def pythag(x1,x2,y1,y2,z1,z2):
   rx = x1 - x2
   ry = y1 - y2
   rz = z1 - z2
   total = (rx ** 2) + (ry ** 2) + (rz ** 2)
   bond_length = sqrt(total)







#function for if 'bond-length' =< 'hbond_length', 'hbond' +1
def is_hbond(bond_length):
    if bond_length <=  hbond_length:
      h_bonds = h_bonds + 1
    else: 
      pass







