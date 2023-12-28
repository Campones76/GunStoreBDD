from nifverifier import generate_dead_ass_valid_nif

# Generate a valid NIF
# Valid initial values are: "1, 2, 3, 5, 6, 8, 9"
valid_nif = generate_dead_ass_valid_nif(initial_value="2")
print(valid_nif)