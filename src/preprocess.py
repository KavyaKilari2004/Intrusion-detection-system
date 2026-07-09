# One-hot encoding for categorical features
categorical_cols = ['protocol_type', 'service', 'flag']
df_encoded = df.copy()

for col in categorical_cols:
    one_hot = pd.get_dummies(df_encoded[col], prefix=col)
    df_encoded = df_encoded.drop(col, axis=1)
    df_encoded = df_encoded.join(one_hot)

print(f"Dataset shape after one-hot encoding: {df_encoded.shape}")

# Create binary labels (normal vs attack)
df_encoded['binary_label'] = df_encoded['attack_type'].apply(lambda x: 0 if x == 'normal' else 1)

# Create multi-class labels
def map_attack_type(attack):
    if attack == 'normal':
        return 'normal'
    elif attack in ['back', 'land', 'neptune', 'pod', 'smurf', 'teardrop', 'apache2', 'udpstorm', 
                     'processtable', 'worm', 'mailbomb']:
        return 'dos'
    elif attack in ['satan', 'ipsweep', 'nmap', 'portsweep', 'saint', 'mscan']:
        return 'probe'
    elif attack in ['buffer_overflow', 'loadmodule', 'perl', 'rootkit', 'sqlattack', 'xterm', 'ps']:
        return 'u2r'
    else:
        return 'r2l'  # phf, imap, multihop, warezmaster, etc.

df_encoded['attack_class'] = df_encoded['attack_type'].apply(map_attack_type)

# Encode multi-class labels
le = LabelEncoder()
df_encoded['attack_class_encoded'] = le.fit_transform(df_encoded['attack_class'])
class_mapping = dict(zip(le.transform(le.classes_), le.classes_))
print("Class mapping:", class_mapping)

# Prepare data for modeling
X = df_encoded.drop(['attack_type', 'binary_label', 'attack_class', 'attack_class_encoded'], axis=1)
y_binary = df_encoded['binary_label']
y_multiclass = df_encoded['attack_class_encoded']
