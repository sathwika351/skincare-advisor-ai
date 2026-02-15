# Configuration file for the Skin Analysis Application

# MongoDB Configuration
MONGO_URI = "mongodb+srv://thenoparkingtv:Abhi4123@cluster0.5crqooi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Change this to your MongoDB URI

# Flask Configuration
SECRET_KEY = "your-secret-key-here"
UPLOAD_FOLDER = "static/uploads"
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

# Model Configuration
MODEL_PATH = "model/cnn_model.h5"
IMAGE_SIZE = (128, 128)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Application Settings
DEBUG = True
HOST = "0.0.0.0"
PORT = 8080