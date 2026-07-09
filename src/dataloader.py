import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the NSL-KDD dataset
col_names = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", 
            "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", 
            "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells", 
            "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count", 
            "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", 
            "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", 
            "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", 
            "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate", 
            "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", 
            "attack_type"]
train_url = 'https://raw.githubusercontent.com/merteroglu/NSL-KDD-Network-Instrusion-Detection/master/NSL_KDD_Train.csv'
test_url = 'https://raw.githubusercontent.com/merteroglu/NSL-KDD-Network-Instrusion-Detection/master/NSL_KDD_Test.csv'
df_train = pd.read_csv(train_url,header=None, names = col_names)
df_test = pd.read_csv(test_url, header=None, names = col_names)
df=pd.concat([df_train,df_test],ignore_index=True)
print(f"Dataset shape: {df.shape}")
