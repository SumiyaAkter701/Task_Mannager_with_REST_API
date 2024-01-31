<div align="center">
<h1>Task Management With Rest API</h1>
<br>

<h3>-----Project's Short Video link-----</h3>
Google Drive : https://drive.google.com/drive/folders/15Iogqy2iKH2fDUkX3vmVDL2aJbRIwzKO?usp=sharing 
<br>

</div>

<br>

## Technology Used --------

-   **Frontend:** HTML5, CSS3, Bootstrap5
-   **Backend:** Python=3.11.4, Django=4.2.5
-   **Database:** PostgreSQL
-   **API:** Django-REST-Framework

<br>

## How to Run Step by step --------


### Clone from GitHub

-   Clone the repository

```bash
git clone https://github.com/SumiyaAkter701/Task_Mannager_with_REST_API.git
```

-   Go to the project directory

```bash
cd Task_Mannager_with_REST_API
```

-   Create a virtual environment

```bash
python -m venv virtual_env
```

-   Activate the virtual environment

```bash
source virtual_env/Scripts/activate
```

-   Install the all required Lib

```bash
pip install -r requirements.txt
```

-   Run the server

```bash
python manage.py runserver
```

-   Open the browser and go to http://127.0.0.1:8000/

<br>

### Setup PostgreSQL

-   Install PostgreSQL

```bash
pip install psycopg2
```

-   Login to PostgreSQL

-   Create a database

-   Create a user

-   Exit from PostgreSQL


<br>

### Create environment variables & Config settings.py

-   Open the `settings.py` file from `Task_Mannager` directory

-   Create a file named `.env` in the `Task_Mannager` directory and add the following lines

```bash
SECRET_KEY = Enter your django project secret key.

#DATABASE
ENGINE= django.db.backends.postgresql
NAME= Enter your Database name
USER= Enter your Databse user name
PASSWORD= Enter your Database password
HOST= Enter your Databse HOST name
PORT= Enter your Databse PORT number

#Send Email backend
EMAIL_HOST_USER = Enter your e-mail host user name
EMAIL_HOST_PASSWORD = Enter your e-mail host user password
```

See the `.env.example` .

<br>

### Import Data from db.json

-   You will find a file named `db.json` in the root directory


-   Migrate Database

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```


-   Run the following command to import data from `db.json`

```bash
python manage.py loaddata db.json
```
<br>

## API View Point --------
-   **Endpoint:** http://127.0.0.1:8000/api-view/
-   **Method:** GET, POST
-   **Description:**
    -   Returns all the tasks
    -   Create a new task using by post method
-   **Endpoint:** http://127.0.0.1:8000/api-view/9/
-   **Method:** GET, PUT, PATCH, DELETE
-   **Description:**
    -   Single task Return
    -   Single task Updates
    -   Single task Partially updates 
    -   Single task Deletes

<br>

### Admin Panel --------

-   Run the server

```bash
python manage.py runserver
```

-   Open http://127.0.0.1:8000/admin/ for access the admin panel

-   Login with the following credentials:

    -   Username: `admin`
    -   Password: `admin`

<br>

### User Credentials --------

-   User Credentials: Username: `sumiyaUser ` , Password: `sumiyaUser`

-   Staff Credentials: Username: `sumiyaStaff` , Password: `sumiyaStaff`

-   Admin Credentials: Username: `sumiyaAdmin` , Password: `sumiyaAdmin`

<br>


