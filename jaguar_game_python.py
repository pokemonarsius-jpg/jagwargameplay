"""
Jaguar Hunt Game - A Python Pygame Adventure
Created with Pygame - Install with: pip install pygame

Controls:
- Arrow Keys or WASD: Move the jaguar
- SPACE: Pounce to catch prey
- ESC: Pause game
- R: Restart after game over

Objective: Hunt prey, avoid obstacles, survive as long as possible!
"""

import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)
JAGUAR_YELLOW = (244, 164, 96)
JAGUAR_SPOT = (139, 69, 19)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)

# Game States
MENU = 0
PLAYING = 1
PAUSED = 2
GAME_OVER = 3


class Jaguar(pygame.sprite.Sprite):
    """The player-controlled jaguar"""
    
    def __init__(self, x, y):
        super().__init__()
        self.width = 60
        self.height = 50
        self.x = x
        self.y = y
        self.speed = 6
        self.dx = 0
        self.dy = 0
        self.pouncing = False
        self.pounce_timer = 0
        self.pounce_cooldown = 0
        self.facing_right = True
        self.animation_frame = 0
        self.animation_speed = 0.2
        
        # Create surface
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.draw_jaguar()
    
    def draw_jaguar(self):
        """Draw the jaguar sprite"""
        self.image.fill((0, 0, 0, 0))
        
        # Pounce effect
        if self.pouncing:
            color = ORANGE
            glow_surface = pygame.Surface((self.width + 20, self.height + 20), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, (255, 215, 0, 100), 
                             (self.width // 2 + 10, self.height // 2 + 10), 40)
            self.image.blit(glow_surface, (-10, -10))
        else:
            color = JAGUAR_YELLOW
        
        # Body
        body_rect = pygame.Rect(10, 15, 40, 25)
        pygame.draw.ellipse(self.image, color, body_rect)
        
        # Spots
        spot_positions = [(15, 20), (25, 18), (35, 22), (20, 28), (30, 30)]
        for pos in spot_positions:
            pygame.draw.circle(self.image, JAGUAR_SPOT, pos, 3)
        
        # Head
        head_x = 45 if self.facing_right else 15
        pygame.draw.circle(self.image, color, (head_x, 25), 12)
        
        # Eyes
        eye_offset = 3 if self.facing_right else -3
        pygame.draw.circle(self.image, BLACK, (head_x + eye_offset, 23), 2)
        
        # Ears
        ear_offset = 5 if self.facing_right else -5
        pygame.draw.polygon(self.image, color, 
                          [(head_x + ear_offset, 15), 
                           (head_x + ear_offset + 3, 10), 
                           (head_x + ear_offset + 6, 15)])
        
        # Tail (animated)
        tail_start_x = 10 if self.facing_right else 50
        tail_wave = math.sin(self.animation_frame) * 5
        tail_points = [
            (tail_start_x, 28),
            (tail_start_x - 15 if self.facing_right else tail_start_x + 15, 25 + tail_wave),
            (tail_start_x - 25 if self.facing_right else tail_start_x + 25, 30 + tail_wave)
        ]
        pygame.draw.lines(self.image, color, False, tail_points, 4)
        
        # Legs (simple)
        leg_color = BROWN
        leg_positions = [(18, 35), (28, 35), (35, 35), (42, 35)]
        for leg_x, leg_y in leg_positions:
            pygame.draw.line(self.image, leg_color, (leg_x, leg_y), (leg_x, leg_y + 8), 3)
    
    def update(self, keys):
        """Update jaguar position and state"""
        # Movement
        self.dx = 0
        self.dy = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx = -self.speed
            self.facing_right = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx = self.speed
            self.facing_right = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.dy = self.speed
        
        # Apply movement
        self.x += self.dx
        self.y += self.dy
        
        # Boundary check
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        self.y = max(50, min(self.y, SCREEN_HEIGHT - self.height - 50))
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Pounce mechanics
        if self.pounce_cooldown > 0:
            self.pounce_cooldown -= 1
        
        if self.pouncing:
            self.pounce_timer -= 1
            if self.pounce_timer <= 0:
                self.pouncing = False
        
        # Animation
        self.animation_frame += self.animation_speed
        
        self.draw_jaguar()
    
    def pounce(self):
        """Activate pounce ability"""
        if not self.pouncing and self.pounce_cooldown == 0:
            self.pouncing = True
            self.pounce_timer = 15
            self.pounce_cooldown = 30
            return True
        return False


class Prey(pygame.sprite.Sprite):
    """Prey animals for the jaguar to hunt"""
    
    def __init__(self):
        super().__init__()
        self.types = ['rabbit', 'deer', 'monkey']
        self.type = random.choice(self.types)
        self.width = 35
        self.height = 35
        self.x = SCREEN_WIDTH
        self.y = random.randint(100, SCREEN_HEIGHT - 100)
        self.speed = random.uniform(2.5, 4.5)
        self.points = 10
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.draw_prey()
    
    def draw_prey(self):
        """Draw prey based on type"""
        self.image.fill((0, 0, 0, 0))
        
        if self.type == 'rabbit':
            # Body
            pygame.draw.ellipse(self.image, (200, 200, 200), (8, 15, 20, 15))
            # Head
            pygame.draw.circle(self.image, (220, 220, 220), (25, 18), 8)
            # Ears
            pygame.draw.ellipse(self.image, (200, 200, 200), (26, 5, 4, 12))
            pygame.draw.ellipse(self.image, (200, 200, 200), (30, 5, 4, 12))
            # Eye
            pygame.draw.circle(self.image, BLACK, (28, 18), 2)
            
        elif self.type == 'deer':
            # Body
            pygame.draw.ellipse(self.image, (160, 82, 45), (5, 15, 25, 18))
            # Head
            pygame.draw.circle(self.image, (160, 82, 45), (28, 18), 7)
            # Antlers
            pygame.draw.line(self.image, BROWN, (28, 12), (28, 5), 2)
            pygame.draw.line(self.image, BROWN, (28, 8), (24, 4), 2)
            pygame.draw.line(self.image, BROWN, (28, 8), (32, 4), 2)
            
        elif self.type == 'monkey':
            # Body
            pygame.draw.ellipse(self.image, (139, 90, 43), (10, 12, 18, 20))
            # Head
            pygame.draw.circle(self.image, (139, 90, 43), (19, 12), 9)
            # Face
            pygame.draw.circle(self.image, (205, 133, 63), (19, 14), 5)
            # Eyes
            pygame.draw.circle(self.image, BLACK, (17, 12), 2)
            pygame.draw.circle(self.image, BLACK, (21, 12), 2)
            # Tail
            pygame.draw.arc(self.image, (139, 90, 43), (22, 18, 15, 20), 0, 3.14, 3)
    
    def update(self):
        """Move prey across screen"""
        self.x -= self.speed
        self.rect.x = self.x
        
        if self.x < -50:
            self.kill()


class Obstacle(pygame.sprite.Sprite):
    """Obstacles that damage the jaguar"""
    
    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 80
        self.x = SCREEN_WIDTH
        self.y = random.randint(80, SCREEN_HEIGHT - 150)
        self.speed = 3
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.draw_obstacle()
    
    def draw_obstacle(self):
        """Draw tree obstacle"""
        self.image.fill((0, 0, 0, 0))
        
        # Trunk
        pygame.draw.rect(self.image, BROWN, (15, 20, 20, 60))
        
        # Foliage
        pygame.draw.circle(self.image, DARK_GREEN, (25, 20), 25)
        pygame.draw.circle(self.image, GRASS_GREEN, (15, 15), 18)
        pygame.draw.circle(self.image, GRASS_GREEN, (35, 15), 18)
    
    def update(self):
        """Move obstacle across screen"""
        self.x -= self.speed
        self.rect.x = self.x
        
        if self.x < -60:
            self.kill()


class Particle(pygame.sprite.Sprite):
    """Visual effect particles"""
    
    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.size = random.randint(3, 8)
        self.color = color
        self.lifetime = random.randint(20, 40)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-3, -1)
        
        self.image = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, self.color, (self.size, self.size), self.size)
    
    def update(self):
        """Update particle position"""
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1
        self.rect.x = self.x
        self.rect.y = self.y
        
        if self.lifetime <= 0:
            self.kill()


class Game:
    """Main game class"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jaguar Hunt Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 32)
        
        self.state = MENU
        self.score = 0
        self.lives = 3
        self.high_score = 0
        
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.prey_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.particle_group = pygame.sprite.Group()
        
        self.jaguar = None
        self.spawn_timer = 0
        self.difficulty_timer = 0
        self.spawn_rate = 60
        
    def reset_game(self):
        """Reset game state"""
        self.all_sprites.empty()
        self.prey_group.empty()
        self.obstacle_group.empty()
        self.particle_group.empty()
        
        self.score = 0
        self.lives = 3
        self.spawn_timer = 0
        self.difficulty_timer = 0
        self.spawn_rate = 60
        
        self.jaguar = Jaguar(100, SCREEN_HEIGHT // 2)
        self.all_sprites.add(self.jaguar)
        
        self.state = PLAYING
    
    def draw_background(self):
        """Draw game background"""
        # Sky
        self.screen.fill(SKY_BLUE)
        
        # Grass
        pygame.draw.rect(self.screen, GRASS_GREEN, 
                        (0, SCREEN_HEIGHT - 80, SCREEN_WIDTH, 80))
        
        # Grass details
        for i in range(0, SCREEN_WIDTH, 20):
            pygame.draw.line(self.screen, DARK_GREEN, 
                           (i, SCREEN_HEIGHT - 80), 
                           (i, SCREEN_HEIGHT - 70), 2)
    
    def draw_ui(self):
        """Draw UI elements"""
        # Score
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        score_shadow = self.small_font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_shadow, (22, 12))
        self.screen.blit(score_text, (20, 10))
        
        # Lives
        lives_text = self.small_font.render(f"Lives: {self.lives}", True, WHITE)
        lives_shadow = self.small_font.render(f"Lives: {self.lives}", True, BLACK)
        self.screen.blit(lives_shadow, (22, 47))
        self.screen.blit(lives_text, (20, 45))
        
        # High Score
        high_text = self.small_font.render(f"High: {self.high_score}", True, GOLD)
        self.screen.blit(high_text, (SCREEN_WIDTH - 180, 10))
        
        # Pounce cooldown indicator
        if self.jaguar and self.jaguar.pounce_cooldown > 0:
            cooldown_width = 100
            cooldown_height = 10
            cooldown_x = SCREEN_WIDTH // 2 - cooldown_width // 2
            cooldown_y = SCREEN_HEIGHT - 30
            
            pygame.draw.rect(self.screen, BLACK, 
                           (cooldown_x - 2, cooldown_y - 2, cooldown_width + 4, cooldown_height + 4))
            
            fill_width = cooldown_width * (1 - self.jaguar.pounce_cooldown / 30)
            pygame.draw.rect(self.screen, ORANGE, 
                           (cooldown_x, cooldown_y, fill_width, cooldown_height))
        else:
            ready_text = self.small_font.render("POUNCE READY!", True, GOLD)
            text_rect = ready_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 25))
            self.screen.blit(ready_text, text_rect)
    
    def draw_menu(self):
        """Draw main menu"""
        self.draw_background()
        
        title = self.font.render("JAGUAR HUNT", True, GOLD)
        title_shadow = self.font.render("JAGUAR HUNT", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 150))
        
        self.screen.blit(title_shadow, (title_rect.x + 3, title_rect.y + 3))
        self.screen.blit(title, title_rect)
        
        instructions = [
            "Press SPACE to Start",
            "",
            "Controls:",
            "Arrow Keys / WASD - Move",
            "SPACE - Pounce",
            "ESC - Pause",
            "",
            "Hunt prey, avoid obstacles!"
        ]
        
        y_offset = 280
        for line in instructions:
            text = self.small_font.render(line, True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
            self.screen.blit(text, text_rect)
            y_offset += 40
    
    def draw_game_over(self):
        """Draw game over screen"""
        self.draw_background()
        
        game_over_text = self.font.render("GAME OVER", True, RED)
        game_over_shadow = self.font.render("GAME OVER", True, BLACK)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        
        self.screen.blit(game_over_shadow, (text_rect.x + 3, text_rect.y + 3))
        self.screen.blit(game_over_text, text_rect)
        
        score_text = self.small_font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.screen.blit(score_text, score_rect)
        
        high_text = self.small_font.render(f"High Score: {self.high_score}", True, GOLD)
        high_rect = high_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
        self.screen.blit(high_text, high_rect)
        
        restart_text = self.small_font.render("Press R to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
        self.screen.blit(restart_text, restart_rect)
    
    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.state == MENU:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                
                elif self.state == PLAYING:
                    if event.key == pygame.K_SPACE:
                        if self.jaguar and self.jaguar.pounce():
                            # Create pounce particles
                            for _ in range(10):
                                particle = Particle(self.jaguar.x + self.jaguar.width // 2,
                                                  self.jaguar.y + self.jaguar.height // 2,
                                                  GOLD)
                                self.particle_group.add(particle)
                    
                    if event.key == pygame.K_ESCAPE:
                        self.state = PAUSED
                
                elif self.state == GAME_OVER:
                    if event.key == pygame.K_r:
                        self.reset_game()
                
                elif self.state == PAUSED:
                    if event.key == pygame.K_ESCAPE:
                        self.state = PLAYING
        
        return True
    
    def update(self):
        """Update game state"""
        if self.state != PLAYING:
            return
        
        keys = pygame.key.get_pressed()
        
        # Update jaguar
        if self.jaguar:
            self.jaguar.update(keys)
        
        # Spawn enemies
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_timer = 0
            
            if random.random() < 0.7:
                prey = Prey()
                self.prey_group.add(prey)
                self.all_sprites.add(prey)
            else:
                obstacle = Obstacle()
                self.obstacle_group.add(obstacle)
                self.all_sprites.add(obstacle)
        
        # Update sprites
        self.prey_group.update()
        self.obstacle_group.update()
        self.particle_group.update()
        
        # Check collisions with prey
        if self.jaguar and self.jaguar.pouncing:
            caught_prey = pygame.sprite.spritecollide(self.jaguar, self.prey_group, True)
            for prey in caught_prey:
                self.score += prey.points
                # Create catch particles
                for _ in range(15):
                    particle = Particle(prey.rect.centerx, prey.rect.centery, GOLD)
                    self.particle_group.add(particle)
        
        # Check collisions with obstacles
        if self.jaguar:
            hit_obstacles = pygame.sprite.spritecollide(self.jaguar, self.obstacle_group, True)
            if hit_obstacles:
                self.lives -= 1
                # Create damage particles
                for _ in range(20):
                    particle = Particle(self.jaguar.x + self.jaguar.width // 2,
                                      self.jaguar.y + self.jaguar.height // 2,
                                      RED)
                    self.particle_group.add(particle)
                
                if self.lives <= 0:
                    if self.score > self.high_score:
                        self.high_score = self.score
                    self.state = GAME_OVER
        
        # Increase difficulty
        self.difficulty_timer += 1
        if self.difficulty_timer >= 300:
            self.difficulty_timer = 0
            self.spawn_rate = max(30, self.spawn_rate - 2)
    
    def draw(self):
        """Draw everything"""
        if self.state == MENU:
            self.draw_menu()
        elif self.state == GAME_OVER:
            self.draw_game_over()
        else:
            self.draw_background()
            
            # Draw sprites
            self.prey_group.draw(self.screen)
            self.obstacle_group.draw(self.screen)
            self.particle_group.draw(self.screen)
            
            if self.jaguar:
                self.screen.blit(self.jaguar.image, self.jaguar.rect)
            
            self.draw_ui()
            
            if self.state == PAUSED:
                pause_text = self.font.render("PAUSED", True, WHITE)
                pause_shadow = self.font.render("PAUSED", True, BLACK)
                text_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                self.screen.blit(pause_shadow, (text_rect.x + 3, text_rect.y + 3))
                self.screen.blit(pause_text, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()