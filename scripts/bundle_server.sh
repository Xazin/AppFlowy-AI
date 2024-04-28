#!/bin/bash

# Define the name of the server bundle.
server_bundle_name="appflowy_ai"

# Install PyInstaller for creating standalone executables.
pip freeze | grep PyInstaller || pip install pyinstaller

# Install other dependencies from the requirements file.
pip install -r requirements.txt

# Navigate to the application directory where the main.py file is located.
cd app

# Determine the operating system type using the OSTYPE environment variable.
os_type=$OSTYPE
echo "💻 Current OS Type: $os_type"

# Set the output name of the bundle based on the OS type.
if [[ $os_type == "msys" || $os_type == "win32" ]]; then
    # For Windows environments, detected as 'msys' (Git Bash) or 'win32'.
    name="${server_bundle_name}_win"
elif [[ $os_type == "darwin"* ]]; then
    # For macOS environments, identified by 'darwin'.
    name="${server_bundle_name}_osx"
else
    # For Linux and other Unix-like environments.
    name="${server_bundle_name}_lnx"
fi

echo "📡 Bundling the server for $name"

# Remove any previous build directories to prevent conflicts.
rm -rf dist/

# Create a standalone executable using PyInstaller.
pyinstaller --onefile --noconfirm --clean --name="$name" main.py

if [ -f "./dist/${name}" ]; then
    echo "🚀 Bundle successfully created, the binary is located at $(pwd)/dist/${name}"
else
    echo "❌ Failed to create the bundle."
    exit 1
fi
