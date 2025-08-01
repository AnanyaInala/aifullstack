Django Bookstore App 📚

A fully functional Django-based web application simulating an online bookstore. Users can browse books, manage their shopping cart, place orders, and more, all within a secure and user-friendly interface.



✨ Features





User Authentication: Secure sign-up and login using Django's built-in authentication system.



User Profiles: Update personal information and upload profile pictures.



Book Catalog: Browse trending books on the homepage or explore the full catalog on the "All Books" page.



Search & Filter: Find books by title, author, or price with a search bar and filtering options.



Shopping Cart: Add, adjust, or remove books with real-time updates.



Checkout Process: Simulated checkout with Cash on Delivery (other payment methods are placeholders).



Order History: View past orders and track delivery status.



Admin Panel: Manage books, users, carts, and orders via Django's admin interface.



🛠️ Technologies Used





Python: Core programming language.



Django: Web framework for rapid development and clean design.



Pillow: Handles image uploads for user profile pictures.



SQLite: Default database for development (configurable for production).



HTML/CSS/JavaScript: Frontend for responsive and interactive UI.



📋 Prerequisites





Python 3.8+: Ensure Python is installed.



Virtual Environment: Recommended to isolate dependencies.



Git: For cloning the repository.



🚀 Installation & Setup





Clone the Repository:

git clone https://github.com/your-username/django-bookstore.git
cd django-bookstore/mybookstore



Set Up a Virtual Environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate



Install Dependencies:

pip install django==5.2.4 Pillow



Apply Database Migrations:

python manage.py migrate



Create a Superuser (for admin access):

python manage.py createsuperuser

Follow the prompts to set a username, email, and password.



Start the Development Server:

python manage.py runserver



Access the Application:





Homepage: http://127.0.0.1:8000/



Admin Panel: http://127.0.0.1:8000/admin/
