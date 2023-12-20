# GunShopBDD

## Project Description

GunShopBDD is a project developed for our database class, focusing on the functionalities of a gun shop. The system includes features such as background checks for clients, inventory management, and more.

## Technologies Used

- Python
- Flask
- Microsoft SQL
- Flask-wtf
- Faker

## Requirements

To run and contribute to this project, ensure you have the following tools and dependencies installed:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/) (Install the 3.9.8 version)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) (Install using `pip install Flask`)
- [Pypyodbc](https://github.com/pypyodbc/pypyodbc) (Install using `pip install pypyodbc`)

### Setting Up the Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/GunShopBDD.git
   cd GunShopBDD

2. It's recommended to create a python enviroment

   ```bash
   Steps:
      1. Open the Command Palette (Ctrl+Shift+P), start typing the Python: Create Environment command to search, and then select the command.

      2. Select Venv

      3. The command then presents a list of interpreters that can be used for your project. Select interpreter for the python 3.9.8 you installed at the begining.

      4. After selecting the interpreter, a notification will show the progress of the environment creation and the environment folder (/.venv) will appear in your workspace.

      5. Ensure your new environment is selected by using the Python: Select Interpreter command from the Command Palette.

      6. Delete all terminal windows currently active in VSCode

      7. Open a new powershell window in VSCode

      8. If for any reason you get a similar error to "cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at..." then you need to open a PS(powershell) admin window and type the following command "Set-ExecutionPolicy RemoteSigned" close VS PS terminal window currently opened and open new one and it should begin to login into your enviroment automatically.

      9. Be careful because history restored terminals won't be running the enviroment so it's recomended to create a new terminal window when you start vscode

3. Installing dependecies:

   ```bash
   pip install -r requirements.txt

Remember:
Replace "your-username" in the clone URL with your actual GitHub username.

Everything should work now!
Feel free to fork the project if you want or need to do something similar for your class
