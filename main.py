# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)