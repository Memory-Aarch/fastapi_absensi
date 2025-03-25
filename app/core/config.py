import os
from dotenv import load_dotenv

# Muat variabel dari file .env
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app/database.db")
    
    # The code above is a snippet from the config.py file in the core directory. 
    # This file contains the configuration for the application, such as the SECRET_KEY and DATABASE_URL variables. 
    # The SECRET_KEY variable is used to sign and verify JWT tokens, while the DATABASE_URL variable is used to connect to the database.
    # The load_dotenv() function is used to load environment variables from a .env file. 
    # This file should be placed in the root directory of the project and contain the following variables: 
    # SECRET_KEY=your_secret_key_here