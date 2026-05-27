import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import flwr as fl
import numpy as np
import pandas as pd
import random
import csv

from privacy.dp_utils import add_dp_noise

# ---------------- HOSPITAL INPUT ----------------

hospital_name = input(
    "Enter Hospital Name (A/B/C): "
).strip().upper()

# ---------------- PRIVACY BUDGET ----------------

privacy_budget = 0.5

print(
    f"\nPrivacy Budget (ε): {privacy_budget}"
)

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

print(
    f"\nLoaded Dataset for Hospital {hospital_name}"
)

print(df.head())

# ---------------- INITIAL MODEL WEIGHTS ----------------

weights = [

    np.array([1.0, 2.0, 3.0])

]

# ---------------- FEDERATED CLIENT ----------------

class HospitalClient(fl.client.NumPyClient):

    # Send parameters to server
    def get_parameters(self, config):

        return weights

    # ---------------- LOCAL TRAINING ----------------

    def fit(self, parameters, config):

        print(
            f"\nTraining locally at Hospital {hospital_name}..."
        )

        print(
            f"Number of patient records: {len(df)}"
        )

        # ---------------- SIMULATED LOCAL TRAINING ----------------

        updated_weights = [

            param + np.random.randn(*param.shape) * 0.1

            for param in parameters

        ]

        # ---------------- DIFFERENTIAL PRIVACY ----------------

        private_weights = add_dp_noise(

            updated_weights,

            noise_scale=0.05

        )

        print(
            f"Differential Privacy applied at Hospital {hospital_name}"
        )

        print(
            f"Noise Scale Applied: 0.05"
        )

        print(
            f"Hospital {hospital_name} completed local training."
        )

        return private_weights, len(df), {}

    # ---------------- EVALUATION ----------------

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

        # ---------------- SAVE METRICS ----------------

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

        print(
            f"Accuracy: {accuracy}"
        )

        print(
            f"Loss: {loss}"
        )

        return loss, len(df), {

            "accuracy": accuracy

        }

# ---------------- START CLIENT ----------------

fl.client.start_numpy_client(

    server_address="127.0.0.1:8080",

    client=HospitalClient()

)