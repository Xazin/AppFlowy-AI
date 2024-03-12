#!/bin/bash

# Function to check if a Python package is installed
is_installed() {
    pip freeze | grep $1 > /dev/null
    return $?
}

# Function to install a Python package using pip
ensure_installed() {
    PACKAGE=$1
    if is_installed $PACKAGE; then
        echo "$PACKAGE is already installed."
    else
        echo "$PACKAGE is not installed. Installing..."
        pip install $PACKAGE
    fi
}

# Ensuring necessary packages are installed
ensure_installed "autoflake"
ensure_installed "isort"
ensure_installed "black"
ensure_installed "pylint"

# Define the directory containing your Python code
CODE_DIR="./app"

# Run autoflake
echo "Running autoflake to remove unused imports and variables..."
autoflake --remove-all-unused-imports --remove-unused-variables --in-place --recursive $CODE_DIR

# Run isort
echo "Running isort to sort imports..."
isort $CODE_DIR

# Run black
echo "Running black to format code..."
black $CODE_DIR

# Run pylint
echo "Running pylint for static code analysis..."
pylint $CODE_DIR

echo "Auto-fix script completed."
