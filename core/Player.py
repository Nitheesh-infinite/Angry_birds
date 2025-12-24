
import constants as c

class Player:
    def __init__(self, player_id, name, score=0):
        self.id = player_id            
        self.name = name              
        self.score = score       
        self.all_blocks_destroyed = False      

    def update_score(self, points):
        self.score += points

    def display_score(self, pos=(10, 10)):
        score_text = c.FIRE_FONT.render(f"Score: {self.score}", True, c.WHITE)
        name_text = c.FIRE_FONT.render(f"Player {self.id}: {self.name}", True, c.WHITE)
        c.screen.blit(name_text, (pos[0], pos[1] - 60))
        c.screen.blit(score_text, pos)
