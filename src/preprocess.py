# Identify categorical and numerical features
categorical_features = ['protocol_type', 'service', 'flag']
numerical_features = [col for col in df.columns if col not in categorical_features + ['attack_type']]

# Create preprocessor with one-hot encoding for categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Preprocess data
X = df.drop('attack_type', axis=1)
y = df['attack_type']

# Transform data
print("Applying preprocessing transformations...")
X_transformed = preprocessor.fit_transform(X)

# Get feature names after one-hot encoding
cat_feature_names = preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)
feature_names = numerical_features + list(cat_feature_names)
print(f"Total features after one-hot encoding: {len(feature_names)}")

# Create binary classification datasets for each attack type
print("Creating binary classification datasets...")

def create_binary_dataset(df, attack_type):
    binary_df = df.copy()
    binary_df['label'] = binary_df['attack_type'].apply(lambda x: 1 if x == attack_type else 0)
    return binary_df

# Create binary datasets
dos_df = create_binary_dataset(df, 'DoS')
probe_df = create_binary_dataset(df, 'Probe')
r2l_df = create_binary_dataset(df, 'R2L')
u2r_df = create_binary_dataset(df, 'U2R')

# Function to preprocess and split binary datasets
def preprocess_binary_dataset(binary_df):
    X_bin = binary_df.drop(['attack_type', 'label'], axis=1)
    y_bin = binary_df['label']
    
    # Transform data
    X_bin_transformed = preprocessor.transform(X_bin)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_bin_transformed, y_bin, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test

# Process each attack type
X_DoS_train, X_DoS_test, Y_DoS_train, Y_DoS_test = preprocess_binary_dataset(dos_df)
X_Probe_train, X_Probe_test, Y_Probe_train, Y_Probe_test = preprocess_binary_dataset(probe_df)
X_R2L_train, X_R2L_test, Y_R2L_train, Y_R2L_test = preprocess_binary_dataset(r2l_df)
X_U2R_train, X_U2R_test, Y_U2R_train, Y_U2R_test = preprocess_binary_dataset(u2r_df)

print("Data preprocessing complete.")
