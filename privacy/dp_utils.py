import numpy as np

# ---------------- DIFFERENTIAL PRIVACY ----------------

def add_dp_noise(parameters, noise_scale=0.05):

    noisy_parameters = []

    for param in parameters:

        noise = np.random.normal(

            loc=0.0,

            scale=noise_scale,

            size=param.shape

        )

        noisy_param = param + noise

        noisy_parameters.append(noisy_param)

    return noisy_parameters