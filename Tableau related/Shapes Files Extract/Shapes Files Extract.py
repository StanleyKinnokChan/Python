import xml.etree.ElementTree as ET
import base64
import os

# save your workbook into twb
# Path to your XML file
xml_file_path = r"C:\Users\StanleyChan\Downloads\python\Shapes Files Extract\demo.twb"
output_dir = r"C:\Users\StanleyChan\Downloads\python\Shapes Files Extract\Shapes Files"
 
# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()
 
# Find all <shape> elements
shapes = root.findall('.//shape')

# Create an output directory for the images
os.makedirs(output_dir, exist_ok=True)
 
# Process each <shape> element
for shape in shapes:
    # Get the name attribute and base64 data
    name = shape.attrib.get('name')

    if name is not None:
        base64_data = shape.text.strip()
    
        # Decode the base64 data
        image_data = base64.b64decode(base64_data)
    
        # Determine the output file path
        output_file_path = os.path.join(output_dir, name.replace('/', '_'))
    
        # Save the image to a file
        with open(output_file_path, 'wb') as image_file:
            image_file.write(image_data)
    
        print(f'Saved image to {output_file_path}')
 
print('Image extraction complete.')