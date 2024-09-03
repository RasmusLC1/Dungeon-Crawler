Game Ideas

# Dungeon Crawler Gameplay Ideas
    Earn money from Dungeon to pay for inn at night
    Collect companions from prison cells in Dungeon
    Each prisoner increases rent cost in Inn
    Prisoners become companions or merchants/trainers/teachers
    Prisoners if companions can go with you to the dungeon, but will get perma killed if they die
    Can find weapons, armor and magic tombes to learn spells
    There are layers to the dungeon, each layer have one exit and different staircases down to a new random dungeon. You cannot go up through the original entrance again
    Clank card system to trigger dungeon events, it's an artifical dungeon
    Loot has weight which will slow you down, also lowers your initiative in combat
    Each dungeon layer get's progressively harder, but main challenge is to conserve resources to proceed further down
    Enviorement effects and physics to solve puzzles in the dungeon
    Each section has at least 1 random combat from a pool of possible mobs based on enviorement, frost section as frost enemies
    Each layer draws a random theme, fire for example, then it draws from the tech theme for example
    Pokemon style resistances and effectivness in a rock paper scissor style
    You can drop loot to flee combat, to distract enemies
    Take contracts to complete achievements, example kill 5 ice demons
    Noice attracts enemies

# Gameplay Loop
    Start with a deck / Runes, mixture of positive and negative cards, but all low risk
    Colelct gold and artifcats in dungeon to buy new cards
    Lower levels have better rewards
    To get to lower levels you need to collect a key on each floor
    Each time you complete a run you get a curse card that is calculated based on performance to force playstyle adjustments
        If you kill lots of enemies, it might make enemies tougher
        If you don't get detected or sneak a lot, maybe enemies have their detection radius increased
    You can then buy new cards and other upgrades with the gold you brought up
        Example could be buying keys to get to lower levels quicker
        Permanent upgrades for character like more health
    There are shrines in the dungeon where you can pay with souls of slain enemies to buy upgrades
        Upgrades could be temporarily calming the dungeon so that no new enemies spawn
        More gold on the floor
        Key to the next floor in case you cannot find one
        Weapon or artifact to help you
        Temporary rune for this run
    Game ends when you die, you can buy resurrection tombs to prevent this, but it will be money you could spend on other upgrades instead
        Each resurrection tomb gets more expensive
        

# Engine Features:
    # Tile systsem
    # Use A* for path finding
    # Inventory System
    # Weapon inventory system
    # Dropping item, triggers trap
    # Raytracer that limits players vision, so enemies can sneak up from behind
    # Light engine
    # Clatter System where enemies are attracted to noise
    Cards / Runes
    Level editor
    Dungeon generator
    Chunk system to prevent slowdown with larger maps

# Gameplay
    # Player can hold weapons
    # Attack
    Defend


# Weapons:
    # Torch, emits light and be be used to set enemies on fire, relatively low damage
    # Sword, best damage, little utility
    # Spear, can be thrown
    Shield, can block damage, can be used to rocket jump with bomb
    # Bow, can press button, different arrows that can do certain things
    Crossbow, Same as bow, but takes longer to load, but can be preloaded
    Boomerang, Returns to player and damages everything it hits
    Bomb, one time use, splash damage, can break enviorement, knockback from blast
    Axe, can break wood doors
    Mace/Hammer, can break certain walls and enviorement
    Whip, can be used for movement
    magic Staff, improved spells but poor melee damage, different staffs for different lores of magic

# Potions
    # Health
    # Mana
    Stamina
    Invisibility
    Light
    Damage
    Poison

# Arrows:
    # Basic Arrow, Higher base damage
    Rope arrow, allows you to cross traps
    Fire arrow, lights enemies on fire and lights up the envoirement
    Ice arrow, ice effect, if it touches water it freezes the water
    Poison arrow, poison effect, if it touches water it poisons it
    Electric arrow, electric effect, triggers traps and electrifies water

# Armour:
    Lighter armour less noise but less protection
    Heavy armour movement penalty
    Different types of armour to protect against different elements

# Movements:
    # Dash, Move rapidly without hit detection to a location
    Teleport to a random destination, has x amount of charges
    Run, double run speed for a short duration
    Roll, avoid damage and roll in the direction of the mouse
    Block, block damage, if the player has shield block all damage, if not then it only blocks melee
    Jump, can jump over 2 blocks with light armour, 1 with medium and 0 with heavy, takes stamina
    Swim in deep water, can't cross if in heavy armour
    Push certain objects and block

# Traps:
    # Spike pits, fall into and slows you down
    # Spike traps, that move up and harm you when they're extended
    # Spike traps poison, that move up and harm you when they're extended, poision effect
    # Fire traps, sets you on fire
    # Pushing trap, pushes entities when triggered
    Pressure plates, Trigger nearby linked object when pressed
    Explosive traps, area of effect damage
    # Bear trap, snares the entity for a period of time
    # Lava, sets on fire and slows down entity, heavy damage
    # Water, slows down entities


# Enemies:
    Each enemy has an intelligence level and personality that determines it's ability to think
        Personality:
            - Agression, number from 1 to 10 that determines its behaviour and makes it more likely to attack and stay in combat
            - Intelligence, 1-10, higher intelligence avoids traps and attacks from the shadows
            - Hunter type
                - pack swarms the player
                - Solo, goes after the player alone
                - Scout, looks for and calls allies to attack the player
                - Sentry, calls enemies in a wide range to notify if they spot the player, but they don't move unless they see the player
                - Ambusher, waits and attacks the player
                - Support, supports the other enemies with healing
                - Ranged, shoots the player from range 
                - Melee, attacks the player up close

    Spider, shoots spiderweb that snares you, less damage
    Big spider, boss mob, spawns smaller spiders and jumps at you, more damage
    Skeletons take more damage from blunt weapons, make more noise from rattle
    Rats swarm attack, easy to kill, little damage
    Robots, noisy, high armour but slow
    Minotaur, boss mob, charges and breaks envoirement, high damage, low defence
    Clicker, blind but good hearing, loud because of clicks
    Sniffer, Good smells, but bad hearing, attracted to blood and destroyed potions
    Necromancer, boss mob, spawns skeletons, raises killed skeletons
    Hydra, boss mob, splits head when a head is killed, needs to be attacked from behind or killed with enviorement damage
    Slime, splits into smaller slimes when health is low
    Ushabity, boss mob, sentry that waits for the player and attacks, high damage and defence
    Gargoyle, sentry that waits for players and blends into the envoirement
    Living plant, waits for the player and tries to ambush them, also attacks normal enemies, basically a trap
    Armadillos that dig and pop out of the ground to surprise you
    Goblins swarm attack, cowardly
    Elementals, rock, ice, fire, electric, metal
    Lurker in the dark, lowers light level around it, tries to sneak attack, vulnable to light

# Biomes:
    Desert Biome, Water does not exist, enemies are vulnerable to fire, high gold in urns
    Mushroom Biom, poison effects are common, enemies here are immune to poision, potion ingredients
    Crystal Caverns, High armour enemies, crystals that emit light, Rare gems
    Lava forge, lots of lava, enemies are immune to fire and deal fire damage, rare weapons
    Ice Cave, Lots of ice, enemies are immune to frost and deal frost damage, breakable walls are more common
    Ancient ruins, undead enemies, rare runes
    Water caves, need to traverse lots of water, Deep water contains enemies, look for shallow water. More Treasure chests


# Companions:
    Save friendly entities from prisons through the dungeon and make them ally you
    They will follow you and assists in different ways
    Ideas:
        Light source
        Healer
        Mana
        Item picker
        Attacker
        Defender

