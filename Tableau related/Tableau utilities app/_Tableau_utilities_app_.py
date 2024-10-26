import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
import sys
from read_tableau_to_xml import read_tableau_to_xml
from Shapes_Files_Extract import Shapes_Files_Extract
from image_extract import image_extract
from unzip_twbx import unzip_twbx
from Tableau_Calculation_Dependencies import Tableau_Calculation_Dependencies
from workbook_colour_extractor import *
import os
import webbrowser

# Initialize the main window
root = TkinterDnD.Tk()  # TkinterDnD enabled root
root.title("Tableau Utilities")
root.geometry("600x650")

# Variable to store the file path
file_path = tk.StringVar()

# Class to redirect stdout to the Text widget
class TextRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, message):
        self.widget.config(state=tk.NORMAL)
        self.widget.insert(tk.END, message)
        self.widget.see(tk.END)  # Scroll to the end
        self.widget.config(state=tk.DISABLED)

    def flush(self):
        pass  # Flush is required for compatibility with stdout

# Function to browse files
def browse_file():
    file = filedialog.askopenfilename(title="Select a file")
    if file:
        file_path.set(file)

# Function to handle drag and drop
def drop(event):
    file_path.set(event.data.strip('{}'))

# Function to display the initial panel again
def show_initial_panel():
    script_panel.pack_forget()  # Hide the script panel
    initial_panel.pack(pady=20)  # Show the initial panel

# Function to process files and capture output
def process_file(func, *args):
    file = file_path.get()
    file = r'{}'.format(file)

    if not file:
        print("No file selected")
        return None

    try:
        return func(file, *args)
    except Exception as e:
        print(f"Error processing the file: {e}")
        return None

# Wrapper to run each script and capture print output
def run_script_with_output(func):
    console_output.config(state=tk.NORMAL)
    console_output.delete(1.0, tk.END)  # Clear previous output
    console_output.config(state=tk.DISABLED)

    sys.stdout = TextRedirector(console_output)  # Redirect stdout
    try:
        func()
    finally:
        sys.stdout = sys.__stdout__  # Reset stdout back to default

# Function to run Tableau XML parsing
def run_read_tableau_to_xml():
    return process_file(read_tableau_to_xml)

# Script functions
def run_unzip_twbx():
    run_script_with_output(lambda: process_file(unzip_twbx))

def run_Shapes_Files_Extract():
    # Process XML first
    xml_root = run_read_tableau_to_xml()
    if xml_root:
        # Then proceed to extract shapes
        run_script_with_output(lambda: process_file(Shapes_Files_Extract, xml_root))

def run_image_extract():
    return process_file(image_extract)

def run_Tableau_Calculation_Dependencies():
    # Process XML first
    xml_root = run_read_tableau_to_xml()
    if xml_root:
        # Then proceed with calculation dependency analysis
        run_script_with_output(lambda: process_file(Tableau_Calculation_Dependencies, xml_root))

def run_workbook_colour_extractor():
    # Process XML first
    xml_root = run_read_tableau_to_xml()
    if xml_root:
        # Then proceed with calculation dependency analysis
        run_script_with_output(lambda: process_file(workbook_colour_extractor, xml_root))

# Function to display new panel with buttons to execute different scripts
def show_script_panel():

    if not os.path.exists(file_path.get()) or not file_path.get().endswith(('.twb', '.twbx')):
        # Show warning when file path is not valid
        messagebox.showwarning("Invalid File", "Please select a valid workbook (.twb/.twbx).")
        return  # Prevent further execution and do not move to the script panel

    # Hide the initial panel (label, entry, and buttons)
    initial_panel.pack_forget()

    # Create new panel for script execution buttons
    global script_panel
    script_panel = tk.Frame(root)
    script_panel.pack(pady=20, fill="both", expand=True)

    # Heading for the script execution panel
    tk.Label(script_panel, text="What actions you want to perform?", font=("Arial", 14)).pack(pady=10)

    # Button to execute Script 1
    script1_button = tk.Button(script_panel, text="Unzip the Package Workbook (.twbx)", command=run_unzip_twbx)
    script1_button.pack(pady=5)

    # Button to execute Script 2
    script2_button = tk.Button(script_panel, text="Extract Shapes", command=run_Shapes_Files_Extract)
    script2_button.pack(pady=5)

    # Button to execute Script 3
    script3_button = tk.Button(script_panel, text="Extract Container Images", command=run_image_extract)
    script3_button.pack(pady=5)

    # Button to execute Script 4
    script4_button = tk.Button(script_panel, text="Calculation Dependency Analysis", command=run_Tableau_Calculation_Dependencies)
    script4_button.pack(pady=5)

    # Button to execute Script 5
    script5_button = tk.Button(script_panel, text="Extract Colour from Workbook", command=run_workbook_colour_extractor)
    script5_button.pack(pady=5)

    # Show the console_output only in the script panel
    global console_output
    console_output = tk.Text(script_panel, height=10, width=70, state=tk.DISABLED)
    console_output.pack(pady=50)

    # Add a "Return" button to go back to the initial panel
    return_button = tk.Button(script_panel, text="Return", command=show_initial_panel)
    return_button.pack(pady=10)

# Initial Panel (Drag and Drop, File Selection)
initial_panel = tk.Frame(root)
initial_panel.pack(pady=10)

# Create and configure the label to display the file path
text_header = tk.Label(initial_panel, text='      Tableau Utilities (Beta 1.2)',
							fg='white', bg='#0876ee', font=('verdana',14,'bold'),
							width=450, height=1, compound=tk.LEFT,
							anchor='w')
text_header.pack(pady=20)

# Create and configure the label to display the file path
label = tk.Label(initial_panel, text="Drag and drop a workbook (.twb/.twbx) here", width=60, height=4, bg="lightgray")
label.pack(pady=20)

text_OR = tk.Label(initial_panel, text="or", font=("Arial", 8))
text_OR.pack(pady=5)

# Button to browse files
browse_button = tk.Button(initial_panel, text="Browse Workbook", command=browse_file)
browse_button.pack(pady=10)


# empty space
empty_frame = tk.Frame(initial_panel, height=70)  # Adjust height as needed
empty_frame.pack()

text_yourWB = tk.Label(initial_panel, text="                     Your selected workbook:", font=("Arial", 8), anchor="w")  # Align text to the left
text_yourWB.pack(pady=0, fill='x')  # Use fill='x' to make the label take the full width

# Entry widget to display the file path
entry = tk.Entry(initial_panel, textvariable=file_path, width=60)
entry.pack(pady=10)

# Confirm Button to proceed to the script panel
confirm_button = tk.Button(initial_panel, text="Confirm", command=show_script_panel)
confirm_button.pack(pady=15)

######### Footer Section

######### Benchmark
# Text
text_Benchmark = tk.Label(initial_panel, text="Copyright is owned by", font=("Arial", 8))
text_Benchmark.pack(pady=5)  # Adjust pady as needed for spacing

# Function to open the URL
def open_link(event):
    webbrowser.open("https://www.linkedin.com/in/staneykinnok-chan/")

# Create the hyperlink text label
hyperlink_text = tk.Label(initial_panel, text="Stanley Chan", fg="blue", cursor="hand2", font=("Arial", 8, "underline"))
hyperlink_text.pack(pady=5)

# Bind the click event to the open_link function
hyperlink_text.bind("<Button-1>", open_link)

# Construct the image file path
script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
image_path = os.path.join(script_directory, '_image', 'Linkedin QR.png')

# Load and display the image
image = tk.PhotoImage(file=image_path)
image_label = tk.Label(initial_panel, image=image)
image_label.pack(pady=5)

# Bind DnD functionality to the label
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', drop)

# Start the Tkinter loop
root.mainloop()
