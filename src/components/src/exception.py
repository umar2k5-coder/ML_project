import sys
from logger import logger
def error_message_detail(error, error_detail: sys):
    """
    Extracts the file name, line number, and error message from the system traceback.
    """
    # exc_info() returns a tuple: (type, value, traceback)
    # We only need the traceback object (exc_tb)
    _, _, exc_tb = error_detail.exc_info()
    
    # Extracting file name and line number from the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    # Formatting the error message
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Inherit from the base Exception class
        super().__init__(error_message)
        
        # Call our custom function to generate the detailed error message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        # When we print the exception, it will return our detailed string
        return self.error_message

if __name__ == "__main__":
    
    # Let's log a message to show the script started
    logger.info("Starting the division test...")
    
    try:
        a = 1 / 0
    except Exception as e:
        # 1. Generate the detailed error message
        detailed_error = CustomException(e, sys)
        
        # 2. LOG THE ERROR! This writes it to the file in your 'logs' folder
        logger.error(detailed_error)
        
        # Optional: Print a message to your terminal so you know it finished
        print("An error occurred. Check the logs folder for details!")