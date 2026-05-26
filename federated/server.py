from flwr.server import start_server, ServerConfig

# Start Flower Federated Learning Server
start_server(

    server_address="127.0.0.1:9090",

    config=ServerConfig(
        num_rounds=3
    )

)


