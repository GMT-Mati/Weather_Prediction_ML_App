# Makefile for setting up the Weather Prediction App development environment

# Python interpreter
PYTHON = python3

# Name of the virtual environment
VENV_NAME = weather-app-env

# Location of the requirements file
REQUIREMENTS = requirements.txt

# Command to create a virtual environment
VENV = virtualenv

.PHONY: setup-venv install-requirements

# Set up the virtual environment
setup-venv:
	@echo "Setting up virtual environment..."
	$(PYTHON) -m $(VENV) $(VENV_NAME)
	@echo "Virtual environment '$(VENV_NAME)' created. Activate it using 'source $(VENV_NAME)/bin/activate' (Linux/macOS) or '.\$(VENV_NAME)\Scripts\activate' (Windows)."

# Install required Python packages
install-requirements: setup-venv
	@echo "Installing required Python packages..."
	$(PYTHON) -m pip install -r $(REQUIREMENTS)
	@echo "Required packages installed."

# Help target to display available targets
help:
	@echo "Weather Prediction App Development Environment Setup"
	@echo "---------------------------------------------------"
	@echo "Available targets:"
	@echo "  setup-venv          Set up a virtual environment"
	@echo "  install-requirements Install required Python packages"
	@echo "  help                Show this help message"
