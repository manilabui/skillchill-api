# 🤸🏻‍♀️ Skillchill REST API 🏋🏻‍♂️

Find me on: [Portfolio](www.manilabui.com)|[LinkedIn](https://www.linkedin.com/in/manilabui/)

## About

Skillchill is an app for those looking to track their progression on the skills they are learning and get feedback from others learning the same skills. As a lifelong student, I have several skills I would like to improve upon, such as powerlifting. 

Previously, I've posted my lifting videos on Instagram due to the ability to write notes about my sessions in the captions. It was a great format, but not the best platform, especially if you want to post about several skills. There isn't a good way to organize them on Instagram, and your followers probably don't want to be bombarded with your skill posts. My app allows users to categorize their posts according to their skills and follow only the skills that interest them.

## Installation

Requirements: Python 3

1. Clone this repository
   ```sh
   git clone https://github.com/manilabui/skillchill-api.git
   ```
1. Navigate to the project directory
   ```sh
   cd skillchill-api
   ```
1. Create your virtual environment
   ```sh
   python -m venv SkillchillEnv
   ```
1. Activate your virtual environment
   ```sh
   # for OSX environment in Terminal
   source ./bangazonenv/bin/activate
   
   # or for Windows environment in Command Line
   source ./bangazonenv/Scripts/activate
   ```
1. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
1. Build your database from the existing models
   ```sh
   python manage.py makemigrations skillchill-api
   python manage.py migrate
   ```
1. Populate your database with initial data from fixtures files (_NOTE: every time you run this it will remove existing data and repopulate the tables_)
   ```sh
   python manage.py loaddata */fixtures/*.json
   ```
1. Start your local development server
   ```sh
   python manage.py runserver
   ```
1. If your browser doesn't open and navigate to the app automatically, navigate to http://localhost:8000 to view it in the browser in development mode.
1. Make sure to start your local React client server. Found [here](https://github.com/manilabui/skillchill).
