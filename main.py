import os
import importlib.util

def clean_temp_folder():
    temp_folder = os.environ.get('TEMP')
    if temp_folder:
        print(f"Cleaning Temp folder: {temp_folder}")
        for root, dirs, files in os.walk(temp_folder):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                except Exception as e:
                    print(f"Error deleting {file}: {e}")
        print("Temp folder has been cleaned.")
    else:
        print("Temp folder not found.")

def run_external_scripts():
    for script_name in ['rickrols.py', 'rerlamma.py']:
        spec = importlib.util.spec_from_file_location(script_name.split('.')[0], script_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

if __name__ == "__main__":
    clean_temp_folder()
    run_external_scripts()
