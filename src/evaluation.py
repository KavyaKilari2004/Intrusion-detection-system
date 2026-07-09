# Visualize confusion matrices
plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
cm = confusion_matrix(y_binary_test, y_binary_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('SVM Confusion Matrix (Binary)')
plt.xlabel('Predicted')
plt.ylabel('Actual')

plt.subplot(1, 2, 2)
cm = confusion_matrix(y_multiclass_test, y_multiclass_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('KNN Confusion Matrix (Multiclass)')
plt.xlabel('Predicted')
plt.ylabel('Actual')

plt.tight_layout()
plt.show()

print("\nAnalysis complete! Confusion matrices saved as 'confusion_matrices.png'")
