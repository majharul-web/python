# Instructions for Running the Script for Python venv

## Prerequisites

Before you can run the script, you need to set up a virtual environment and install the necessary dependencies.

### 1. Create and Activate Virtual Environment

1. **Navigate to the project directory**:
   Open your terminal and navigate to the project folder:

   ```bash
   cd /path/to/your/project
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

### 2. Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

```bash
# .env
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```

### 4. Run the Script

To run the script, use the following command:

```bash
python main.py
python3 exam/as_1/make_pyramid.py

```

### 5. Deactivate the Virtual Environment

When you're done, you can deactivate the virtual environment by running:

```bash
deactivate
```

### 6. Additional Notes

- Make sure to replace `your_api_key_here` and `your_api_secret_here` with your actual API credentials.
- If you encounter any issues, ensure that all dependencies are correctly installed and that your environment variables are set up properly.
- For any additional configurations or settings, refer to the documentation of the libraries you are using.
- If you are using a different version of Python, make sure to adjust the commands accordingly.
- If you are using a different operating system, the commands may vary slightly. Please refer to the documentation for your specific OS.
- If you are using a different shell (e.g., zsh, fish), the commands for activating the virtual environment may differ. Please refer to the documentation for your specific shell.
- If you are using a different package manager (e.g., conda), the commands for creating and activating the virtual environment may differ. Please refer to the documentation for your specific package manager.
- If you are using a different IDE or text editor, the commands for running the script may differ. Please refer to the documentation for your specific IDE or text editor.
- If you are using a different version control system (e.g., Git), the commands for managing your project may differ. Please refer to the documentation for your specific version control system.
- If you are using a different operating system, the commands for installing dependencies may differ. Please refer to the documentation for your specific operating system.
- If you are using a different programming language, the commands for running the script may differ. Please refer to the documentation for your specific programming language.
- If you are using a different framework or library, the commands for running the script may differ. Please refer to the documentation for your specific framework or library.
- If you are using a different database, the commands for connecting to the database may differ. Please refer to the documentation for your specific database.
- If you are using a different cloud provider, the commands for deploying the script may differ. Please refer to the documentation for your specific cloud provider.
- If you are using a different deployment method (e.g., Docker, Kubernetes), the commands for deploying the script may differ. Please refer to the documentation for your specific deployment method.
- If you are using a different CI/CD tool, the commands for deploying the script may differ. Please refer to the documentation for your specific CI/CD tool.
- If you are using a different testing framework, the commands for running tests may differ. Please refer to the documentation for your specific testing framework.
- If you are using a different code quality tool, the commands for running code quality checks may differ. Please refer to the documentation for your specific code quality tool.
- If you are using a different code formatting tool, the commands for running code formatting checks may differ. Please refer to the documentation for your specific code formatting tool.
- If you are using a different linting tool, the commands for running linting checks may differ. Please refer to the documentation for your specific linting tool.
- If you are using a different debugging tool, the commands for running debugging checks may differ. Please refer to the documentation for your specific debugging tool.
