import os
import sys
import subprocess

if len(sys.argv) != 3 or sys.argv[2] not in ["360", "480"]:
    print("Usage: python downsize_batch.py folder 360/480")
    sys.exit()

folder = sys.argv[1]
resolution = sys.argv[2]

folder, folders, files = tuple(os.walk(folder))[0]

for movie in files:
    name, extension = os.path.splitext(movie)
    if extension not in ('.mkv', '.mp4', '.avi'):
        continue
    new_name = name + "." + resolution + extension
    print(folder, new_name)
    os.system('./downsize%s.sh "%s" "%s"' % (resolution, os.path.join(folder, movie),
                                       os.path.join(folder, new_name)))
    #subprocess.call(['./downsize.sh', os.path.join(folder, movie),
    #                 os.path.join(folder, new_name)])

