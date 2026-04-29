Resources
Read or watch:

ECMAScript 6 - ECMAScript 2015
Statements and declarations
Arrow functions
Default parameters
Rest parameter
Javascript ES6 — Iterables and Iterators
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

What ES6 is
New features introduced in ES6
The difference between a constant and a variable
Block-scoped variables
Arrow functions and function parameters default to them
Rest and spread function parameters
String templating in ES6
Object creation and their properties in ES6
Iterators and for-of loops
Requirements
General
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using node 20.x.x and npm 9.x.x
Allowed editors: vi, vim, emacs, Visual Studio Code
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the js extension
Your code will be tested using the Jest Testing Framework
Your code will be analyzed using the linter ESLint along with specific rules that we'll provide
All of your functions must be exported
Setup
Install NodeJS 20.x.x
(in your home directory):

curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
$ nodejs -v
v20.15.1
$ npm -v
10.7.0
Install Jest, Babel, and ESLint
in your project directory:

Install Jest using: npm install --save-dev jest
Install Babel using: npm install --save-dev babel-jest @babel/core @babel/preset-env
Install ESLint using: npm install --save-dev eslint
Configuration files
Please create the following 3 files (with the provided contents) in the project directory:

package.json
Click to show/hide file contents
babel.config.js
Click to show/hide file contents
.eslintrc.js
Click to show/hide file contents
Finally…
Don't forget to run npm install from the terminal of your project folder to install all necessary project dependencies. Do not push on your repository the folder node_modules that has been created.