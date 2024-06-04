import numpy as np

# Padrão fornecido
pattern = [[1, 1, 1, 0, 1, 0, 0],
           [0, 1, 1, 1, 0, 1, 0],
           [1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 0, 0, 1, 1, 1],
           [0, 1, 1, 1, 0, 0, 1],
           [0, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1]]

print(len(pattern[0]))
def expand_pattern(pattern, new_shape):
    """
    Expand the given pattern to fit the new shape.

    Parameters:
        pattern (list): The input pattern.
        new_shape (tuple): The new shape of the expanded pattern.

    Returns:
        np.ndarray: The expanded pattern as a NumPy array.
    """
    # Get the dimensions of the pattern
    pattern_rows = len(pattern)
    pattern_cols = len(pattern[0])

    # Create a new matrix filled with zeros with the new shape
    expanded_pattern = np.zeros(new_shape, dtype=int)

    # Copy values from the pattern to the expanded pattern, repeating if necessary
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            expanded_pattern[i, j] = pattern[i % pattern_rows][j % pattern_cols]

    return expanded_pattern


# Define the new shape (30x30)
new_shape = (200, 200)

# Expand the pattern to fit the new shape
expanded_matrix = expand_pattern(pattern, new_shape)

# Salvar a matriz em um arquivo de texto com os elementos separados por vírgulas
np.savetxt("expanded_matrix.txt", expanded_matrix, fmt='%d')

# Print a mensagem informando que a matriz foi salva
print("A matriz expandida foi salva no arquivo 'expanded_matrix.txt'.")
