# schedule

Use a virtual environment: pip3 install virtualenv
Enter environment: source env/bin/activate
Install flask: flask-sqlalchemy, and requests
Add database: python3, >>> from app import app, db >>> app.app_context().push() >>> db.create_all() >>> exit()
Run using: python3 app.py