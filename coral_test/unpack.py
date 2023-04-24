import tflite_runtime.interpreter as tflite
import platform



EDGETPU_SHARED_LIB = {
  'Linux': 'libedgetpu.so.1',
  'Darwin': 'libedgetpu.1.dylib',
  'Windows': 'edgetpu.dll'
}[platform.system()]


def make_interpreter(model_file):
  model_file, *device = model_file.split('@')
  return tflite.Interpreter(
      model_path=model_file,
      experimental_delegates=[
          tflite.load_delegate(EDGETPU_SHARED_LIB,
                               {'device': device[0]} if device else {})
      ])


# Load the TensorFlow Lite model
interpreter = make_interpreter("voice_commands_v0.7_edgetpu.tflite")
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
