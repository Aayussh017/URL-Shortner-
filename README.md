URLShortner-
This project is a web application built using the Django framework. It include functionalities to manage various URL's aspects of the application which shorten the URL

Project Structure The main components of the project include: 1.) ASGI Configuration: Manages asynchronous server gateway interface configuration. 2.) Settings Configuration: Contains all the settings and configuration for the Django project. 3.) URL Configuration: Handles the routing of URLs to appropriate views within the application.

How to Run the Project Clone the repository:

bash Copy code git clone https://github.com/Aayussh017/URLShortner.git

Navigate to the project directory: bash Copy code cd env

Create a virtual environment: bash Copy code python -m venv env Activate the virtual environment:

On Windows: bash Copy code .\env\Scripts\activate On macOS/Linux: bash Copy code source env/bin/activate

Install the dependencies: bash Copy code pip install -r requirements.txt Run the development server:

bash Copy code python manage.py runserver Access the application: Open your web browser and navigate to http://127.0.0.1:8000/.

