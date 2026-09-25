from random import randint
import telebot
from config import TOKEN
from logic import Fighter, Pokemon, Wizard

bot = telebot.TeleBot(TOKEN)


def get_user_identifier(user) -> str:
    """Extracts username or falls back to user ID if username is not set."""
    return user.username if user.username else str(user.id)


@bot.message_handler(commands=['go', 'start'])
def start_game(message):
    """Initializes a new Pokemon for the user if they don't own one yet."""
    user_id = get_user_identifier(message.from_user)

    if user_id not in Pokemon.pokemons:
        chance = randint(1, 3)
        if chance == 1:
            pokemon = Pokemon(user_id)
        elif chance == 2:
            pokemon = Wizard(user_id)
        else:
            pokemon = Fighter(user_id)

        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "You already have a Pokemon assigned!")


@bot.message_handler(commands=['attack'])
def attack_pokemon(message):
    """Handles turn-based battle execution when replying to an opponent's message."""
    if not message.reply_to_message:
        bot.send_message(
            message.chat.id, 
            "To attack, reply to a message from the trainer you want to challenge!"
        )
        return

    attacker_id = get_user_identifier(message.from_user)
    defender_id = get_user_identifier(message.reply_to_message.from_user)

    if attacker_id in Pokemon.pokemons and defender_id in Pokemon.pokemons:
        attacker_pok = Pokemon.pokemons[attacker_id]
        defender_pok = Pokemon.pokemons[defender_id]

        battle_result = attacker_pok.attack(defender_pok)
        bot.send_message(message.chat.id, battle_result)
    else:
        bot.send_message(
            message.chat.id, 
            "Both players must create a Pokemon using the /go command before battling!"
        )


if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)
