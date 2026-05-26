import flwr as fl
import numpy as np
import pandas as pd

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

# Load dataset
df = pd.read_csv(dataset_path)

print(f"\nLoaded Dataset for Hospital {hospital_name}")
print(df.head())

# ---------------- DUMMY MODEL PARAMETERS ----------------

weights = [np.array([1.0, 2.0, 3.0])]

# ---------------- FEDERATED CLIENT ----------------

class HospitalClient(fl.client.NumPyClient):

    def get_parameters(self, config):

        return weights

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

    def evaluate(self, parameters, config):

        loss = 0.1

        accuracy = 0.90

        return loss, len(df), {
            "accuracy": accuracy
        }

# ---------------- START CLIENT ----------------

fl.client.start_numpy_client(

    server_address="127.0.0.1:8080",

    client=HospitalClient()

)