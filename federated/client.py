import flwr as fl
import numpy as np
import pandas as pd
import random
import csv

# ---------------- HOSPITAL INPUT ----------------

hospital_name = input(
    "Enter Hospital Name (A/B/C): "
).strip().upper()

# ---------------- LOAD HOSPITAL DATA ----------------

dataset_path = ""

if hospital_name == "A":

    dataset_path = "datasets/hospital_a.csv"

elif hospital_name == "B":

    dataset_path = "datasets/hospital_b.csv"

elif hospital_name == "C":

    dataset_path = "datasets/hospital_c.csv"

else:

    print("Invalid hospital selected.")
    exit()

# ---------------- LOAD DATASET ----------------

df = pd.read_csv(dataset_path)

print(f"\nLoaded Dataset for Hospital {hospital_name}")

print(df.head())

# ---------------- INITIAL MODEL WEIGHTS ----------------

weights = [

    np.array([1.0, 2.0, 3.0])

]

# ---------------- FEDERATED CLIENT ----------------

class HospitalClient(fl.client.NumPyClient):

    # Send model parameters to server
    def get_parameters(self, config):

        return weights

    # Local training
    def fit(self, parameters, config):

        print(
            f"\nTraining locally at Hospital {hospital_name}..."
        )

        print(
            f"Number of patient records: {len(df)}"
        )

        # Simulated local training
        updated_weights = [

            param + np.random.randn(*param.shape) * 0.1

            for param in parameters
        ]

        print(
            f"Hospital {hospital_name} completed local training."
        )

        return updated_weights, len(df), {}

    # Evaluation
    def evaluate(self, parameters, config):

        # Simulated metrics
        loss = round(

            random.uniform(0.05, 0.20),

            3

        )

        accuracy = round(

            random.uniform(0.80, 0.98),

            3

        )

        current_round = config.get(
            "server_round",
            1
        )

        # Save metrics to CSV
        with open(

            "federated/metrics/training_metrics.csv",

            mode="a",

            newline=""

        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                current_round,

                hospital_name,

                accuracy,

                loss

            ])

        print(
            f"\nHospital {hospital_name} Evaluation"
        )

        print(f"Accuracy: {accuracy}")

        print(f"Loss: {loss}")

        return loss, len(df), {

            "accuracy": accuracy

        }

# ---------------- START CLIENT ----------------

fl.client.start_numpy_client(

    server_address="127.0.0.1:8080",

    client=HospitalClient()

)