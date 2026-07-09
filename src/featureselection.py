# Apply PCA for dimensionality reduction
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=0.95)
X_pca = pca.fit_transform(X_scaled)

print(f"Original features: {X.shape[1]}")
print(f"Features after PCA: {X_pca.shape[1]}")
print(f"Explained variance ratio: {sum(pca.explained_variance_ratio_):.4f}")

import numpy as np
import random

def hho_feature_selection(X, min_features=10, max_iterations=50, population_size=10):
    num_features = X.shape[1]  # Number of features

    # Initialize population (binary: 1 = select feature, 0 = ignore feature)
    population = np.random.randint(2, size=(population_size, num_features))

    # Fitness function (ensure at least min_features are selected)
    def fitness_function(selected_features):
        selected_count = np.sum(selected_features)
        if selected_count < min_features:  # Penalize if fewer than min_features
            return num_features  # Assign worst score
        return selected_count  # Minimize selected count while keeping at least min_features

    # Evaluate initial fitness
    fitness = np.array([fitness_function(ind) for ind in population])
    best_index = np.argmin(fitness)
    best_hawk = population[best_index].copy()
    best_fitness = fitness[best_index]

    # Main Optimization Loop
    for iteration in range(max_iterations):
        E1 = 2 * (1 - (iteration / max_iterations))  # Energy decreasing factor

        for i in range(population_size):
            E0 = 2 * random.random() - 1  # Random energy level
            E = E1 * E0  # Escape energy

            if abs(E) >= 1:  # Exploration Phase
                random_hawk = population[random.randint(0, population_size - 1)]
                new_hawk = random_hawk - random.random() * abs(random_hawk - best_hawk)

            else:  # Exploitation Phase
                new_hawk = best_hawk - E * abs(best_hawk - population[i])

            # Convert values to binary (0 or 1)
            new_hawk = np.where(new_hawk > 0.5, 1, 0)

            # Ensure at least min_features are selected
            while np.sum(new_hawk) < min_features:
                random_idx = np.random.randint(0, num_features)
                new_hawk[random_idx] = 1  # Force selection of random features

            # Evaluate new solution
            new_fitness = fitness_function(new_hawk)

            # Update population if the new solution is better
            if new_fitness < fitness[i]:
                population[i] = new_hawk
                fitness[i] = new_fitness

        # Update best solution
        new_best_index = np.argmin(fitness)
        if fitness[new_best_index] < best_fitness:
            best_hawk = population[new_best_index].copy()
            best_fitness = fitness[new_best_index]

        # Print progress
        if iteration % 10 == 0 or iteration == max_iterations - 1:
            print(f"Iteration {iteration+1}/{max_iterations} - Best Fitness: {best_fitness}")

    return best_hawk

#  Run HHO with at least 10 selected features
best_features = hho_feature_selection(X_pca, min_features=10)

# Extract selected features
selected_feature_indices = np.where(best_features == 1)[0]
X_selected = X_pca[:, selected_feature_indices]  # Apply feature selection

print("\n HHO Feature Selection Completed!")
print(f"Selected Features: {selected_feature_indices}")
print(f"Shape of X_selected: {X_selected.shape}")

print(selected_feature_indices)
print(X.columns[selected_feature_indices])
