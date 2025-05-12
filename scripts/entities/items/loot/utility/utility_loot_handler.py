from scripts.entities.items.loot.utility.echo_bell import Echo_Bell
from scripts.entities.items.loot.utility.shadow_cloak import Shadow_Cloak
from scripts.entities.items.loot.utility.faded_hourglass import Faded_Hourglass
from scripts.entities.items.loot.utility.ethereal_chains import Ethereal_Chains
from scripts.entities.items.loot.utility.recall_scroll import Recall_Scroll
from scripts.entities.items.loot.loot_types_handler import Loot_Types_Handler


class Utility_Loot_Handler(Loot_Types_Handler):
    def __init__(self, game):
        super().__init__(game)


        self.loot_map = {
            self.game.dictionary.echo_bell: Echo_Bell,
            self.game.dictionary.faded_hourglass : Faded_Hourglass,
            self.game.dictionary.ethereal_chains : Ethereal_Chains,
            self.game.dictionary.shadow_cloak: Shadow_Cloak,
            self.game.dictionary.recall_scroll: Recall_Scroll,
        }

        self.types = [
            self.game.dictionary.echo_bell,
            self.game.dictionary.faded_hourglass,
            self.game.dictionary.ethereal_chains,
            self.game.dictionary.shadow_cloak,
            self.game.dictionary.recall_scroll
        ]



