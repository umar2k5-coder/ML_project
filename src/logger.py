import logging
import os
from datetime import datetime

# 1. Generate a unique log file name based on the current timestamp
LOG_FILE_NAME = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# 2. Get the main project directory 
# os.path.abspath(__file__) gets the exact path of THIS logger.py file
# os.path.dirname() gets the folder containing this file (your main project folder)
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# 3. Define the path where the logs folder will be created inside the project root
LOGS_DIR = os.path.join(PROJECT_ROOT_DIR, "logs")

# 4. Create the logs directory if it doesn't already exist
os.makedirs(LOGS_DIR, exist_ok=True)

# 5. Create the full file path for the current log file
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE_NAME)

# 6. Configure the global logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, # Sets the default logging level
)

# Optional: You can instantiate a custom logger object to export
logger = logging.getLogger("ml_project_logger")

