from dotenv import load_dotenv, dotenv_values

environ = dotenv_values(".env")
USER_TOKEN = environ["USER_TOKEN"]
PARTNER_TOKEN = environ["PARTNER_TOKEN"]
PARTNER_ID = environ["PARTNER_ID"]

company_id = environ["company_id"]

user_id = environ["user_id"]
HEADERS = {
    "Authorization": f"Bearer {PARTNER_TOKEN}, User {USER_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/vnd.api.v2+json",
}


user = environ["DATABASE_USER"]
password = environ["DATABASE_PASSWORD"]
host = environ["DATABASE_HOST"]
port = environ["DATABASE_PORT"]
database = environ["DATABASE_NAME"]
