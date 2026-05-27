# Differential Privacy in MediChain

MediChain uses Differential Privacy concepts
to protect sensitive healthcare information
during Federated Learning.

Instead of sharing raw model updates,
controlled random noise is added before
sending parameters to the federated server.

This helps reduce the risk of patient
data reconstruction attacks while still
allowing collaborative AI learning.