import os
DB_CONFIG = {
  "PSQL": {
    "HOST": os.getenv("ZTF_HOST"),
    "DB_NAME": os.getenv("ZTF_DATABASE"),
    "USER": os.getenv("ZTF_USER"),
    "PASSWORD": os.getenv("ZTF_PASSWORD"),
    "PORT": 5432,
  }
}

PROFILE = True

PROFILE_CONFIG = {
    "enabled": PROFILE,
    "storage": {
        "engine": "sqlalchemy",
        "db_url": f"postgresql://{DB_CONFIG['PSQL']['USER']}:{DB_CONFIG['PSQL']['PASSWORD']}@{DB_CONFIG['PSQL']['HOST']}:{DB_CONFIG['PSQL']['PORT']}/{DB_CONFIG['PSQL']['DB_NAME']}"
    },
    "basicAuth":{
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
	    "^/static/.*"
	]
}
