# Local MySQL server setup

sudo apt install mysql-server -y

## Start database service
sudo service mysql start

## Check Status of service
sudo service mysql status

## Install python extension
pip install mysql-connector-python

# Database creation
- Created 'utils/schema.sql': Creating database schema under 'root' user of mysql service

## Running the raw SQL script (only once)
sudo mysql -u root -p < utils/schema.sql

## To check existing databases
sudo mysql -u root -p -e "SHOW DATABASES;"

## To check existing tables in database
sudo mysql -u root -p -e "USE intern_project; SHOW TABLES;"

## To check inside the table
sudo mysql -u root -p -e "USE intern_project; SHOW TABLES; SELECT * from employees;"