import os
import shutil
import tempfile
import psutil


def show_environment_variables():
    """
    Displays all environment variables.
    """
    env = dict(os.environ)
    return env


def clear_temp_files():
    """
    Deletes files from the system's temporary directory.
    """
    temp_dir = tempfile.gettempdir()
    deleted = 0
    failed = 0

    for item in os.listdir(temp_dir):
        path = os.path.join(temp_dir, item)

        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
                deleted += 1

            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
                deleted += 1

        except Exception:
            failed += 1

    return {
        "Temporary Folder": temp_dir,
        "Deleted": deleted,
        "Failed": failed
    }


def get_current_directory():
    """
    Returns the current working directory.
    """
    return os.getcwd()


def list_disk_partitions():
    """
    Lists all available disk partitions.
    """
    partitions = []

    for partition in psutil.disk_partitions():
        partitions.append({
            "Device": partition.device,
            "Mount Point": partition.mountpoint,
            "File System": partition.fstype
        })

    return partitions


def create_directory(path):
    """
    Creates a new directory.
    """
    try:
        os.makedirs(path, exist_ok=True)
        return "Directory created successfully."
    except Exception as e:
        return str(e)


def delete_directory(path):
    """
    Deletes a directory.
    """
    try:
        shutil.rmtree(path)
        return "Directory deleted successfully."
    except Exception as e:
        return str(e)


if __name__ == "__main__":

    print("===== CONFIGURATION TOOL =====")

    print("\nCurrent Working Directory:")
    print(get_current_directory())

    print("\nDisk Partitions:")
    for partition in list_disk_partitions():
        print(partition)

    print("\nEnvironment Variables:")
    env = show_environment_variables()

    count = 0
    for key, value in env.items():
        print(f"{key} = {value}")
        count += 1
        if count == 10:
            print("... (showing first 10 variables only)")
            break

    choice = input("\nDo you want to clear temporary files? (y/n): ")

    if choice.lower() == "y":
        result = clear_temp_files()
        print(result)
    else:
        print("Operation cancelled.")