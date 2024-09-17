# Desktop-Flask App

This is a simple Flask application that can be converted into a standalone desktop application using `PyInstaller` and `pywebview`. The app demonstrates a basic task management system and serves as a single-page application (SPA). Below is a detailed guide on how to set it up, run it, and package it as an executable.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Building an Executable with PyInstaller](#building-an-executable-with-pyinstaller)
- [File Structure](#file-structure)
- [Usage](#usage)

## Prerequisites

Before you get started, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- Flask
- PyInstaller
- PyWebView (optional for GUI)

You can install the required Python packages using the following command:

```bash
pip install flask pywebview
```

## Installation
### Clone this repository or download the project files.

```bash
git clone https://github.com/your-repo/electron-flask-app.git
cd electron-flask-app
```

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application
Once the dependencies are installed, you can run the Flask application locally:

```bash
python main.py
```

Open your browser and go to:

```arduino
http://127.0.0.1:5000
```
This will launch the Flask application in development mode.

## Building an Executable with PyInstaller
Follow these steps to build the app as a standalone executable using PyInstaller:

Install PyInstaller if you haven't already:

```bash
pip install pyinstaller
```
Create the executable using the following command:

```bash
pyinstaller --noconfirm --onefile --windowed --add-data "templates;templates" --add-data "static;static" main.py
```
Explanation:

- --noconfirm: Skips confirmation prompts during the build process.
- --onefile: Packages everything into a single executable.
- --windowed: Ensures the app runs without opening a console window (GUI mode).
- --add-data: Includes the templates and static folders in the build.

The generated executable will be available in the dist folder.

On Windows, it will look like:

```bash
dist/electron_flask_app.exe
```
You can now distribute the generated .exe file.

## File Structure
Here's the structure of the project:

```csharp
Copy code
electron-flask-app/
│
├── templates/
│   ├── base.html
│   └── index.html
│
├── static/
│   └── styles.css
│
├── main.py
├── requirements.txt
├── electron_flask.spec
└── README.md
```

- templates/: Contains the Jinja2 HTML templates.
- static/: Contains static files like CSS and JavaScript.
- main.py: The main Python Flask application file.
- requirements.txt: List of Python dependencies.
- electron_flask.spec: The PyInstaller spec file.

## Usage
- Add Task: Use the "Add Task" button on the main page to add a new task.
- View Tasks: Tasks will be displayed on the home page after they are added.

## Known Issues
Ensure that the templates and static folders are correctly included in the build command. If the paths are incorrect, it may cause the TemplateNotFound error.