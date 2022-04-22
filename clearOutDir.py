import os, shutil

def clearOutDir():
    out_path = "out"

    if not os.path.exists(out_path) or not os.path.isdir(out_path):
        os.mkdir(out_path)

    for file_name in os.listdir(out_path):
        file_path = os.path.join(out_path, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except:
            print(f"Failed to remove {file_path}.")
