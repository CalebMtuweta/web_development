from sqlalchemy import create_engine, text
import os


db_connection_string= os.environ['DB_CONNECTION_STRING']




engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                        }
                      })



    
def adding_users_to_the_db(Form):
    with engine.connect() as conn:
        query = text("INSERT INTO users (username,email,password,password_confirmation) VALUES (:username, :email, :password, :password_confirmation)")

        conn.execute(query, {
            'username': Form.username.data,
            'email': Form.email.data,
            'password': Form.password.data,
            'password_confirmation': Form.password_confirmation.data
        })
def get_user_by_email(email):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT password FROM users WHERE email = :email"), {"email": email})
        password = result.scalar()
        return password if password else None
