from builtins import str
import random


def generate_nickname() -> str:
    """Generate a URL-safe nickname using adjectives and animal names."""
    adjectives = ["clever", "jolly", "brave", "sly", "gentle"]
    animals = ["panda", "fox", "raccoon", "koala", "lion"]
    number = random.randint(0, 999)
    nickname = f"{random.choice(adjectives)}_{random.choice(animals)}_{number}"
    print(nickname)
    return nickname