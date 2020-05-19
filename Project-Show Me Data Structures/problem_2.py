import os


def find_files(suffix = "", path = "."):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    files = []
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
    else: 
        new_paths =  os.listdir(path)
        for item in new_paths:
            files += find_files(suffix, "{}/{}".format(path, item))            
    return files

ff = find_files(suffix=".c",path="C:/Users/Sumit/Downloads/testdir")
for f in ff:
    print(f)
