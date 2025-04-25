import itertools
import random

# Define detailed components of a landscape prompt
landscape_features = [
    "rolling green hills with wildflowers scattered across",
    "majestic snow-capped mountains towering over a pine forest",
    "a vast, sun-baked desert with undulating dunes",
    "a dense, ancient forest with towering redwoods and a carpet of ferns",
    "a serene alpine lake surrounded by rocky cliffs and evergreen trees",
    "a meandering river cutting through a deep gorge with steep, rocky walls",
    "a pristine sandy beach with crystal-clear turquoise waters and gentle waves",
    "a rugged coastline with crashing waves and jagged cliffs",
    "a meadow covered in colorful wildflowers swaying in a gentle breeze",
    "a rocky plateau with sparse vegetation under a vast, open sky",
    "a tropical island with white sandy beaches and lush, green jungles",
    "a barren tundra with patches of snow and low-lying shrubs",
    "a verdant valley with a winding river and grazing wildlife",
    "steep cliffs with cascading waterfalls plunging into a deep pool below",
    "a lush jungle with dense foliage and vibrant, exotic flowers",
    "an arid canyon with towering red rock formations and a winding river below",
    "a vineyard with rows of grapevines stretching towards distant hills",
    "terraced rice fields cascading down a mountainside with a reflective surface",
    "a wind farm on rolling hills with giant wind turbines spinning",
    "a sunflower field in full bloom under a bright blue sky"
]

environments = [
    "a rugged mountain range filled with wild, untouched beauty",
    "a sprawling desert that stretches as far as the eye can see",
    "an ancient forest filled with towering trees and a rich variety of wildlife",
    "a secluded beach with fine, white sand and a calm sea",
    "a tranquil lake surrounded by high peaks and dense woodland",
    "a fast-flowing river winding through a narrow canyon",
    "a flower-strewn meadow nestled in a quiet valley",
    "a tropical jungle bursting with vibrant colors and teeming with life",
    "a vast canyon carved out by millennia of flowing water",
    "a quiet valley enclosed by steep mountains and lush vegetation",
    "a frozen tundra where the ground is covered in a thick layer of ice and snow",
    "a remote island paradise with lush greenery and sparkling waters",
    "a vast wetland with tall reeds swaying in the wind and birds flying overhead",
    "a high plateau with sparse vegetation and a panoramic view of the landscape below",
    "a grassy savannah dotted with acacia trees and grazing animals",
    "a rolling prairie with tall grasses swaying in the wind and endless skies",
    "a misty moorland with heather-covered hills and low-lying fog",
    "a swampy area with gnarled trees and murky waters, filled with the sounds of wildlife"
]

weather_conditions = [
    "under a clear blue sky, with bright sunshine illuminating the landscape",
    "during a dramatic thunderstorm, with dark clouds and flashes of lightning",
    "in thick, rolling fog that shrouds the area in mystery",
    "on a rainy day, with raindrops pattering on leaves and the ground becoming muddy",
    "under overcast skies, with a soft, diffused light that casts no shadows",
    "on a scorching hot day, with heat waves shimmering above the ground",
    "during a heavy snowstorm, with thick snowflakes falling and accumulating quickly",
    "in a heavy downpour, with sheets of rain obscuring the view and water streaming down",
    "under a bright full moon, casting a silvery glow over the landscape",
    "with a rainbow arching across the sky after a recent rain shower",
    "on a windy day, with strong gusts blowing leaves and dust through the air",
    "during a calm evening, with a gentle breeze and the last light of day fading"
]

times_of_day = [
    "at sunrise, with the first light of day casting a golden glow over the scene",
    "at noon, when the sun is high in the sky and shadows are at their shortest",
    "in the late afternoon, with long shadows stretching across the ground",
    "at sunset, with the sky ablaze in shades of orange, pink, and purple",
    "at twilight, with the soft glow of the setting sun and the first stars appearing",
    "at night, under a starry sky with the Milky Way visible above",
    "in the early morning, with dew on the grass and a fresh, crisp feel to the air",
    "at dawn, as the sky begins to brighten and the world awakens"
]

# Generate all possible combinations using itertools.product
all_combinations = list(itertools.product(landscape_features, environments, weather_conditions, times_of_day))

# Shuffle the combinations to ensure randomness
random.shuffle(all_combinations)

# Create a list to hold the generated prompts
prompts = []

# Format each combination into a detailed descriptive prompt
for feature, environment, weather, time in all_combinations:
    prompt = f"A landscape photo of {feature} in {environment}, {weather} {time}."
    prompts.append(prompt)

# Limit to 10,000 prompts if there are more combinations
prompts = prompts[:10000]

# Example of displaying some prompts
for i, prompt in enumerate(prompts[:10]):
    print(f"{i+1}: {prompt}")

# Save the prompts to a file (optional)
with open("prompts_landscapes.txt", "w") as file:
    for prompt in prompts:
        file.write(prompt + "\n")
