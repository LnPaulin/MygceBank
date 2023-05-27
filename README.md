This is a Django project that I built to create a blog that allows users to post past question papers of official exams for high school students. Users can also comment, browse through different categories and use the contact page to leave a message that is stored on the server.

Features
•  Users can create an account and log in to post past question papers in PDF format.

•  Users can edit and delete their own posts and view other users' posts.

•  Users can comment on any post and reply to other comments.

•  Users can browse through different categories of exams, such as Mathematics, English, Biology, etc.

•  Users can use the search bar to find posts by keywords or titles.

•  Users can use the contact page to send a message to the admin with their name, email and message. The messages are stored on the server and can be viewed by the admin.

•  Users can view their profile page and update their information and password.

Installation
To run this project locally, you will need Python 3.6 or higher and Django 3.2 or higher installed on your machine. You will also need a PostgreSQL database to store the data. You can install Django using pip:

pip install django

Then, clone this repository to your desired location:

git clone https://github.com/your_username/mygcebank.git

Navigate to the project directory and create a file named .env with the following content:

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port

Replace the values with your own. You can generate a secret key using this tool: https://djecrety.ir/.

Next, install the required packages using pip:

pip install -r requirements.txt

Then, run the following commands to create the database tables and a superuser account:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

Follow the prompts to enter your username, email and password for the superuser account.

Finally, run the following command to start the development server:

python manage.py runserver

You should see a message like this:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 27, 2023 - 21:15:39
Django version 3.2.4, using settings 'mygcebank.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Now you can open your browser and go to http://127.0.0.1:8000/ to see the project in action.

Usage
To use the blog, follow these steps:

•  To access the admin panel, go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials. Here you can manage the users, posts, comments, categories and messages.

•  To create a new user account, go to http://127.0.0.1:8000/register/ and fill in the form with your username, email and password. You will receive a confirmation email with a link to activate your account.

•  To log in to your account, go to http://127.0.0.1:8000/login/ and enter your username and password.

•  To create a new post, go to http://127.0.0.1:8000/new-post/ and fill in the form with your title, category and PDF file. You can also add a description if you want.

•  To edit or delete your post, go to http://127.0.0.1:8000/post/<post_id>/ and click on the edit or delete button below your post.

•  To view other users' posts, go to http://127.0.0.1:8000/posts/ and browse through the latest posts or use the filters on the sidebar to narrow down your search.

•  To comment on a post, go to http://127.0.0.1:8000/post/<post_id>/ and write your comment in the text box below the post. You can also reply to other comments by clicking on the reply button below each comment.

•  To view your profile page, go to http://127.0.0.1:8000/profile/ and see your information and posts.

•  To update your profile information or password, go to http://127.0.0.1:8000/profile/edit/ and fill in the form with your new details.

•  To contact the admin, go to http://127.0.0.1:8000/contact/ and fill in the form with your name, email and message.
