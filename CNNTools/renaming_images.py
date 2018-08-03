import os, sys, argparse

# if len(sys.argv) != 2:
#     print("Folder name not given as an argument")
#     exit()

 
# directory_name = sys.argv[1]
# directory_path = os.path.join(os.path.dirname(sys.argv[0]), directory_name) 

# print(directory_path)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='input folder')
parser.add_argument('--start', required=False, default=1, help='start')
parser.add_argument('--base_name', required=False, default='image', help='base name')

args = parser.parse_args()

directory_path = args.input
i = int(args.start)
base_name = args.base_name

filenames = os.listdir(directory_path)

# i = 1
# base_name = 'quaver_ef'

for filename in os.listdir(directory_path):
    extension = filename.split('.')[-1]
    old_filename_path = os.path.join(directory_path, filename)
    print(directory_path)
    new_filename_path = os.path.join(directory_path, base_name + '_' + str(i) + '.' + extension)
    print('Renaming', old_filename_path, 'to', new_filename_path)
    os.rename(old_filename_path, new_filename_path)
    i += 1

