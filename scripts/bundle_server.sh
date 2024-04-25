#!/bin/bash

server_bundle_name="appflowy_ai_server"

# install the PyInstaller
pip install pyinstaller

# install the requirements
pip install -r requirements.txt

# cd to app directory
cd app

# bundle the server depending on the OS
os_type=$OSTYPE
echo "💻 current OS Type: $os_type"

if [[ $os_type == "msys" || $os_type == "win32" ]]; then
    name="${server_bundle_name}_win"
elif [[ $os_type == "darwin"* ]]; then
    name="${server_bundle_name}_osx"
else
    name="${server_bundle_name}_lnx"
fi

echo "📡 Bundling the server for $name"
rm -rf dist/
pyinstaller --onefile --noconfirm --clean --name="$name" main.py
echo "🚀 Bundle succesully, the binary is in $(pwd)/dist/${name}"
