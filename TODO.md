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
    Each section has at least 1 random combat from a pool of possible mobs based on enviorement, freeze section as freeze enemies
    Each layer draws a random theme, fire for example, then it draws from the tech theme for example
    Pokemon style resistances and effectivness in a rock paper scissor style
    You can drop loot to flee combat, to distract enemies
    Take contracts to complete achievements, example kill 5 ice demons
    Noice attracts enemies

# Gameplay Loop
    Start with a deck / Runes, mixture of positive and negative cards, but all low risk
    Collect gold and artifcats in dungeon to buy new cards
    Lower levels have better rewards
    To get to lower levels you need to collect a key on each floor
    Each time you complete a run you get a curse card that is calculated based on performance to force playstyle adjustments
        If you kill lots of enemies, it might make enemies tougher
        If you don't get detected or sneak a lot, maybe enemies have their detection radius increased
    You can then buy new cards and other upgrades with the gold you brought up
        Example could be buying keys to get to lower levels quicker
        Permanent upgrades for character like more health
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
    Cards / Runes

# Gameplay
    # Player can hold weapons
    # Attack
    # Defend


# Weapons:
    Implement better animations, bright arcs for where the damage area is
    # Torch, emits light and be be used to set enemies on fire, relatively low damage
    # Sword, best damage, little utility
    # Spear, can be thrown
    # Shield, can block damage, can be used to rocket jump with bomb
    # Bow, can press button, different arrows that can do certain things
    Crossbow, Same as bow, but takes longer to load, but can be preloaded
    Halberd, swing and stab attack, charge attack
    Bomb, one time use, splash damage, can break enviorement, knockback from blast
    Axe, can break wood doors
    Hatchet, small axe, faster than axe
    Mace/Hammer, can break certain walls and enviorement, special ground pound to stun nearby enemies
    magic Staff, improved spells but poor melee damage, different staffs for different lores of magic, costs souls per cast. Special attack for each lores

# Items
    Rare objects found in loot rooms
    Pendant of light, Revive the player one time for 100 gold
    Pendant of Faith, Highlights traps
    Lantern, Sets the player light to 7, passive light
    Totem of Power, increases Rune power, stacks with more totems
    Totem of Strength, increases strength
    Totem of Luck, gives a chance to cancel negative card
    Compass that points towards boss room
    


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
    physical resistance
    luck
    vampire, heals based on damage dealt

# Spells
    You can have 3 spells equipped at a time
    Can buy new spells or upgrade existing ones in shrines 

    Costs souls each time it's cast
    Two types of spells, passive spells and activated spells
    Passive spells don't cost souls, but they are less powerful
    Active Spells:
        # Dash,
        # Healing
        Speed
        Immunity
        Invisibility
        Silence
        # Door unlock
        Directed Fire blast 
        Circle Fire blast
        Directed Ice blast 
        Circle Ice blast
        Poision Cloud
        Lightning bolt
        Random Teleport, to get out of bad situations
        Scream, make enemies run away from you
        Shield charm, have 4 shield around you that grant immunity but breaks when damage taken
        Vampiric touch, regen from damaging enemies
    
    Passive Spells:
        # Regen
        # Light
        Resistance
        Thorns, enemies take damage when they hit you
        Frost Shield, enemies freeze when damaging you
        Arcane conduit, increase power level of your other spells




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
    - pack swarms the player
    - Solo, goes after the player alone
    - Scout, looks for and calls allies to attack the player
    - Sentry, calls enemies in a wide range to notify if they spot the player, but they don't move unless they see the player
    - Ambusher, waits and attacks the player
    - Support, supports the other enemies with healing
    - Ranged, shoots the player from range 
    - Melee, attacks the player up close

## Ancient Tomb Enemies
    # Spider, shoots spiderweb that snares you, less damage -> Upgrades to Big Spider
    Big spider, boss mob, spawns smaller spiders and jumps at you, more damage
    # Skeletons take more damage from blunt weapons, make more noise from rattle  -> Upgrades to Wight Lord
    Wight Lord, elite armoured skeleton with shield and sword, can dash to close range
    Ghost, can go through walls, low health high damage, need special effect to damage -> Upgrades to Reaper
    Reaper, elite melee enemy with scythe sweep attack
    Vampire, life steal, flying bat form when travelling, close combat
    Crypt Ghoul, bone club, fast -> Upgrades to Crypt Horror
    Crypt Horror, Elite high damage and strength, fast
    Wolves, fast and high damage  -> Upgrades to WereWolf
    WereWolf, Elite enemy high mass fast, high damage
    Necromancer, elite mob, spawns skeletons, raises killed skeletons, atacks with poision orb shots  
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

    Lava forge, lots of lava, enemies are immune to fire and deal fire damage, rare weapons

    Ice Cave, Lots of ice, enemies are immune to freeze and deal freeze damage, breakable walls are more common

    Ancient ruins, undead enemies, rare runes

    Water caves, need to traverse lots of water, Deep water contains enemies, look for shallow water. More Treasure chests

# LOW PRIORITY TASKS
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

