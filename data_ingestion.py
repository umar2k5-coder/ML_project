import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

# Importing custom modules from your project source
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion. 
    It defines the paths where the raw, train, and test data will be saved inside the artifacts folder.
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        # Initialize the config class to get access to the paths
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads the data, creates the artifacts folder, saves the raw data, 
        performs a train-test split, and saves the split datasets.
        """
        logging.info("Entered the data ingestion method")
        try:
            # 1. Read the data (Add your manual CSV path here)
            csv_path = r"O:\PROJECTS\ML_Project_1\notebook\data\stud.csv"  
            df = pd.read_csv(csv_path)
            logging.info(f"Read the dataset as a dataframe from: {csv_path}")

            # 2. Create the artifacts folder if it doesn't exist
            # exist_ok=True ensures it won't throw an error if the folder is already there
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # 3. Save the raw data to the artifacts folder
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Saved raw data to artifacts folder")

            # 4. Perform Train-Test Split
            logging.info("Initiating train-test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # 5. Save the train and test data separately
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and test data saved successfully")

            logging.info("Data Ingestion completed")

            # 6. Return the paths for the next stage (Data Transformation)
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Catching the exception and raising our custom exception with sys info
            logging.error("Exception occurred during data ingestion")
            raise CustomException(e, sys)

# Optional testing block so you can run this script directly to test it
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(f"Train data saved at: {train_data_path}")
    print(f"Test data saved at: {test_data_path}")