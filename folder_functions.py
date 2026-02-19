import os
import shutil

def openFolder(folder_path: str) -> list:
    '''Opens a folder and extracts all of the files within.'''

    try: 
        files_in_directory = os.listdir(folder_path)
    except Exception as e:
        print(f"Sorry unc exception {e} occurred!")
        return []
    return files_in_directory
    
def sortFolder(file_list: list) -> dict:
    '''Sorts files into a hash map'''

    files_map = {}
    for i in file_list:
        dot_count = i.count('.')
        # Remove additional dots in file names for classifications
        if dot_count > 1:
            replaced = i.replace('.', '/', dot_count - 1)
            split = replaced.split('.')
        else:
            split = i.split('.')

        try:
            if split[1] not in files_map:
                files_map[split[1]] = []
                files_map[split[1]].append(i)
            else:
                files_map[split[1]].append(i)
        except Exception:
            pass
    print(files_map)
    return files_map

def createFolders(folder_map: dict, folder_path: str):
    if len(folder_map) > 0:
        organised_dir = folder_path + '/Organised Files'
        os.makedirs(organised_dir, exist_ok=True)
        for i in folder_map:
            key_dir = organised_dir + '/' + i
            os.makedirs(key_dir, exist_ok=True)
            for j in folder_map[i]:
                shutil.move(folder_path + '/' + j, key_dir + '/' + j)