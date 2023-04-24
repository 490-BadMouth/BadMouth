import tensorflow as tf

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter("4c_64n_10e_LN_edgetpu.tflite")
interpreter.allocate_tensors()

# Get information about the input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("Input details:", input_details)
print("Output details:", output_details)

# Print the values of the weights and biases of each tensor
for detail in input_details + output_details:
    tensor = interpreter.tensor(detail["index"])
    print(detail["name"], tensor())
