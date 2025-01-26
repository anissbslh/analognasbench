from analognasbench import AnalogNASBench

# Initialize
benchmark = AnalogNASBench()

# Query a specific metric for an architecture
analog_accuracy = benchmark.query_metric((0, 0, 0, 4, 3, 2), 'analog_accuracy')

print("Analog Accuracy :",analog_accuracy)

# Get full architecture details
arch_details = benchmark.get_architecture_details((0, 1, 0, 4, 3, 2))
print(arch_details)
