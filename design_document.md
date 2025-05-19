# Core Mechanics
    Lighting engine to create dynamic lighting

    Dungeon has layers. One exit per layer; staircases descend into new random dungeons.

    Clank system spawns enemies using a director (inspired by Left 4 Dead).

    Difficulty increases per layer; managing resources is key.

    Item/inventory system to force players into meaningful choices

    Each section contains random enemy encounters based on environment.

    Layers draw random themes.

    Noise attracts enemies.

    Enemies have behavioral AI, so their attacks are randomised. They will circle the player and attack when ready

    Aggression metre that responds to players actions and how much clatter they generate. Gets more sensitive in lower layers

# Gameplay loop

    Enter Dungeon layer 1 with nothing

    Look for weapons, keys and other items and avoid enemies

    Start with 3 basic runes, can be upgraded later

    First level has less enemies, so it's safer to walk around

    Fight against enemies is a risk since there's no auto healing

    If health is low there's a greater chance to get healing items

    If player has no keys, keys will have a higher drop rate

    Search the dungeon for the portal shrine and kill enemies / sacrifice gold or get souls in other ways to activate it.

    You do not want to rush it though, since you want to collect items and upgrade weapons before entering next dungeon since portal shrine will increase in cost each layer

    If you want to upgrade runes you need to fight an optional boss. Risk reward

    Weapon shrines can be found and weapons can be combined with gems for powerful upgrades

    Gold can be used either as sacrifice for souls or to buy items

    Each layer should take 10-30 minutes to complete. Meaning a full run 7 layers should take around 2 hours

    Enemies scale the further into the dungeon you travel. But basic enemies should always be a threat

    Combat is timing based. You can see when enemies are about to attack and you need to get away from them before they do.

    If you start getting to much aggression then the player needs to hide. But if the aggression gets to high the enemies will be able to pathfind towards you and you just need to survive until it calms down. Avoid making it optimal to hide without doing anything. Maybe the player needs to find an item to remove the aggression

    Enemies have synergies, warriors are basic attack, spiders will snare and attack, priests heal, undertaker revives etc..

    Increasing heartbeat synced to aggression level

    Score at the end of the game to check performance metrics, enemies killed, aggression level, gold, souls, depth, shrines, etc