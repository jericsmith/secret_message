import os


def clear_directory(dir_path):
    for existing_file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, existing_file)
        delete_file(file_path)


def delete_file(file_path):
    if not os.path.isfile(file_path):
        return None

    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)
