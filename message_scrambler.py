import random
import os
import shutil


def clear_directory(dir_path):
    for existing_file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, existing_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
            
            
def scramble_message(secret: str, newpath: str) -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    asset_relative_path = 'assets'
    asset_path = os.path.join(dir_path, asset_relative_path)

    if not os.path.exists(newpath):
        os.makedirs(newpath)

    f = open('countries.txt', 'r')
    countries = f.readlines()
    random_countries = []
    random_numbers = []

    #  pull a list of random countries to match length of the secret message
    #  create a list of random numbers from 100 to 9000 to match length of the secret message
    i = 0
    while i < len(secret):
        country = countries[random.randint(0, len(countries) - 1)].strip()
        #  if country already exists in our list, try again
        if country in random_countries:
            continue
        random_countries.append(country)
        random_numbers.append(random.randint(100, 9999))
        i += 1

    #  sort the list of random countries
    random_countries.sort()
    #  DO NOT sort the list of random numbers

    #  in another list matching secret message length, store the filename in format of random number + country +
    #  '.png' concatenated with pipe('|') and character + '.png'

    #  reset i and create our list to hold the tuples
    secret_file_names = []
    i = 0

    while i < len(secret):
        str_name_parts = [str(random_numbers[i]), random_countries[i], '.png |', secret[i], '.png']
        file_name_struct = ''.join(str_name_parts)
        secret_file_names.append(file_name_struct)
        i += 1

    #  now all data is where we need it, we can sort the secret_filenames_list.  if we didn't sort before creating
    #  the new files, the recipient could simply sort the files by created date to unscramble the message.  too easy
    secret_file_names.sort()
    
    #  clear the directory of previous message files
    clear_directory(newpath)
    
    #  copy the files now to 'encrypt' our secret message
    for f in secret_file_names:
        data = f.split('|')
        if data[1] == ' .png':
            data[1] = 'space.png'

        src_file = os.path.join(asset_path, data[1])
        dest_file = os.path.join(newpath, data[0])
        shutil.copyfile(src_file, dest_file)

