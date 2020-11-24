'''
Image converter from JPEG to PNG or EPS format
Description:
The code converts all the .jpg files in a provided source folder into .png or .eps format and storages
them in a target folder. If target folder doesn´t exist, it'll be created.
Script execution meant to be in the terminal:
JPEG to PNG: python3 JPEG2PNG.py images\directory\name new\directory\name
JPEG to EPS: python3 JPEG2PNG.py images\directory\name new\directory\name True/1
'''

import sys
import os
from PIL import Image

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            raise Exception('Please insert source and target folders.')

        if os.path.exists(sys.argv[1]):
            cwd = sys.argv[1]
        else:
            print('The source folder doen´t exist.')

        if len(sys.argv) >= 3:
            new_cwd = sys.argv[2]
            eps_enable = False
        else:
            raise Exception('Target folder was not provided.')

        if len(sys.argv) >= 4:
            eps_enable = bool(sys.argv[3])

    except Exception as error:
        print(f'Error: {error}')
        sys.exit(1)

    if not os.path.exists(sys.argv[2]):
        print('Creating new target folder...')
        os.mkdir(sys.argv[2])
    else:
        print('Converting files...')

    for file in os.listdir(cwd):
        filenames = os.path.splitext(file)
        if filenames[1] == '.jpg' or filenames[1] == '.JPG' or filenames[1] == '.eps':
            img = Image.open(f'{cwd}/{file}')
            cleanName = filenames[0]
            if eps_enable:
                img.save(f'{new_cwd}/{cleanName}.eps', 'EPS')

            else:
                img.save(f'{new_cwd}/{cleanName}.png', 'PNG')
    print('Successful convertion!')