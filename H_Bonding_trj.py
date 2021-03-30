#!/usr/bin/env python
# coding: utf-8

# # HBonding 
# 1) Input Opens .gro file
# 2) Using coordinates, which beads hydrogen bonding 
# 3) If they shorter than length____ and have abno

# In[35]:


#!/usr/bin/env python3

#Procedure for calculating number of Hbonds from .gro coord file

import math
import sys
import pandas as pd
import numpy as np
import os
from itertools import combinations
import subprocess as sp
import argparse
import statistics


def readin_gro(grofile):
    ##finish command read in
    # print("hello",grotype )
    #grotype=="coord":
    #    COMMAND = '''awk '{print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6 }'''+grofile+''' > ./tst.gro'''
        # COMMAND = '''awk '{print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6 }' ./MARTINI_500.gro > ./MARTINI_500_reformat.gro'''
    #    sp.call(COMMAND, shell=True)
        #open the coordinate.gro file to read
    #    file_df=pd.read_table("./tst.gro", delim_whitespace=True,skipfooter=1, skiprows=2, header=None,  error_bad_lines=False,names=["residue","beadname","bead_num","coord_x","coord_y","coord_z"] )
    #    print(file_df.head())
    total_beads = int
    total_beads = 11600
    
    COMMAND = '''awk '{print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6 }'''+grofile+''' > ./tst.gro'''
    sp.call(COMMAND, shell=True)
    trj_skip = int
    trj_skip = 2+(total_beads+3)*trj_step
    #open the coordinate.gro file to read
    file_df=pd.read_table("./tst.gro", delim_whitespace=True, skiprows=trj_skip, nrows=total_beads, header=None,  error_bad_lines=False,names=["residue","beadname","bead_num","coord_x","coord_y","coord_z"] )
    print(file_df.head())
    return(file_df)


def readcoordinates(file_df,beadlist):
    ###filter input
    file_df_sub=file_df[file_df["beadname"].isin(beadlist)]

    #Remove Alt residue name 
    file_df_sub['residue']=file_df_sub['residue'].str.split("Alt").str.get(0)

    #make variable 'hbond_length', distance between 2 h-beads
    hbond_length = 0.28
    #make variable 'nmol', total number of residues
    nmol = 100

    file_df_sub_head=file_df_sub.head(n=100)


    # cc=[]
    # for index,row in file_df_sub_head.iterrows():
    #     for index,row in file_df_sub_head.iterrows():
    #         if row 
    #         cc.append(index)


    cc = list(combinations(file_df_sub_head.index,2))
    # out = pd.DataFrame([file_df_test[["coord_x","coord_y","coord_z"]].loc[c,:].sum() for c in cc], index=cc)
    out = pd.DataFrame([(file_df_sub_head[["coord_x","coord_y","coord_z"]].loc[c[0],:] - file_df_sub[["coord_x","coord_y","coord_z"]].loc[c[1],:])for c in cc] , index=cc)
    out["coord_x"]=out["coord_x"]**2
    out["coord_y"]=out["coord_y"]**2
    out["coord_z"]=out["coord_z"]**2
    out["bond_length"] = np.sqrt(out.sum(axis=1))

    #sum all ints from 'total_hbonds' to give final value
    sample_hbonds = sum( out["bond_length"] < hbond_length )
    print('The total number hbeads hydrogen bonded at a radius of less than', str(hbond_length), 'is', str(sample_hbonds), 'at this step')
    #close the coordinate.gro file
    print(out.head())
        
    
def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--grofile', type=str, required=True, help="Location of the gro file")
    parser.add_argument('--beadlist', type=list, default=["c2","c4","c6","c8","c10","c12"], help="List of chosen beads")


    args = parser.parse_args()

    print('If you are reading this you are not a total bozo - at least you have provided all the parameters')

    global trj_step
    trj_step = int
    trj_step = 0
    hbonds_list=[]
    global trj_confs
    trj_confs = int
    trj_confs = 250
    
    if trj_step <= trj_confs:
        readcoordinates(beadlist=args.beadlist, file_df=readin_gro(args.grofile))
        hbonds_list = hbonds_list.append(sample_hbonds)
        trj_step = trj_step + 1
        
    else:
        average_hbonds=sum(hbonds_list)/trj_confs
        deviation=statistics.stdev(hbonds_list)
        print('The average number of hydrogen bonds at a radius of less than', str(hbond_length), 'is', str(average_hbonds), 'with a standard deviation of', str(deviation))       

  

             

if __name__ == "__main__":
   main(sys.argv[1:])
