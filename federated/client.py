import flwr as fl
import numpy as np

# Ask hospital name
hospital_name = input("Enter Hospital Name: ")

# Dummy model weights
weights = [
    np.array([1.0, 2.0, 3.0])
]

# Federated Client
class HospitalClient(fl.client.NumPyClient):

    def get_parameters(self, config):

        return weights

    def fit(self, parameters, config):

        print(f"\nTraining happening at {hospital_name}...\n")

        updated_weights = [

            param + np.random.randn(*param.shape) * 0.1

            for param in parameters
        ]

        return updated_weights, 10, {}

    def evaluate(self, parameters, config):

        loss = 0.1
        accuracy = 0.90

        return loss, 10, {
            "accuracy": accuracy
        }

# Start Client
fl.client.start_numpy_client(

    server_address="127.0.0.1:9090",

    client=HospitalClient()

)