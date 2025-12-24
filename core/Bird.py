import pygame
import constants as c
import math
import copy

class Bird():
    def __init__(self):
        self.name = None
        self.id = None
        self.rect = None
        self.position = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)
        self.damage = None
        self.is_dragging = False
        self.is_launched = False
        self.is_active = False
        self.damage_to_wood=0
        self.damage_to_glass=0
        self.damage_to_rock=0
        self.IMAGE = None
        self.radius = None
        self.super_power = None          
        self.super_power_triggered = False
        self.birds = None
        self.collide_with_block = False
        self.bounce_time = None
        self.bounce_survive_duration = 4000
        self.life = None
        self.start_pos = pygame.math.Vector2(0, 0)
        self.life = 400

    def set_bird(self, id):
        if self.name == "RED":
            self.damage_to_wood = 40
            self.damage_to_glass = 40
            self.damage_to_rock = 40
        elif self.name == "BLUE":
            self.damage_to_wood = 30
            self.damage_to_glass = 70
            self.damage_to_rock = 20
            self.super_power = "SPLIT"
        elif self.name == "BLACK":
            self.damage_to_wood = 20
            self.damage_to_glass = 30
            self.damage_to_rock = 90
            self.super_power = "GRAVITY"
        elif self.name == "YELLOW":
            self.damage_to_wood = 70
            self.damage_to_glass = 30
            self.damage_to_rock = 20
            self.super_power = "SPEED"
        self.id = id
        original_image = c.BIRD_IMAGES[self.name]
        scaled_image = pygame.transform.scale(original_image, (c.SCREEN_WIDTH // 50, c.SCREEN_WIDTH // 50))
        if self.id == 2:
            scaled_image = pygame.transform.flip(scaled_image, True, False)
        self.IMAGE = scaled_image

        self.radius = 10
        self.velocity = pygame.math.Vector2(0, 0)
        self.is_dragging = False
        self.is_launched = False
        self.is_active = True
        self.power_time = None
        if self.id == 1:
            self.start_pos = pygame.math.Vector2(
                c.LEFT_CATAPULT_RECT[0] + c.SCREEN_WIDTH//100,
                c.LEFT_CATAPULT_RECT[1] + c.SCREEN_WIDTH//100,
            )
            self.rect = c.LEFT_CATAPULT_RECT.copy()
        else:
            self.start_pos = pygame.math.Vector2(
                c.RIGHT_CATAPULT_RECT[0] + c.SCREEN_WIDTH//100,
                c.RIGHT_CATAPULT_RECT[1] + c.SCREEN_WIDTH//100,
            )
            self.rect = c.RIGHT_CATAPULT_RECT.copy()

        self.position = pygame.math.Vector2(self.rect.center)

    def update_position_and_velocity(self):
        if self.is_launched:
            self.position += self.velocity
            self.rect.center = self.position
            self.velocity.y += c.GRAVITY
    
    def take_damage(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.reset()

    def clamp(self):
        mx, my = pygame.mouse.get_pos()
        self.rect.center = mx, my
        end_pos = self.rect.center
        dx = end_pos[0]-self.start_pos[0] 
        dy = end_pos[1]-self.start_pos[1]
        if math.hypot(dx, dy) > c.MAX_LENGTH:
            angle = math.atan2(dy, dx)
            dx = math.cos(angle) * c.MAX_LENGTH
            dy = math.sin(angle) * c.MAX_LENGTH
        self.rect.center = (self.start_pos[0] + dx, self.start_pos[1] + dy)
        self.position = pygame.math.Vector2(self.rect.center) 

    def initial_velocity(self):
        end_pos = self.rect.center
        dx = self.start_pos[0] - end_pos[0]
        dy = self.start_pos[1] - end_pos[1]
        distance = math.hypot(dx, dy)
        if distance != 0:
            direction = pygame.math.Vector2(dx / distance, dy / distance)
        else:
            direction = pygame.math.Vector2(0, 0)
        power_scale = distance / c.MAX_LENGTH
        power = power_scale * c.MAX_POWER  
        self.velocity = direction * power *2

    def show_bird(self):
        if self.is_active and self.IMAGE:
            c.screen.blit(self.IMAGE, (self.position.x - self.rect.width/2, self.position.y - self.rect.height/2))

    def get_circle(self):
        return (self.rect.centerx, self.rect.centery, self.radius)
    
    def circle_rect_collision(self, rect):
        x, y, r = self.get_circle()
        closest_x = max(rect[0], min(x, rect[0] + rect[2]))
        closest_y = max(rect[1], min(y, rect[1] + rect[3]))
        dx = closest_x - x
        dy = closest_y - y
        return math.hypot(dx, dy) <= r
    
    def get_collision_side(self, rect):
        x, y, r = self.get_circle()
        block_center_x = rect[0] + rect[2] // 2
        block_center_y = rect[1] + rect[3] // 2
        dx = x - block_center_x
        dy = y - block_center_y
        overlap_x = (rect[2] // 2 + r) - abs(dx)
        overlap_y = (rect[3] // 2 + r) - abs(dy)
        if overlap_x < overlap_y:
            if dx > 0:
                return "RIGHT"
            else:
                return "LEFT"
        else:
            if dy > 0:
                return "BOTTOM"
            else:
                return "TOP"

    def out_of_screen(self):
        if self.is_launched:
            return (
                self.rect.left < 0
                or self.rect.right > c.SCREEN_WIDTH
                or self.rect.top < 0
                or self.rect.bottom > c.SCREEN_HEIGHT
            )
        return False
    
    def predicted_projectile_path(self):
        mx, my = pygame.mouse.get_pos()
        dx = self.start_pos.x - mx
        dy = self.start_pos.y - my
        distance = math.hypot(dx, dy)

        if distance == 0:
            return  

        direction = pygame.math.Vector2(dx / distance, dy / distance)
        power_scale = min(distance / c.MAX_LENGTH, 1)
        power = power_scale * c.MAX_POWER
        initial_velocity = direction * power * 2 

        prediction_dots = 8
        frames_between_dots = 5
        simulated_pos = pygame.math.Vector2(self.rect.center)
        simulated_vel = initial_velocity.copy()

        for _ in range(prediction_dots):
            for _ in range(frames_between_dots):
                simulated_pos += simulated_vel
                simulated_vel.y += c.GRAVITY
            pygame.draw.circle(c.screen, (255, 0, 0), (int(simulated_pos.x), int(simulated_pos.y)), 5)

    def active_super_power(self):
        if self.super_power == "SPEED":
            self.velocity[0] *= 1.5
            return
        elif self.super_power == "SPLIT":
            return self.split()
        elif self.super_power == "GRAVITY":
            self.gravity()
            return
        
    def gravity(self):
        if self.super_power == "GRAVITY":
            self.velocity[1] *= self.velocity[1]
            self.velocity[0] = 0
            return

    def split(self):
        if not self.super_power_triggered:
            new_birds = []
            for offset, velocity_scale in [(10, 1.1), (-10, 0.9)]:
                new_bird = Bird()
                new_bird.velocity = self.velocity * velocity_scale
                new_bird.position = self.position + pygame.math.Vector2(offset, 0)
                new_bird.rect = self.rect.copy()
                new_bird.IMAGE = self.IMAGE
                new_bird.is_active = True
                new_bird.is_launched = True
                new_bird.radius = self.radius
                new_bird.damage_to_wood = self.damage_to_wood
                new_bird.damage_to_glass = self.damage_to_glass
                new_bird.damage_to_rock = self.damage_to_rock
                new_bird.name = self.name
                new_bird.id = self.id
                new_birds.append(new_bird)

            self.super_power_triggered = True
            new_birds.append(self)
            return new_birds

    def reset(self):
        self.__init__() 




