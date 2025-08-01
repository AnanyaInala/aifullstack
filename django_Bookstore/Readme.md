Open your terminal or command prompt.

Navigate to your project's parent directory (BookStore).

Bash

#cd C:\Users\ananya inala\Documents\BookStore
Activate your virtual environment.

Bash

#.\env\Scripts\activate
You should see (env) at the beginning of your command prompt.

Step 2: Navigate to Your Project and Run Migrations

Navigate into your Django project's root directory.

Bash

#cd mybookstore
Run the makemigrations command to detect any changes you've made to your models and create migration files. It's a good practice to run this for all your apps at once.

Bash

#python manage.py makemigrations accounts books cart orders
Run the migrate command. This will apply any new migrations and update your database schema to match your models.

Bash

#python manage.py migrate
Step 3: Create a Superuser (If Needed)

If you have just reset your database (by deleting db.sqlite3), you'll need to create a new superuser to access the admin panel.

Run the createsuperuser command.

Bash

#python manage.py createsuperuser
Follow the prompts to set up a username and password.

Step 4: Run the Development Server

Finally, start the development server.

Bash

#python manage.py runserver
You should see output indicating that the server is running, usually at http://127.0.0.1:8000/.

