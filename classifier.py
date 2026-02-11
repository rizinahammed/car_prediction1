import pickle
import warnings
import os
import yaml

# Load configuration from config.yml
with open("config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

model_name = config.get("model_name", "model.pkl")

def load_model():
    model_path = os.environ.get("MODEL_PATH", model_name)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        # Surface a clearer error for startup logs
        raise RuntimeError(f"Failed to load model from {model_path}: {e}") from e
