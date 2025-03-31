## Creating a virtual environment is essential for isolating dependencies in Python projects. Here's how you can do it:
 
# Step 1: Install virtualenv (if not installed)

Before creating a virtual environment, ensure you have virtualenv installed. If not, install it using:

pip install virtualenv

# Step 2: Create a Virtual Environment

Navigate to your project directory and run:

python -m venv Rest-api

# Step 3: Activate the Virtual Environment

On Windows (Command Prompt)

Rest-api\Scripts\activate

On Windows (PowerShell)

Rest-api\Scripts\Activate.ps1

On macOS/Linux

source Rest-api/bin/activate

# Step 4: Install Dependencies

Once activated, install your project dependencies:

pip install -r requirements.txt

(if you have a requirements.txt file)


# Step 5: Deactivate the Virtual Environment

When done, deactivate the virtual environment by running:

deactivate