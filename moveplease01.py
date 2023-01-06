#!/usr/bin/env python3

"""A simple script to move two files into ceph_storage/
   Alta3 Research | rzfeeser@alta3.com"""

 # standard libraries to use an os or play around with files
import shutil
import os

def main():
    # set this to start in this directory
    os.chdir('/home/student/mycode/')
    
    # Move raynor file to ceph_storage
    shutil.move('raynor.obj', 'ceph_storage/')
    
    # allowing the user to choose new file name
    xname = input('What is the new name for kerrigan.obj? ')

    # move newly name file 
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)










if __name__ == "__main__":
    main()
