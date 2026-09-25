from random import randint
from typing import Dict, Tuple
import requests


class Pokemon:
    """Base class representing a Pokemon fetched from PokeAPI."""

    pokemons: Dict[str, "Pokemon"] = {}

    def __init__(self, pokemon_trainer: str):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.power = randint(30, 50)
        self.hp = randint(200, 400)

        # Fetch image and name in a single HTTP request
        self.name, self.img = self._fetch_pokemon_data()
        Pokemon.pokemons[pokemon_trainer] = self

    def _fetch_pokemon_data(self) -> Tuple[str, str]:
        """Fetches Pokemon metadata and artwork URL from PokeAPI."""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        default_img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png"
        default_name = "Pikachu"

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                name = data.get('forms', [{}])[0].get('name', default_name).capitalize()
                img = data.get('sprites', {}).get('other', {}).get('official-artwork', {}).get('front_default', default_img)
                return name, img
        except requests.RequestException:
            pass

        return default_name, default_img

    def info(self) -> str:
        """Returns stats summary for the Pokemon."""
        return (
            f"Pokemon Name: {self.name}\n"
            f"Power Level: {self.power}\n"
            f"Health Points (HP): {self.hp}"
        )

    def show_img(self) -> str:
        """Returns the official artwork image URL."""
        return self.img

    def attack(self, enemy: "Pokemon") -> str:
        """Executes attack against an opponent Pokemon."""
        if isinstance(enemy, Wizard):
            if randint(1, 5) == 1:
                return f"Wizard Pokemon @{enemy.pokemon_trainer} blocked the attack with a magic shield!"

        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Battle between @{self.pokemon_trainer} and @{enemy.pokemon_trainer}. @{enemy.pokemon_trainer} has {enemy.hp} HP left."
        else:
            enemy.hp = 0
            return f"Victory! @{self.pokemon_trainer} defeated @{enemy.pokemon_trainer}!"


class Wizard(Pokemon):
    """Wizard Pokemon class specializing in defensive magic shields."""

    def attack(self, enemy: Pokemon) -> str:
        return super().attack(enemy)


class Fighter(Pokemon):
    """Fighter Pokemon class specializing in physical super-attacks."""

    def attack(self, enemy: Pokemon) -> str:
        super_power = randint(5, 15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return f"{result}\n[Fighter Bonus] Applied super-attack with +{super_power} extra power!"


if __name__ == '__main__':
    wizard = Wizard("Trainer_Alice")
    fighter = Fighter("Trainer_Bob")

    print(wizard.info())
    print("-" * 30)
    print(fighter.info())
    print("-" * 30)
    print(fighter.attack(wizard))
