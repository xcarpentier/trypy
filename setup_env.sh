#/bin/bash

# This script is used to setup the environment for the project.

# if virtual environment is activate then exit.
if [ -n "$VIRTUAL_ENV" ]; then
    echo "Virtual environment is already activated."
else
    echo "Virtual environment is not activated."

    # Check if .venv exists, if not create it.
    if [ ! -d .venv ]; then
        python3 -m venv .venv
    fi

    # Activate the virtual environment.
    source ".venv/bin/activate"
fi

# Install the requirements.
pip install -r requirements.txt
