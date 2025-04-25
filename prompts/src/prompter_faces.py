import random

# Define the lists of options
ethnicities = ["african", "asian", "thai", "south american", "caucasian", "indian", "hispanic", "mediterranian", "carribean", "arab"]
ages = ["adult", "teenager", "old"]
genders = ["male", "female"]
hair_lengths = ["long", "short", "no"]
hair_type = ["straight", "curly", "wavy"]
hair_colors = ["brown", "blonde", "black", "red"]
expressions = ["happy", "disgusted", "angry", "sad", "surprised", "scared"]
accessories = ["earrings", "sunglasses", "glasses", "piercings", ""]
backgrounds = ["a white wall", "a forest", "a beach", "a mountain", "the savana", "the skyline"]

# Function to generate a random prompt
def generate_prompt():
    hair = random.choice(hair_lengths)
    accesory = random.choice(accessories)
    if accesory == "":
        return f"Head and shoulder photo of an {random.choice(ethnicities)} {random.choice(ages)} {random.choice(genders)} with {hair} {random.choice(hair_type) if hair != 'no' else ''} hair and natural textured skin, the subject is {random.choice(expressions)}, in the background is visible a {random.choice(backgrounds)}."
    else:    
        return f"Head and shoulder photo of an {random.choice(ethnicities)} {random.choice(ages)} {random.choice(genders)} with {hair} {random.choice(hair_type) if hair != 'no' else ''} hair and natural textured skin, the subject has {accesory} and is {random.choice(expressions)}, in the background is visible a {random.choice(backgrounds)}."

# Generate 40,000 random prompts
prompts = [generate_prompt() for _ in range(10000)]

# Print the first 10 prompts to verify
for prompt in prompts[:10]:
    print(prompt)

# Optionally, save the prompts to a file
with open("prompts_faces2.txt", "w") as file:
    for prompt in prompts:
        file.write(prompt + "\n")
