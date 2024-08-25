# Create .gitignore File

Our .venv folder is huge. And we aren't responsible for  any of the code in it, and we don't need to keep track of it in our GitHub repo. 

Besides, it's a generated artifact, so if we mess it up, we just recreate it as needed using our commands. 

To keep it out of source control, Git will look for a .gitignore file. 

Anything listed in the .gitignore file will NOT be managed by git. 

There's no file name - just the dot and the .gitignore file extension. It's a common convention for environment files - to keep them visually away from the main project files where we do our work. 

## Steps

1. Create a new file named .gitignore in the root folder of our project. 
2. Add the contents as shown in [.gitignore](..\.gitignore).
