<<QAIC CERTIFICATION HTML EDITOR>>

Developed by : Naqibtech, Maismuka

Intended usage: To edit HTML file for certification purpose

This python script is developed with intention to edit the Certification html file which the Certification is 
produced by QAIC Team.

Below are the workflow of the application:

index.html ---[send to]----> html-editor.exe ---> new index.html

Definition:
index.html - this is a template file specifically used to edit the QAIC Certification. 
html-editor.exe - this is an executable program which acts as an editor for the QAIC Certification cert file (in html format).
new index.html - this is a final product of the html file which is edited by html-editor.exe.

How to create a Windows Executable file?

To create a Windows executable file from your provided Python script, I will use PyInstaller. Here are the steps to create the executable compatible with both Windows 10 and Windows 11:

1. Install PyInstaller: Ensure you have Python installed, and then install PyInstaller using the command:
pip install pyinstaller

2. Prepare the Python script: Make sure your Python script (html-editor.py) is in a separate folder to keep the generated files organized.

3. Generate the executable: Run the following command in the terminal or command prompt:
pyinstaller --onefile --windowed html-editor.py

This command will create a single executable file without a console window.

4. Adding an icon (Optional): If you want to add a custom icon, you can use the --icon flag. Place your icon file in the same directory and use:
pyinstaller --onefile --windowed --icon=your_icon.ico html-editor.py

5. Locate the generated executable: After running PyInstaller, you will find the executable in the dist folder created in the same directory as your script.