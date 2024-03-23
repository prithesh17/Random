import numpy as np  # Import NumPy library for array operations

# Define input and target data
inputs = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)  # Input data
targets = np.array(([92], [86], [89]), dtype=float)      # Target data

# Normalize input and target data
inputs = inputs / np.amax(inputs, axis=0)  # Normalizing input data
targets = targets / 100                     # Normalizing target data

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function
def derivative_sigmoid(x):
    return x * (1 - x)

# Define hyperparameters
epochs = 5000         # Number of training epochs
learning_rate = 0.1          # Learning rate for weight updates
input_layer_neurons = 2      # Number of neurons in the input layer
hidden_layer_neurons = 3     # Number of neurons in the hidden layer
output_layer_neurons = 1     # Number of neurons in the output layer

# Initialize weights and biases with random values
weights_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))  # Initialize weights for hidden layer
bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))                        # Initialize biases for hidden layer
weights_out = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))     # Initialize weights for output layer
bias_out = np.random.uniform(size=(1, output_layer_neurons))                            # Initialize biases for output layer

# Training loop
for i in range(epochs):
    # Forward pass
    hidden_input = np.dot(inputs, weights_hidden)  # Calculate input to hidden layer
    hidden_input += bias_hidden                    # Add bias to hidden layer input
    hidden_output = sigmoid(hidden_input)          # Apply activation function to hidden layer output

    output_input = np.dot(hidden_output, weights_out)  # Calculate input to output layer
    output_input += bias_out                            # Add bias to output layer input
    predicted_output = sigmoid(output_input)            # Apply activation function to output layer output

    # Backpropagation
    error_output = targets - predicted_output               # Calculate error in output layer
    output_derivative = derivative_sigmoid(predicted_output)  # Calculate derivative of sigmoid for output layer
    delta_output = error_output * output_derivative          # Calculate delta for output layer

    error_hidden = delta_output.dot(weights_out.T)              # Calculate error in hidden layer
    hidden_derivative = derivative_sigmoid(hidden_output)       # Calculate derivative of sigmoid for hidden layer
    delta_hidden = error_hidden * hidden_derivative             # Calculate delta for hidden layer

    # Update weights and biases
    weights_out += hidden_output.T.dot(delta_output) * learning_rate  # Update weights for output layer
    bias_out += np.sum(delta_output, axis=0) * learning_rate           # Update biases for output layer
    weights_hidden += inputs.T.dot(delta_hidden) * learning_rate       # Update weights for hidden layer
    bias_hidden += np.sum(delta_hidden, axis=0) * learning_rate        # Update biases for hidden layer

# Print results
print("Input:\n", inputs)
print("Actual Output:\n", targets)
print("Predicted Output:\n", predicted_output)
