Resources
Read or watch:

NoSQL Databases Explained
What is NoSQL ?
MongoDB with Python Crash Course - Tutorial for Beginners
MongoDB Tutorial 2 : Insert, Update, Remove, Query
Aggregation
Introduction to MongoDB and Python
mongo Shell Methods
The mongo Shell
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What NoSQL means
What is difference between SQL and NoSQL
What is ACID
What is a document storage
What are NoSQL types
What are benefits of a NoSQL database
How to query information from a NoSQL database
How to insert/update/delete information from a NoSQL database
How to use MongoDB
Requirements
MongoDB Command File
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4)
All your files should end with a new line
The first line of all your files should be a comment: // my comment
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
Python Scripts
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9) and PyMongo (version 4.8.0)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5.*)
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
Your code should not be executed when imported (by using if __name__ == "__main__":)
Install MongoDB 4.4 in the sandbox (Ubuntu 22.04)
1. Install the missing libssl1.1 dependency
MongoDB 4.x requires OpenSSL 1.1, which isn’t included in Ubuntu 22.04.

echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt update
sudo apt install -y libssl1.1
sudo rm /etc/apt/sources.list.d/focal-security.list
sudo apt update
2. Add the MongoDB 4.4 repository and key
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update
3. Install MongoDB 4.4 packages
sudo apt install -y mongodb-org
4. Prepare required directories and permissions
sudo mkdir -p /var/lib/mongodb /var/log/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb
5. Start mongod
sudo -u mongodb /usr/bin/mongod --config /etc/mongod.conf &
This runs MongoDB in the foreground.

Verification
Check the MongoDB version:

mongod --version
Expected output should show something like v4.4.xx.