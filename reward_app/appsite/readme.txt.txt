# Django App Reward System

This is a simple Django project where:

- Users can register, login, and upload screenshots of app installations to earn reward points.
- Admins can log in separately to add and manage apps 

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/chikkurs/reward_app.git

cd appsite
python -m venv env
env\Scripts\activate   

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
