import flwr as fl

print("\nStarting MediChain Federated Server...\n")

# Configure federated strategy
strategy = fl.server.strategy.FedAvg(

    min_fit_clients=3,
    min_available_clients=3,
    min_evaluate_clients=3

)

# Start Flower server
fl.server.start_server(

    server_address="0.0.0.0:8080",

    config=fl.server.ServerConfig(
        num_rounds=3
    ),

    strategy=strategy

)