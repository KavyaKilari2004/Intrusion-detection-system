print("\n--- Baseline LDA Performance ---")

def evaluate_base_lda(X_train, y_train, X_test, y_test, attack_type):
    lda = LinearDiscriminantAnalysis()
    
    start_time = time.time()
    lda.fit(X_train, y_train)
    y_pred = lda.predict(X_test)
    execution_time = time.time() - start_time
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    print(f"{attack_type} Attack - LDA Baseline:")
    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall: {recall:.4f}")
    print(f"  F1-Score: {f1:.4f}")
    print(f"  Detection Time: {execution_time:.4f} seconds")
    
    return accuracy

# Get baseline performance
acc_dos = evaluate_base_lda(X_DoS_train, Y_DoS_train, X_DoS_test, Y_DoS_test, "DoS")
acc_probe = evaluate_base_lda(X_Probe_train, Y_Probe_train, X_Probe_test, Y_Probe_test, "Probe")
acc_r2l = evaluate_base_lda(X_R2L_train, Y_R2L_train, X_R2L_test, Y_R2L_test, "R2L")
acc_u2r = evaluate_base_lda(X_U2R_train, Y_U2R_train, X_U2R_test, Y_U2R_test, "U2R")
