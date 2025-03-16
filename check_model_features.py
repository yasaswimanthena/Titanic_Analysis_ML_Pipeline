import pickle

# Load the trained model
with open("best_rf_model.pkl", "rb") as file:
    model = pickle.load(file)

# Print expected features
print("The model expects:", model.n_features_in_)
