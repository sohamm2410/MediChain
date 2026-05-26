import pandas as pd
import matplotlib.pyplot as plt

# Load metrics
df = pd.read_csv(
    "federated/metrics/training_metrics.csv"
)

print("\nTraining Metrics:\n")
print(df)

# ---------------- ACCURACY PLOT ----------------

plt.figure(figsize=(8, 5))

for hospital in df["hospital"].unique():

    hospital_data = df[
        df["hospital"] == hospital
    ]

    plt.plot(

        hospital_data["round"],

        hospital_data["accuracy"],

        marker="o",

        label=f"Hospital {hospital}"

    )

plt.title("Federated Training Accuracy")

plt.xlabel("Training Round")

plt.ylabel("Accuracy")

plt.legend()

plt.grid(True)

plt.show()

# ---------------- LOSS PLOT ----------------

plt.figure(figsize=(8, 5))

for hospital in df["hospital"].unique():

    hospital_data = df[
        df["hospital"] == hospital
    ]

    plt.plot(

        hospital_data["round"],

        hospital_data["loss"],

        marker="o",

        label=f"Hospital {hospital}"

    )

plt.title("Federated Training Loss")

plt.xlabel("Training Round")

plt.ylabel("Loss")

plt.legend()

plt.grid(True)

plt.show()