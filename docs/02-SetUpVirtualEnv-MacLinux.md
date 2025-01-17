# Set Up Local Project Virtual Environment

When we use external packages (as we typically do), we want to work in an isolated virtual environment. 

We recommend creating one virtual environment per project which can be found in the .venv folder of our project repository. 

There are several steps:

1. Create it (generally only once)
2. Activate it (whenever we work on the project!)
3. Install packages as needed (must be active)

## Create

Open a new Terminal in VS Code (Menu: Terminal / New Terminal) and create it. 

In terminal:

```shell
python3 -m venv .venv
```

## Activate (ALWAYS!)

In terminal:

```shell
source .venv/bin/activate
```

Important! Remember to activate your .venv every time you open a terminal to work on your project. 

Verify the .venv appears in your terminal prompt. 

## Install Packages (as needed)

In terminal:

Upgrade pip with the recommended command:

```shell
python3 -m pip install --upgrade pip
```

```shell
py -m pip install requests --upgrade
py -m pip install openpyxl --upgrade
```

