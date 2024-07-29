class Projectile:
    def __init__(self, game, p_type, pos, velocity, time):
        self.game = game
        self.type = p_type
        self.pos = pos
        self.velocity = velocity
        self.time = time
    
    def update(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.time += 1
        
    def Render(self, surf, render_scale, img, offset = (0,0)):
        surf.blit(img, (self.pos[0] - img.get_width() / render_scale - offset[0], self.pos[1] - img.get_height() / render_scale - offset[1]))

