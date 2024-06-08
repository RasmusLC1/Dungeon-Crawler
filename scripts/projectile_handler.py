from scripts.spark import Spark

import random
import math

class Projectile_Handler:
    def Projectile_Update(self, render_scale, offset = (0,0)):
        # [[x, y], direction, timer]
        for projectile in self.projectiles.copy():
            projectile.update()

            img = self.assets['projectile']
            projectile.render(self.display, render_scale, img, offset)
            if self.tilemap.solid_check(projectile.pos):
                self.projectiles.remove(projectile)
                
                
            elif projectile.time > 360:
                self.projectiles.remove(projectile)