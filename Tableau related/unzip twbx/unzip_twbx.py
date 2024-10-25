import zipfile
import os
import xml.etree.ElementTree as ET
import shutil

import zipfile
import os
import xml.etree.ElementTree as ET
import shutil

def unzip_twbx(file_path):
    file_path = r'{}'.format(file_path)
    twb_file_path = None
    extracted_folder = None

    if file_path.endswith('.twbx'):
        # Create a folder for extraction in the same directory as the file
        extracted_folder = os.path.join(os.path.dirname(file_path), 'extracted_twbx')
        os.makedirs(extracted_folder, exist_ok=True)
        
        # Unzip the twbx file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)
        
        # Look for a .twb file in the extracted folder
        for root, dirs, files in os.walk(extracted_folder):
            for file in files:
                if file.endswith('.twb'):
                    twb_file_path = os.path.join(root, file)
                    break
        if twb_file_path is None:
            raise FileNotFoundError("No .twb file found in the .twbx package")

    elif file_path.endswith('.twb'):
        # If it's a .twb file, just set the path
        twb_file_path = file_path
    else:
        raise ValueError("The provided file is neither a .twbx nor a .twb file")


    return root

unzip_twbx(r"C:\Users\StanleyChan\SynologyDrive\Tech\python\Tableau related\Extract twb from twbx\Clayton Kershaw_ An Electric Career.twbx")