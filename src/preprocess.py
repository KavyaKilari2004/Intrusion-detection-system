# One-hot encoding for categorical features
categorical_cols = ['protocol_type', 'service', 'flag']
df_encoded = df.copy()

for col in categorical_cols:
    one_hot = pd.get_dummies(df_encoded[col], prefix=col)
    df_encoded = df_encoded.drop(col, axis=1)
    df_encoded = df_encoded.join(one_hot)

print(f"Dataset shape after one-hot encoding: {df_encoded.shape}")
