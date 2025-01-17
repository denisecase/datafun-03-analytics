# datafun-03-analytics

## Overview
This project demonstrates how to fetch and process various types of 
data (Excel, JSON, text, and CSV) using Python. 

The repository includes:

- Four example fetchers: Scripts to retrieve data from the web.
- Four example processors: Scripts to analyze and process the fetched data.

Start by running the examples to understand their functionality, and then build your own scripts to fetch and process data of your choice (using each of these example types).

---
## Project Workflow

### Step 1. Set Up Your Project
1. Create a GitHub repo with default README.md (you'll need to manually add these example files).
2. Clone your new repo down to your machine. 
3. Open the folder in VS Code.
4. Add a .gitignore file.
5. Install the required packages - see [requirements.txt](requirements.txt).

Full disclosure: We teach building repos from scratch because we assume students want to learn to create their own novel projects. 
However, if you want to get a local copy of this repo down to your machine, you can click the "Use this template" green button to copy it all into your account.  

### Step 2. Run the Examples
If you started with your own repo, copy the files from this GitHub as needed. 
If you cloned the template, you'll have the example files already. 

Read, review, and run each example script. 
Open a terminal in the root project folder and run the appropriate 
command for your operating system. 
For example, these generally work on Windows. 
Adjust the commands to work for your machine, 
e.g. use python3 if Mac/Linux. 

```shell
py fetch_scripts/example_get_csv.py
py fetch_scripts/example_get_excel.py
py fetch_scripts/example_get_json.py
py fetch_scripts/example_get_text.py

py process_scripts/example_process_csv.py
py process_scripts/example_process_excel.py
py process_scripts/example_process_json.py
py process_scripts/example_process_text.py

```

TODO: Replace the example commands with the actual commands used on your machine.
Ensure all example scripts run without errors before proceeding.
 
### Step 3. Create and Run Your Data Fetchers
1. Find data files on the web for each type (CSV, Excel, JSON, and text).  
2. Create your own Python script to fetch each type of data and save it in a folder named **data**.
3. Name your scripts:
   1. yourname_get_csv.py
   2. yourname_get_excel.py
   3. yourname_get_json.py
   4. yourname_get_text.py
4. Implement your data-processing logic in small steps:
   - Fetch data for one file type.
   - Test, verify, and Git add-commit-push.
  
## Step 4. Create and Run Your Data Processors
1. Determine a simple metric from each of your data files.  
2. Create your own Python script to read the data, process it, and save it in a folder named **data_processed**.
3. Name your scripts:
   1. yourname_process_csv.py
   2. yourname_process_excel.py
   3. yourname_process_json.py
   4. yourname_process_text.py
4. Work incrementally, using git add-commit-push after each bit of progress. 

## Step 5. Update README.md to Describe Your Work
1. In your README.md, list each of your fetchers with a short description.
2. In your README.md, list each of your processors with a short description of what it does. 
3. Include the execution commands to run your fetchers and processors. 

---

## Helpful Documentation
If you're unsure about any of the setup steps or tools, consult these resources:
- [requests library documentation](https://docs.python-requests.org)
- [GitHub: Create and Clone a Repo](prereqs/01-CreateAndClone.md)
- [Set Up a Virtual Environment](docs/02-SetUpVirtualEnv.md)
- [Create a .gitignore File](docs/03-CreateGitIgnore.md)
- [Using Git: Add-Commit-Push](docs/04-GitAddCommitPush.md)

---

### Tips
- Use descriptive filenames for the data you fetch - and proper file extensions.
- Work incrementally—verify each small step works before moving to the next.
- The examples are required reading - use them to learn and understand first. 
- Test each script carefully before proceeding.
- Use meaningful commit messages when pushing to GitHub to document your progress.

---
## Review Commit History
Once your project is complete, review your commit history in GitHub under the **Commits** tab. 
Ensure your commit messages are clear and professional.

---
## Finalize GitHub

Make sure the following requirements have been met:

- [ ] You have committed a useful .gitignore file.
- [ ] You have committed a useful logs/project_log.log file. 
- [ ] All example scripts executed successfully.
- [ ] Four fetcher scripts created and executed.
- [ ] Four processor scripts created and functional.
- [ ] README.md includes explanations for fetchers and processors with commands for execution.
- [ ] Each Python file contains a docstring with its purpose and input/output details.
