"""
Advent of code - Day 7

Key points:
* recursivity 
* OOP
"""


import re
import numpy as np 
import pandas as pd


#=============================== Class ===============================


# Filesystem class
class FileSystem():
    def __init__(self):
        self.filesystem = {}
        self.working_dir_path = []
        self.working_dir = self.filesystem

    def parse_command(self, cmd):
        cmd = cmd.split('\n')
        if cmd[0] == 'ls':   self.parse_content(cmd[1:])
        else:                self.change_dir(cmd[0][3:])

    def parse_content(self, content):
        for c in content:
            e1, e2 = c.split(' ')
            if e1 == 'dir':  self.create_dir(e2)
            else:            self.create_file(e2, int(e1))

    def create_dir(self, name):
        self.working_dir[name] = {}

    def create_file(self, name, size):
        self.working_dir[name] = size

    def set_working_dir(self, path):
        self.working_dir = self.filesystem
        for e in path:
            self.working_dir = self.working_dir[e]
                
    def change_dir(self, dir):
        if dir == '..':   del self.working_dir_path[-1]
        else:             self.working_dir_path.append(dir)
        self.set_working_dir(self.working_dir_path)

    def list_all_folders(self, dir=None, full_path=''):
        # Starting point
        if dir is None:
            dir = self.filesystem

        # Check content
        subfolders = [(k,v) for k,v in dir.items() if isinstance(v, dict)]

        # Stop condition : no more subfolder so return complete path
        if len(subfolders) == 0: return [full_path]
        
        # Else get all subfolders
        else: return [full_path] + [j for i in [self.list_all_folders(s[1], f'{full_path}/{s[0]}') for s in subfolders] for j in i]

    def compute_folder_size(self, dir):
        # Stop condition : its a file
        if isinstance(dir, int): return dir
        # Else compute all items size
        else: return np.sum([self.compute_folder_size(v) for k,v in dir.items()])

    def compute_all_folder_size(self):
        def name_to_dir(folder):
            path = folder.split('/')[1:]
            dir = self.filesystem
            for e in path:
                dir = dir[e]
            return dir

        return {i:self.compute_folder_size(name_to_dir(i)) for i in self.list_all_folders()}


#=============================== Data ===============================


# Open data
with open('./data/day7.txt', 'r') as file:
    raw = file.read()

# Parse command
commands = re.split('\n\$ ', raw)[1:]

file_system = FileSystem()

for cmd in commands:
    file_system.parse_command(cmd)

file_system.filesystem


#=============================== First module ===============================


# Compute folder size
folder_size = file_system.compute_all_folder_size()

# Keep only <100000
filtered_folder_size = [size for _, size in folder_size.items() if size < 100000]

# Display sum
print(f'Sum of total size of <100000 directories: {np.sum(filtered_folder_size)}')


#=============================== Second module ===============================


# Compute free space
free_space = 70000000 - file_system.compute_folder_size(file_system.filesystem)

# Space to clean
space_to_clean = 30000000 - free_space

# Filter on folder big enough
big_enough = {k:v for k,v in folder_size.items() if v > space_to_clean}

# Find the smallest
to_delete = np.min([v for _,v in big_enough.items()])

# Display folder to delete
print(f'Size of the folder to delete: {to_delete}')