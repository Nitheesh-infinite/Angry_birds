import pygame
import constants as c

def Winner_screen(player1,player2):
    winner_text = None  
    if player1.all_blocks_destroyed :
        winner_text = c.FIRE_FONT.render(f"Player 1 wins with {player1.score} points!",True, c.WHITE)
    elif player2.all_blocks_destroyed:
        winner_text = c.FIRE_FONT.render(f"Player 2 wins with {player2.score} points!",True, c.WHITE)
    elif player1.all_blocks_destroyed and player2.all_blocks_destroyed:
        if player1.score > player2.score:
            winner_text = c.FIRE_FONT.render(f"Player 1 wins with {player1.score} points!",True, c.WHITE)
        elif player2.score > player1.score:
            winner_text = c.FIRE_FONT.render(f"Player 2 wins with {player2.score} points!",True, c.WHITE)
        else:
            winner_text = c.FIRE_FONT.render(f"It's a tie with {player1.score} points!",True, c.WHITE)
    elif player1.score > player2.score:
        winner_text = c.FIRE_FONT.render(f"Player 1 wins with {player1.score} points!",True, c.WHITE)
    elif player2.score > player1.score:
        winner_text = c.FIRE_FONT.render(f"Player 2 wins with {player2.score} points!",True, c.WHITE)
    running= True
    while running:
        c.screen.blit(c.winner_background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if winner_text:
            c.screen.blit(winner_text, (
                c.SCREEN_WIDTH // 2 - winner_text.get_width() // 2,
                c.SCREEN_HEIGHT // 2 - winner_text.get_height() // 2
            ))
        else:
            fallback_text = c.FIRE_FONT.render("No winner yet!", True, c.WHITE)
            c.screen.blit(fallback_text, (
                c.SCREEN_WIDTH // 2 - fallback_text.get_width() // 2,
                c.SCREEN_HEIGHT // 2 - fallback_text.get_height() // 2
            ))

        pygame.display.flip()