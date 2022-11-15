# Electronics sales app

The application is implemented:

   - Getting information about all network objects
   - Getting information about objects of a certain country (filter by name)
   - Getting statistics about objects whose debt exceeds the average debt of all objects
   - Getting all network objects where you can meet a certain product (filter by product id)
   - Creating and deleting a network object and a product
   - The ability to update the data of the network object and product (prohibit updating via
API of the "Debt to the supplier" field)
   - Implemented a link to the "Supplier"
   - Filter by city name in the admin panel
   - "Admin action" has been implemented, clearing debts to the supplier from selected objects in the admin panel
   - API access rights are configured so that only active employees have access to the API.

Stack: Django, Django Rest Framework, PostgresSQL

## Install:

   - git@github.com:ieasycat/electronics_sales_app.git 
   - virtualenv -p python3 .venv
   - source venv_name/bin/activate
   - python -m pip install -r requirements.txt
   - Creation .env file. Example .env_example

## Starting migrations and filling the database with data:

   - python manage.py makemigrations
   - python manage.py migrate
   - python manage.py loaddata main_fixtures.json
   
## Creating a superuser:

   - python manage.py createsuperuser
   
## Launching the application:

   - python manage.py runserver

## Docker:

   - Creation .env_docker file. Example .env_docker_example
   - docker-compose up -d --build

## Technical task:
1. It is necessary to implement a network model for the sale of electronics. The network should be a hierarchical structure of 5 levels:
- Factory;
- Distributor;
- Dealership;
- Large retail chain;
- Individual entrepreneur.
Each link in the network refers to only one equipment supplier (not necessarily the previous one in the hierarchy). It is important to note that the hierarchy level is determined not by the name of the link, but by the relationship to the other elements of the network, i.e. the factory is always at level 0, and if the retail network refers directly to the factory, bypassing the other links, its level is 1.

2. Each link of the network has the following elements: 
- Name;
- Contacts:
  - Email;
  - Address:
    - Country;
    - City;
    - Street;
    - House number;
- Products:
  - Name;
  - Model;
  - The date of the product's release to the market; 
- Employees;
- Supplier (the previous network object in the hierarchy);
- Debt to the supplier in monetary terms, up to kopecks; 
- Creation time (filled in automatically when created).

3. Make a conclusion in the admin panel of the created objects; On the page of the network object add:
- Link to the "Supplier";
- Filter by city name;
- "Admin action", clearing the debt to the supplier of the selected objects.

4. Using DRF, create a set of views:
- 4.1 Information about all network objects;
- 4.2 Information about objects of a certain country (filter by name);
- 4.3 Statistics on objects whose debt exceeds the average debt
of all objects;
- 4.4 All network objects where a certain product can be found (filter by product id);
- 4.5 The ability to create and delete a network object and a product;
- 4.6 The ability to update the data of the network object and product (prohibit updating via
API of the "Debt to the supplier" field);

5. Configure API access rights so that only active employees have access to the API.

### Additional tasks:

  - Fill the database with test data. Choose the method yourself (item №1)
  - Prepare docker-compose to run all project services with one command.
  - Add validation of incoming data for paragraph 4.6 of the previous part. A network object has a name no longer than 50 characters. Make it easier to name the last 25 characters to check the correctness of the entered product release date on the market (item №4)