# Split data
X_train, X_test, y_binary_train, y_binary_test, y_multiclass_train, y_multiclass_test = train_test_split(
    X_pca, y_binary, y_multiclass, test_size=0.45, random_state=42, stratify=y_multiclass)

X_train, X_val, y_binary_train, y_binary_val, y_multiclass_train, y_multiclass_val = train_test_split(
    X_train, y_binary_train, y_multiclass_train, test_size=0.45, random_state=42, stratify=y_multiclass_train)

# For SVM - binary classification
C = 10.0
gamma = 0.05
svm = SVC(C=C, gamma=gamma, kernel='rbf')
svm.fit(X_train, y_binary_train)

# Evaluate SVM
y_binary_pred = svm.predict(X_test)
print(f"SVM Accuracy: {accuracy_score(y_binary_test, y_binary_pred):.4f}")
print("SVM Classification Report:")
print(classification_report(y_binary_test, y_binary_pred))

# For KNN - multiclass classification
n_neighbors = 5
p = 2  # Euclidean distance
knn = KNeighborsClassifier(n_neighbors=n_neighbors, p=p)
knn.fit(X_train, y_multiclass_train)

# Evaluate KNN
y_multiclass_pred = knn.predict(X_test)
print(f"KNN Accuracy: {accuracy_score(y_multiclass_test, y_multiclass_pred):.4f}")
print("KNN Classification Report:")
print(classification_report(y_multiclass_test, y_multiclass_pred))
