from app import create_app

app = create_app()
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

#pip install python-dotenv
#apt-get install python3-mysqldb

# ORM que se va a utilizar:

# pip install flask_sqlalchemy
#pip install PyMySQL
#pip install cryptography