import os
import sys
import dill
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Saves a python object (like a preprocessing pipeline or model) to a given file path.
    """
    try:
        dir_path = os.path.dirname(file_path)
        
        # Create directory if it does not exist
        os.makedirs(dir_path, exist_ok=True)

        # Save the object using dill
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)