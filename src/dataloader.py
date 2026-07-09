import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report, confusion_matrix
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')

def load_kdd_data(filepath):
    print("Loading KDD Cup dataset...")
    
    # Column names for KDD Cup dataset
    col_names = [
        'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
        'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
        'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations',
        'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
        'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
        'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate',
        'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
        'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
        'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
        'dst_host_srv_rerror_rate', 'attack_type'
    ]
    
    # Load the data
    # For demonstration, using a placeholder. Replace with actual file loading:
    # df = pd.read_csv(filepath, names=col_names, header=None)
    
    # For demonstration, we'll create synthetic data instead
    from sklearn.datasets import make_classification
    
    print("Creating synthetic data for demonstration...")
    # Creating synthetic data with 41 features (like KDD Cup)
    X, y = make_classification(n_samples=500, n_features=41, n_informative=20, 
                             n_redundant=10, n_classes=5, random_state=42)
    
    # Create a DataFrame with proper column names
    df = pd.DataFrame(X, columns=col_names[:-1])
    
    # Add attack_type column (5 classes: normal, DoS, Probe, R2L, U2R)
    attack_labels = ['normal', 'DoS', 'Probe', 'R2L', 'U2R']
    df['attack_type'] = [attack_labels[label] for label in y]
    
    # Add categorical features for demonstration
    df['protocol_type'] = np.random.choice(['tcp', 'udp', 'icmp'], size=len(df))
    df['service'] = np.random.choice(['http', 'smtp', 'ftp', 'ssh', 'telnet'], size=len(df))
    df['flag'] = np.random.choice(['SF', 'S0', 'REJ', 'RSTO', 'RSTR'], size=len(df))
    
    print(f"Dataset created with shape: {df.shape}")
    
    return df

# Load the dataset
# In real implementation, use: df = load_kdd_data('path/to/kddcup.data')
df = load_kdd_data('NSL_KDD.csv')
