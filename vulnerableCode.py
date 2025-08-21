

# HardCoded Credentials

def create_session_noncompliant():
    import boto3
    # Noncompliant: uses hardcoded secret access key.
    sample_key = "AjWnyxxxxx45xxxxZxxxX7ZQxxxxYxxx1xYxxxxx"
    boto3.session.Session(aws_secret_access_key=sample_key)

# sql injection

# def run_insecure_query(request):
#     import sqlite3

#     # Retrieve user input
#     username = request.GET.get("name")

#     # Build the SQL statement unsafely
    
#     sql_statement = f"SELECT * FROM Users WHERE name = {username};"

#     # Open the database connection
#     conn = sqlite3.connect("example.db")
#     try:
#         db = conn.cursor()
#         # Still unsafe: concatenated user input allows SQL injection
#         db.execute(sql_statement)
#         conn.commit()
#     finally:
#         conn.close()

####
# Resource Leak

def read_file_noncompliant(filename):
    file = open(filename, 'r')
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()



# insecure hashing

def hashing_noncompliant():
    import hashlib
    from hashlib import pbkdf2_hmac
    # Noncompliant: insecure hashing algorithm used.
    derivedkey = hashlib.pbkdf2_hmac('sha224', password, salt, 100000)
    derivedkey.hex()



# AWS Credentials logged

def log_credentials_noncompliant():
    import boto3
    import logging
    session = boto3.Session()
    credentials = session.get_credentials()
    credentials = credentials.get_frozen_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key
    # Noncompliant: credentials are written to the logger.
    logging.info('Access key: ', access_key)
    logging.info('secret access key: ', secret_key)


# Hardcoded IP address

def hardcoded_ip_address_noncompliant():
    sock = socket(AF_INET, SOCK_STREAM)
    # Noncompliant: IP address is hardcoded.
    sock.bind(('193.168.14.31', 80))


def change_file_permissions_noncompliant():
    import os
    import stat
    # Noncompliant: permissions assigned to all users.
    os.chmod("sample.txt", stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)



def execute_query_noncompliant(request):
    import sqlite3
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    with sqlite3.connect("example.db") as connection:
        cursor = connection.cursor()
        # Noncompliant: user input is used without sanitization.
        cursor.execute(query)
        connection.commit()
        connection.close()





