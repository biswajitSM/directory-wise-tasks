import os
def remove_file_extension(folderpath, ext_str = ['.offfit']):
    for dirpath, dirname, filenames in os.walk(folderpath):
        for filename in [f for f in filenames if f.endswith(tuple(ext_str))]:
            file_path = os.path.join(dirpath, filename)
            os.remove(file_path)
            print(file_path)
    return