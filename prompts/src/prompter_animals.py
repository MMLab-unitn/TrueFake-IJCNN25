import random

# Python dictionary with habitats as keys and lists of animals as values
habitat_animals = [
    {
        "habitat": ["savannah"], 
        "animals": ["lion", "elephant", "cheetah", "giraffe", "zebra", "hyena", "gazelle", "ostrich", "secretary bird"] #9
    },
    {
        "habitat": ["jungle", "rainforest"], 
        "animals": ["tiger", "jaguar", "gorilla", "python", "chimpanzee", "sloth", "tamarin monkey", "okapi", "anaconda", "capuchin monkey"] #10
    },
    {
        "habitat": ["desert"], 
        "animals": ["camel", "fennec fox", "meerkat", "desert tortoise", "scorpion", "jerboa", "rattlesnake", "dromedary", "roadrunner", "sand cat"] #10
    },
    {
        "habitat": ["ocean", "reef"], 
        "animals": ["dolphin", "blue whale", "great white shark", "manta ray", "sea turtle", "octopus", "swordfish", "sea lion", "clownfish", "starfish", "jellyfish"] #11
    },
    {
        "habitat": ["mountains", "forest", "glade"], 
        "animals": ["mountain goat", "snow leopard", "eagle", "deer", "red fox", "bear", "marmot", "wolf", "moose", "lynx"] #10
    },
    {
        "habitat": ["riverbank"], 
        "animals": ["beaver", "crocodile", "kingfisher", "otter", "capybara", "platypus", "heron", "hippopotamus"] #8
    },
    {
        "habitat": ["grassland", "field", "meadow"], 
        "animals": ["bison", "rabbit", "field mouse", "badger", "ferret", "coyote", "red fox", "hare", "squirrel", "cow", "cat", "dog"] #12
    },
    {
        "habitat": ["beach"], 
        "animals": ["sea gull", "crab", "sea turtle", "pelican", "plover", "hermit crab"] #6
    }
]

animal_properties = {
    "lion": ("hunter", "carnivore", "land"),
    "elephant": ("prey", "herbivore", "land"),
    "cheetah": ("hunter", "carnivore", "land"),
    "giraffe": ("prey", "herbivore", "land"),
    "zebra": ("prey", "herbivore", "land"),
    "hyena": ("hunter", "carnivore", "land"),
    "gazelle": ("prey", "herbivore", "land"),
    "ostrich": ("prey", "herbivore", "land"),
    "secretary bird": ("hunter", "carnivore", "land"),
    "tiger": ("hunter", "carnivore", "land"),
    "jaguar": ("hunter", "carnivore", "land"),
    "gorilla": ("prey", "herbivore", "land"),
    "python": ("hunter", "carnivore", "land"),
    "chimpanzee": ("hunter", "omnivore", "land"),
    "sloth": ("prey", "herbivore", "land"),
    "tamarin monkey": ("prey", "omnivore", "land"),
    "okapi": ("prey", "herbivore", "land"),
    "anaconda": ("hunter", "carnivore", "water/land"),
    "capuchin monkey": ("prey", "omnivore", "land"),
    "camel": ("prey", "herbivore", "land"),
    "fennec fox": ("hunter", "omnivore", "land"),
    "meerkat": ("hunter", "omnivore", "land"),
    "desert tortoise": ("prey", "herbivore", "land"),
    "scorpion": ("hunter", "carnivore", "land"),
    "jerboa": ("prey", "herbivore", "land"),
    "rattlesnake": ("hunter", "carnivore", "land"),
    "dromedary": ("prey", "herbivore", "land"),
    "roadrunner": ("hunter", "omnivore", "land"),
    "sand cat": ("hunter", "carnivore", "land"),
    "dolphin": ("hunter", "carnivore", "water"),
    "blue whale": ("prey", "herbivore", "water"),
    "great white shark": ("hunter", "carnivore", "water"),
    "manta ray": ("hunter", "omnivore", "water"),
    "sea turtle": ("prey", "omnivore", "water"),
    "octopus": ("hunter", "carnivore", "water"),
    "swordfish": ("hunter", "carnivore", "water"),
    "sea lion": ("hunter", "carnivore", "water"),
    "clownfish": ("prey", "omnivore", "water"),
    "starfish": ("prey", "omnivore", "water"),
    "mountain goat": ("prey", "herbivore", "land"),
    "snow leopard": ("hunter", "carnivore", "land"),
    "eagle": ("hunter", "carnivore", "land"),
    "deer": ("prey", "herbivore", "land"),
    "red fox": ("hunter", "omnivore", "land"),
    "bear": ("hunter", "omnivore", "land"),
    "marmot": ("prey", "herbivore", "land"),
    "wolf": ("hunter", "carnivore", "land"),
    "moose": ("prey", "herbivore", "land"),
    "lynx": ("hunter", "carnivore", "land"),
    "beaver": ("prey", "herbivore", "land"),
    "crocodile": ("hunter", "carnivore", "water/land"),
    "kingfisher": ("hunter", "carnivore", "land"),
    "otter": ("hunter", "carnivore", "water/land"),
    "capybara": ("prey", "herbivore", "land"),
    "platypus": ("hunter", "carnivore", "water/land"),
    "heron": ("hunter", "carnivore", "land"),
    "hippopotamus": ("prey", "herbivore", "water/land"),
    "bison": ("prey", "herbivore", "land"),
    "rabbit": ("prey", "herbivore", "land"),
    "field mouse": ("prey", "omnivore", "land"),
    "badger": ("hunter", "omnivore", "land"),
    "ferret": ("hunter", "carnivore", "land"),
    "coyote": ("hunter", "omnivore", "land"),
    "hare": ("prey", "herbivore", "land"),
    "squirrel": ("prey", "omnivore", "land"),
    "cow": ("prey", "herbivore", "land"),
    "cat": ("hunter", "carnivore", "land"),
    "dog": ("hunter", "omnivore", "land"),
    "sea gull": ("prey", "omnivore", "land"),
    "crab": ("prey", "omnivore", "water"),
    "pelican": ("prey", "omnivore", "land"),
    "plover": ("hunter", "omnivore", "land"),
    "hermit crab": ("prey", "omnivore", "water"),
    "jellyfish": ("hunter", "carnivore", "water")
}

# Python dictionary with combinations of properties as keys and lists of possible actions as values
animal_actions_by_properties = {
    # Hunter - Land
    ("hunter", "carnivore", "land"): [
        "hunting for prey", "stalking quietly through the underbrush", "resting under a tree", "roaring to assert dominance",
        "climbing a tree", "drinking water from a river", "playing with its young", "grooming its fur", "guarding its territory", "pouncing on a small animal"
    ],
    ("hunter", "omnivore", "land"): [
        "foraging for food", "hunting small animals", "digging for roots or insects", "resting in a burrow",
        "climbing rocks", "sniffing around for food", "scavenging leftovers", "marking territory", "playing with pack members", "exploring the surroundings"
    ],
    ("hunter", "carnivore", "water/land"): [
        "hunting along the water's edge", "basking in the sun", "sliding into the water", "lurking in shallow waters",
        "ambushing prey", "sunning on a riverbank", "diving into water", "floating near the surface", "building a nest on the shore", "resting in the reeds"
    ],

    # Hunter - Water
    ("hunter", "carnivore", "water"): [
        "swimming swiftly through the water", "hunting fish", "diving deep into the ocean", "chasing after prey",
        "surfacing for air", "resting on a coral reef", "gliding through waves", "spouting water", "communicating with others", "playing with pod members"
    ],
    ("hunter", "omnivore", "water"): [
        "scavenging for food", "catching small fish or crustaceans", "floating near the water surface", "hunting for mollusks",
        "swimming around coral reefs", "resting in shallow waters", "diving for algae", "grooming itself", "playing with seaweed", "interacting with other marine animals"
    ],

    # Prey - Land
    ("prey", "herbivore", "land"): [
        "grazing on grass", "drinking from a stream", "resting in the shade", "watching for predators",
        "grooming itself", "playing with others", "running from a predator", "scratching against a tree", "nursing its young", "foraging for food"
    ],
    ("prey", "omnivore", "land"): [
        "foraging for nuts and seeds", "scavenging for leftovers", "drinking water from a stream", "watching for predators",
        "nesting in a tree", "playing in the foliage", "hiding in a burrow", "running away from danger", "eating fruits", "gathering food for storage"
    ],

    # Prey - Water
    ("prey", "herbivore", "water"): [
        "grazing on underwater plants", "hiding among coral reefs", "drinking from a freshwater spring", "nurturing its young",
        "playing with others in a pod", "swimming in shallow waters", "resting on the water surface", "basking in the sun", "floating gently with the currents", "exploring seagrass beds"
    ],
    ("prey", "omnivore", "water"): [
        "foraging along the shoreline", "catching small fish", "hiding under rocks", "swimming through mangroves",
        "scavenging for food scraps", "digging in the sand", "resting in shallow water", "fleeing from predators", "floating near the surface", "playing in the waves"
    ],

    # Hunter - Land/Water
    ("hunter", "carnivore", "water/land"): [
        "hunting in shallow water", "resting on a riverbank", "sliding into the water to ambush prey", "basking in the sun",
        "diving for fish", "emerging from the water", "swimming near the shore", "waiting motionlessly", "playing in the water", "guarding its territory along the shore"
    ],

    # Prey - Water/Land
    ("prey", "herbivore", "water/land"): [
        "grazing on the riverbank", "wading in shallow water", "hiding in the reeds", "nurturing its young",
        "drinking from the river", "playing near the water's edge", "crossing a shallow stream", "resting on a grassy shore", "fleeing into the water", "swimming leisurely"
    ],
}

habitat_details = {
    "savannah": [
        "Under a scorching midday sun, with a distant heat haze",
        "During a dry season, with cracked earth and sparse trees",
        "At dawn, with the ground cool and dew-covered grasses",
        "On a windy evening, with dust swirling around the tall grass",
        "Under a vast, cloudless sky, with the sun setting in the distance"
    ],
    "jungle": [
        "In dense vegetation, with humidity thick and air heavy",
        "Under a canopy of leaves, during a sudden downpour",
        "On a misty morning, with the calls of hidden birds",
        "Amid the tangled vines, with shafts of light breaking through",
        "During the monsoon season, with muddy trails and flowing rivers"
    ],
    "rainforest": [
        "In a dense fog, with the sounds of dripping water",
        "During a heavy rainfall, with water cascading off leaves",
        "Under the green canopy, with rays of sunlight filtering down",
        "In the early morning mist, with the calls of exotic birds",
        "On a warm, humid afternoon, with insects buzzing around"
    ],
    "desert": [
        "Under the blazing midday sun, with the air shimmering",
        "During a rare rainstorm, with rivulets forming in the sand",
        "At night, with a clear sky full of stars and a cold breeze",
        "On a windy day, with sand dunes shifting and swirling",
        "In the early morning, with long shadows and cool air"
    ],
    "ocean": [
        "In deep, dark waters, with schools of fish darting about",
        "Near a sunken ship, with currents gently swaying the seaweed",
        "Amidst a kelp forest, with light beams penetrating the blue water",
        "During a coral spawning event, with tiny particles floating in the water",
        "In shallow waters, with waves softly crashing above"
    ],
    "reef": [
        "Amidst vibrant coral formations, with colorful fish swimming by",
        "Under a strong current, with seaweed waving back and forth",
        "In clear water, with sunlight illuminating the coral structures",
        "During a feeding frenzy, with predators and prey darting through coral",
        "At low tide, with exposed coral and shallow pools teeming with life"
    ],
    "mountains": [
        "On a clear day, with a panoramic view of the valley below",
        "During a heavy snowfall, with thick snow covering the landscape",
        "On a foggy morning, with peaks just visible through the mist",
        "At sunset, with shadows stretching long across the rocky terrain",
        "During a thunderstorm, with lightning striking distant peaks"
    ],
    "forest": [
        "On a rainy day, with leaves glistening and water dripping from branches",
        "In the early morning fog, with the forest floor covered in dew",
        "During autumn, with leaves falling and a crisp chill in the air",
        "On a sunny afternoon, with light filtering through the dense canopy",
        "At twilight, with the sounds of nocturnal creatures beginning to stir"
    ],
    "glade": [
        "On a sunny day, with wildflowers blooming and butterflies fluttering",
        "At dawn, with dew-covered grass and soft light breaking through trees",
        "During a gentle breeze, with tall grasses swaying rhythmically",
        "In the early evening, with fireflies flickering around the clearing",
        "Under a full moon, with soft moonlight casting shadows in the open space"
    ],
    "riverbank": [
        "On a quiet morning, with mist rising off the slow-moving water",
        "During a gentle rain, with raindrops creating ripples in the river",
        "At sunset, with the water reflecting the orange and pink sky",
        "On a windy day, with reeds rustling and water splashing on the shore",
        "During a flood, with high waters and debris floating downstream"
    ],
    "grassland": [
        "In a gentle breeze, with tall grasses waving like a green ocean",
        "At sunrise, with the dew glistening on the blades of grass",
        "On a hot day, with the sun beating down on dry, parched earth",
        "During a thunderstorm, with lightning illuminating the expansive sky",
        "On a crisp autumn morning, with frost covering the grass"
    ],
    "field": [
        "Under a bright sun, with wildflowers in full bloom",
        "During a light drizzle, with soft earth beneath and fresh scents in the air",
        "At dusk, with long shadows cast across the expansive field",
        "On a windy day, with the grass and flowers swaying rhythmically",
        "In the early morning, with birds singing and a cool breeze blowing"
    ],
    "meadow": [
        "Under the midday sun, with butterflies fluttering over blooming flowers",
        "During spring, with a carpet of wildflowers and buzzing bees",
        "At dawn, with dew on the grass and the first light of day",
        "On a warm evening, with crickets chirping and a gentle breeze",
        "During a rain shower, with raindrops hitting the soft earth"
    ],
    "beach": [
        "On a sunny day, with waves gently lapping at the shore",
        "During a storm, with dark clouds and powerful waves crashing in",
        "At dawn, with the first light of day breaking over the horizon",
        "On a windy afternoon, with sand whipping through the air",
        "At low tide, with exposed rocks and tide pools full of life"
    ]
}

habitat_conjunctions = {
    "savannah": "on a",
    "jungle": "in a",
    "rainforest": "in a",
    "desert": "in a",
    "ocean": "in the",
    "reef": "in the",
    "mountains": "in the",
    "forest": "in a",
    "glade": "in a",
    "riverbank": "by the",
    "grassland": "in a",
    "field": "in a",
    "meadow": "in a",
    "beach": "on the"
}


# for dictionary in habitat_animals:
#     print(', '.join(dictionary["habitat"]))

def generate_prompt():
    dictionary = random.choice(habitat_animals)
    habitat = random.choice(dictionary['habitat'])
    animal = random.choice(dictionary['animals'])
    action = random.choice(animal_actions_by_properties[animal_properties[animal]])
    details = random.choice(habitat_details[habitat])
    conjunction = habitat_conjunctions[habitat]

    return f"Wildlife photography, High Definition, High Quality, RGB, high resolution photo of a {animal} {conjunction} {habitat}, {details.casefold().replace(', ', ' ')}, the {animal} it is {action.replace(',', ' ')}"

# Generate 40,000 random prompts
prompts = [generate_prompt() for _ in range(10000)]

# Print the first 10 prompts to verify
for prompt in prompts[:10]:
    print(prompt)

# Optionally, save the prompts to a file
with open("prompts_animals.txt", "w") as file:
    for prompt in prompts:
        file.write(prompt + "\n")