# FIRST SIMPLE ONLINE SHOP: ACCESSORY SHOP WITH DJANGO
This project is my first store on django framework. Just an accessory store with a cart, registration, login and not a big analog of checkout. 
## Technologies Used
1. Python
2. Django
3. Bootstrap
4. PostgreSQL
### How to Run the Application
1. Clone or download the project to your local machine.
2. Change directory to the "heavy-shop" folder.
3. Ensure that you have Python 3, pip, and virtualenv installed on your machine.
4. Create a virtual environment using the following command:

- **For Mac and Linux:**  
  ```sh
  python3 -m venv venv
- **For Windows**
  ```sh
  python -m venv venv
5. Activate the virtual environment:
   - For Mac/Linux: `source venv/bin/activate`
   - For Windows: `venv\scripts\activate`
6. Install the application requirements by running: `pip install -r requirements.txt`
7. Migrate the database by executing: `python managa.py migrate`
8. Start server: `python manage.py runserver`
9. You should now be able to access the application by visiting: http://127.0.0.1:8000/

## Creating a Superuser

You need to create a superuser if you want to add products, categories, etc.

Run the following command:

```sh
python manage.py createsuperuser
