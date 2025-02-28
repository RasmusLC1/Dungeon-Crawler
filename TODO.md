Game Ideas

LOADING PAGE:
Menu screen that renders parts of a loading bar every time a step in dungeon generator generates a new chunk
Save it in a seperate class that accepts an increment from dungeon generator


# Dungeon Crawler Gameplay Ideas
    Earn money from Dungeon to pay for inn at night
    Collect companions from prison cells in Dungeon
    Each prisoner increases rent cost in Inn
    Prisoners become companions or merchants/trainers/teachers
    Prisoners if companions can go with you to the dungeon, but will get perma killed if they die
    Can find weapons, armor and magic tombes to learn runes
    There are layers to the dungeon, each layer have one exit and different staircases down to a new random dungeon. You cannot go up through the original entrance again
    Clank card system to trigger dungeon events, it's an artifical dungeon
    Loot has weight which will slow you down, also lowers your initiative in combat
    Each dungeon layer get's progressively harder, but main challenge is to conserve resources to proceed further down
    Enviorement effects and physics to solve puzzles in the dungeon
    Each section has at least 1 random combat from a pool of possible mobs based on enviorement, freeze section as freeze enemies
    Each layer draws a random theme, fire for example, then it draws from the tech theme for example
    Pokemon style resistances and effectivness in a rock paper scissor style
    You can drop loot to flee combat, to distract enemies
    Take contracts to complete achievements, example kill 5 ice demons
    Noice attracts enemies

# Gameplay Loop
    Collect gold and artifcats in dungeon to buy items, upgrades, heaaling etc
    Lower levels have better rewards
    To get to lower levels you need to pay a soul cost on each floor
    Each time you complete a floor the next one becomes more difficult
    There are shrines in the dungeon where you can pay with souls of slain enemies to buy upgrades
        Shrines are found in boss rooms, risk damage to upgrade
        Different Shrines do different things:
            Rune shrine, Upgrade and Buy runes
            Character shrine, upgrade character
            Artifact Shrine, buy and upgrade weapons and artifacts
        Boss Room initialised as an object with a radius, closes doors and locks player in.
            Spawns boss mob when player is x from center
            Spawns Shrine when boss mob is defeated
        
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
    # Dungeon generator
    # Chunk system to prevent slowdown with larger maps
    # Save Load System
    # Particle Engine
    Sound engine
    Minimap, adjust rendering scale for minimap and only display tiles that has been in raycaster

# Gameplay
    # Player can hold weapons
    # Attack
    # Defend
    X chance to get a shop each floor, spawns similar to boss room
    In shop you can buy/trash cards, upgrade weapons, buy items, heal, etc
    Each floor you add a new curse to your card deck, trashing curses cost 3X as much gold 
    Get points upon death based on level depth, gold and relics

# Shop
Buy and sell items to help complete levels
Upgrade weapons
Buy and trash cards, when buying a card it is added to discard pile
Cards can be upgraded
Create color coded backgrounds based on level, render image and text on top


# Weapons:
    # Implement better animations, bright arcs for where the damage area is
    # Torch, emits light and be be used to set enemies on fire, relatively low damage
    # Sword, best damage, little utility
    # Spear, can be thrown
    # Shield, can block damage, can be used to rocket jump with bomb
    # Bow, can press button, different arrows that can do certain things
    # Axe, can break wood doors
    # Hatchet, small axe, faster than axe
    # Mace/Hammer, can break certain walls and enviorement, special ground pound to stun nearby enemies
    # Halberd, swing and stab attack, charge attack
    # Scythe, swing attack, soul reap magic attack
    # Crossbow, Same as bow, but takes longer to load, but can be preloaded
    Bomb, one time use, splash damage, can break enviorement, knockback from blast
    magic Staff, improved runes but poor melee damage, different staffs for different lores of magic, costs souls per cast. Special attack for each lores

# Items
    Items are held in inventory, not worth a lot of money, but helps navigate dungeon
    Rare objects found in loot rooms
    Pendant of light, Revive the player one time for 100 gold
    Pendant of Faith, Highlights traps
    Lantern, Sets the player light to 7, passive light
    Totem of Power, increases Rune power, stacks with more totems
    Totem of Strength, increases strength
    Totem of Luck, gives a chance to cancel negative card
    Compass that points towards boss room
    Blood tomb, increases speed and damage as player takes damage
    Magnet, autopickup of items
    lockpick, has a 7/10 chance to open the door and persist, but if it breaks door does not open and generates clank
    


# Potions
    # Health
    # strength
    # movement
    # Soul
    # health regen, more health than health potion but slower
    # silence
    # invisibility
    # poison resistance
    # fire resistance
    # freeze resistance
    luck
    # vampire, heals based on damage dealt


# Runes
    You can have 3 runes equipped at a time
    Can buy new runes or upgrade existing ones in shrines 

    Costs souls each time it's cast
    Two types of runes, passive runes and activated runes
    Passive runes don't cost souls, but they are less powerful
    Active runes:
        # Dash,
        # Healing
        # Speed
        # Invisibility
        # Silence
        # Door unlock
        # Speed
        # Strength
        # Immunity
        Random Teleport, to get out of bad situations
        Scream, make enemies run away from you
        Shield charm, have 4 shield around you that grant immunity but breaks when damage taken
        # Vampiric, regen from damaging enemies
    
    Passive Runes:
        # Regen
        # Light
        # Arcane conduit, increase power level of your other runes
        # Hunger, increase souls generation
        # Magnet, Auto pickup of items
        # Resistance
        Thorns, enemies take damage when they hit you
        Frost Shield, enemies freeze when damaging you

    Fire runes:
        # Fireball, ball of fire that leads to fire explosion
        # Fire spew, flamethrower attack
        Fire wall, wall of fire that damage anything that tries to cross it
    
    Frost runes:
        # Iceball, ball that causes a freeze explosion that slows everything in it
        # Ice projectiles, fast ice projectiles shot like a bullet
        ice storm, Creates a tornado on entity that shoots ice projectiles at random 

    Electric runes:
        # Chain ligtning, Lightning projectile that bounces between entities
        # Electric ball, electric ball that generates electric explosion
        # Electric homing particle, electric projectiles that target nearest entity

    Poison runes:
        # Poison ball, Poison ball that turns into a poison cloud
        # Posion cloud, creates a big poison cloud around entity, area of effect
        # Poison plumes, creates  poison clouds around entity at random positions

    Vampiric runes:
        Life drain, slowly drain health from all nearby entities
        # Soul reap, broad projectile that sucks health from everything it hits
        # Soul pit that pulls entities in and sucks health from them

# Arrows:
    # Basic Arrow, Higher base damage
    Rope arrow, allows you to cross traps
    Fire arrow, lights enemies on fire and lights up the envoirement
    Ice arrow, ice effect, if it touches water it freezes the water
    Poison arrow, poison effect, if it touches water it poisons it
    Electric arrow, electric effect, triggers traps and electrifies water

# Movements:
    # Dash, Move rapidly without hit detection to a location
    # Roll, avoid damage and roll in the direction of the mouse
    # Backstep, move backwards a little and be immune
    # Block, block damage, if the player has shield block all damage, if not then it only blocks melee

    Teleport to a random destination, has x amount of charges
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
    Enemies start out basic but can upgrade to elite as dungeon effects trigger
    Spawn enemies using dungeon director when effects trigger
    Enemies have a difficulty attribute to make the spawning dynamic
    Enemies seperated into tribes with different strengths and weaknesses
    - pack swarms the player
    - Solo, goes after the player alone
    - Scout, looks for and calls allies to attack the player
    - Sentry, calls enemies in a wide range to notify if they spot the player, but they don't move unless they see the player
    - Ambusher, waits and attacks the player
    - Support, supports the other enemies with healing
    - Ranged, shoots the player from range 
    - Melee, attacks the player up close

## Undead Tribe
    # Skeleton Warrior, basic warrior uses standard weapons
    # Skeleton scout, uses ranged weapons
    # Skeleton Cleric, heals undead in the area but does no damage
    # Skeleton Bell Toller, alerts nearby enemies if it sees the player
    # Skeleton Undertaker, revieves dead enemies
    Skeleton Guard, slow, high health and medium damage
    Skeleton warlock, uses magic poison attacks
    Necromancer, boss, can resurrect undead and summon 3 skeletons
    Wight Lord, boss, armoured skeleton with shield and sword, can dash to close range
    Vampire, boss, life steal, flying bat form when travelling, close combat
    Crypt Ghoul, bone club, fast and high damage, but glass cannon
    Crypt Horror, boss, high damage and health, slow
    Ghost, pathfinds directly to the target, phasing through walls, high damage, medium speed and low health
    Wraith, pathfinds directly to the target, phasing through walls, low damage but steals soul, medium speed and low health
    Lich, casts doom on player, debuffing him and slowly drains health until Acolyte is killed


## Dungeon Dwellers
    Undead tribe
    Kobold, different variaties can steal different items from player, soul, loot, potions etc
    # Spider, shoots spiderweb that snares you, less damage -> Upgrades to Big Spider
    Mimic chest that spawns skeleton when opened
    Medusa, laser eyes and can freeze the player


## Ancient Tomb Enemies
    Big spider, boss mob, spawns smaller spiders and jumps at you, more damage
    # Skeletons take more damage from blunt weapons, make more noise from rattle  -> Upgrades to Wight Lord
    Ghost, can go through walls, low health high damage, need special effect to damage -> Upgrades to Reaper
    Reaper, elite melee enemy with scythe sweep attack
    Wolves, fast and high damage  -> Upgrades to WereWolf
    WereWolf, Elite enemy high mass fast, high damage
    Gargoyle, sentry that waits for players and blends into the envoirement
    Eyes of Evil, floating eyes that shoot at range, Snare

## Crystal Caverns enemies
    # Spider, shoots spiderweb that snares you, less damage
    Crystal Elemental, high health and strength, shoots crystal
    Minotaur, boss mob, charges and breaks envoirement, high damage, low defence
    Hydra, boss mob, splits head when a head is killed, needs to be attacked from behind or killed with enviorement damage
    Clicker, blind but good hearing, loud because of clicks



    Rats swarm attack, easy to kill, little damage
    Sniffer, Good smells, but bad hearing, attracted to blood and destroyed potions
    Slime, splits into smaller slimes when health is low
    Ushabity, boss mob, sentry that waits for the player and attacks, high damage and defence
    Living plant, waits for the player and tries to ambush them, also attacks normal enemies, basically a trap
    Armadillos that dig and pop out of the ground to surprise you
    Goblins swarm attack, cowardly
    # Elementals, rock, ice, fire, electric, metal
    Lurker in the dark, lowers light level around it, tries to sneak attack, vulnable to light

# Biomes:
    Desert Biome, Water does not exist, enemies are vulnerable to fire, high gold in urns, 

    Mushroom Biom, poison effects are common, enemies here are immune to poision, more potion, exploding mushrooms, Mushroom Queen boss

    Crystal Caverns, High armour enemies, crystals that emit light, Rare gems

    Aztec Temple, dinosaurs worship, dinosaur skull masks for some enemies, 

    Lava forge, lots of lava, enemies are immune to fire and deal fire damage, rare weapons

    Ice Cave, Lots of ice, enemies are immune to freeze and deal freeze damage, breakable walls are more common

    Ancient ruins, undead enemies, rare runes

    Water caves, need to traverse lots of water, Deep water contains enemies, look for shallow water. More Treasure chests



{'game': <__main__.Game object at 0x000001E2F00BBF10>, 'ID': 342, 'category': 'item', 'sub_category': 'weapon', 'type': 'torch', 'sprite': [<Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>, <Surface(32x32x32 SW)>], 'entity_image': <Surface(32x32x32 SW)>, 'rendered_image': None, 'render_needs_update': True, 'pos': (824.25, 764.75), 'size': (32, 32), 'active': True, 'light_level': 240, 'render': False, 'tile': None, 'saved_data': {}, 'text_box': <scripts.entities.textbox.weapon_textbox.Weapon_Textbox object at 0x000001E290B32320>, 'description': 'fire 1\nspeed 8\nrange 3\ngold 100\n', 'sub_type': 'torch', 'used': False, 'picked_up': True, 'move_inventory_slot': False, 'inventory_type': None, 'inventory_index': 12, 'activate_cooldown': 0, 'animation_cooldown': 9, 'animation_cooldown_max': 20, 'amount': 1, 'max_amount': 0, 'max_animation': 5, 'animation': 2, 'nearby_entities': [], 'delete_countdown': 0, 'value': 100, 'is_projectile': False, 'damage': 1, 'speed': 8, 'range': 3, 'entity': <scripts.entities.moving_entities.player.player.Player object at 0x000001E293D24040>, 'effect': 'fire', 'attack_type': 'cut', 'in_inventory': False, 'equipped': True, 'attacking': 0, 'flip_x': False, 'attack_animation': 0, 'attack_animation_max': 5, 'special_attack_effect_animation_max': 1, 'attack_animation_time': 0, 'attack_animation_counter': 0, 'attack_effect_animation': 0, 'attack_effect_animation_max': 6, 'attack_effect_animation_time': 0, 'attack_effect_animation_counter': 0, 'enemy_hit': True, 'rotate': 0, 'nearby_enemies': [], 'weapon_class': 'one_handed_melee', 'charge_time': 0, 'max_charge_time': 100, 'is_charging': 0, 'special_attack': 0, 'special_attack_active': False, 'charge_effect': 'fire_charge_effect', 'charge_effect_animation': 0, 'charge_effect_animation_max': 5, 'charge_effect_cooldown': 0, 'charge_effect_cooldown_max': 15, 'weapon_cooldown': 0, 'weapon_cooldown_max': 50, 'delete_timer': 0, 'wall_hit': False, 'attack_hitbox_size': (5, 5), 'attack_hitbox': <rect(824, 764, 5, 5)>, 'light_source': <scripts.engine.lights.lights.Light object at 0x000001E290B32380>, 'fire_particle_cooldown': 42, 'flame_thrower': <scripts.entities.items.weapons.magic_attacks.fire.flame_thrower.Flame_Thrower object at 0x000001E290B323B0>}