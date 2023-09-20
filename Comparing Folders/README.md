# Folder Comparison Tool

This is a Python script that provides a graphical user interface (GUI) for comparing the contents of two folders. It allows you to:

- Input the paths of the two folders.
- Compare the folders for files that exist in one folder and not in the other.
- Display a summary of the file count in each folder and its subfolders.

## Getting Started

### Prerequisites

- Python (3.x recommended)
- tkinter library (included in most Python installations)

### Usage

1. Clone the repository or download the `app.py` file.

2. Run the script using Python:

   ```
   python app.py
   ```

   This will launch the GUI application.

3. In the GUI, enter the paths of the two folders you want to compare. You can either type them directly or click the "Browse" button to select them.

4. Click the "Generate Report" button.

5. The application will display the files unique to each folder and provide a summary of the file count.

To create a standalone executable for your Python script with a graphical user interface (GUI), you can use a library like `PyInstaller` or `cx_Freeze`. These tools package your Python application along with its dependencies into a single executable file (exe) that can be run on a Windows machine.

Here are the steps using `PyInstaller`:

1. **Install PyInstaller**:

   Open a command prompt or terminal and run:

   ```
   pip install pyinstaller
   ```

2. **Create the Executable**:

   In the command prompt or terminal, navigate to the directory containing your Python script and run:

   ```
   pyinstaller --onefile your_script_name.py
   ```

   Replace `your_script_name.py` with the actual name of your script -> app.py

   This command tells `PyInstaller` to create a single executable file (`--onefile`) for your script.

4. **Locate the Executable**:

   `PyInstaller` will create a `dist` directory in the same location as your script. Inside `dist`, you'll find the standalone executable file. It will have the same name as your script.

5. **Testing**:

   Double-click the executable to run it. It should launch your GUI application. You can create a shortcut to you desktop if you need to use it frequently.

6. **Distributing**:

   You can now distribute this executable to others. They won't need Python or any additional libraries installed.

Keep in mind that `PyInstaller` may generate additional files and folders in the `dist` directory. These are necessary for the executable to run properly. If you need more customization, `PyInstaller` offers various options you can use in the command line.

## Contributing

If you find a bug or have an idea for an enhancement, feel free to open an issue or create a pull request.

