import os, sys

if len(sys.argv) != 2:
    print("Folder name not given as an argument")
    exit()

 
directory_name = sys.argv[1]
directory_path = os.path.join(os.path.dirname(sys.argv[0]), directory_name) 

print(directory_path)

i = 1

for filename in os.listdir(directory_path):
    extension = filename.split('.')[-1]
    old_filename_path = os.path.join(directory_path, filename)
    new_filename_path = os.path.join(directory_path, directory_name + str(i) + '.' + extension)
    print('Renaming', old_filename_path, 'to', new_filename_path)
    os.rename(old_filename_path, new_filename_path)
    i += 1

