import pygame
import math

# --- 1. GAME SETTINGS & SETUP ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FOV = math.pi / 3  # 60-degree field of view
HALF_FOV = FOV / 2
NUM_RAYS = 120  # Number of rays cast (resolution of 3D view)
DELTA_ANGLE = FOV / NUM_RAYS
DIST_TO_PROJ_PLANE = (SCREEN_WIDTH / 2) / math.tan(HALF_FOV)

# Map definition (1 = Wall, 0 = Empty Path)
MAP_SIZE = 8
TILE_SIZE = 64
GAME_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python DOOM-style Engine")
clock = pygame.time.Clock()

# --- 2. PLAYER VARIABLE INITIALIZATION ---
player_x = 150.0
player_y = 150.0
player_angle = 0.0
player_speed = 3.0
rotation_speed = 0.05

# --- 3. MAIN GAME LOOP ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard Controls for Movement and Rotation
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle -= rotation_speed
    if keys[pygame.K_RIGHT]:
        player_angle += rotation_speed
        
    # Standard translation vectors
    cos_a = math.cos(player_angle)
    sin_a = math.sin(player_angle)
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        new_x = player_x + player_speed * cos_a
        new_y = player_y + player_speed * sin_a
        # Collision detection against the map array boundaries
        if GAME_MAP[int(new_y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
            player_x, player_y = new_x, new_y
            
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        new_x = player_x - player_speed * cos_a
        new_y = player_y - player_speed * sin_a
        if GAME_MAP[int(new_y / TILE_SIZE)][int(new_x / TILE_SIZE)] == 0:
            player_x, player_y = new_x, new_y

    # Clear screen with background color splits (Ceiling and Floor)
    pygame.draw.rect(screen, (30, 30, 30), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT // 2))  # Dark grey ceiling
    pygame.draw.rect(screen, (70, 70, 70), (0, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT // 2))  # Light grey floor

    # --- 4. THE RAYCASTING ENGINE ---
    start_angle = player_angle - HALF_FOV
    
    for ray in range(NUM_RAYS):
        # Cast a ray incrementally until it collides with a wall block
        ray_angle = start_angle + ray * DELTA_ANGLE
        cos_r = math.cos(ray_angle)
        sin_r = math.sin(ray_angle)
        
        for distance in range(1, 800):  # Maximum render distance bound
            target_x = player_x + distance * cos_r
            target_y = player_y + distance * sin_r
            
            map_col = int(target_x / TILE_SIZE)
            map_row = int(target_y / TILE_SIZE)
            
            # Prevent out-of-bounds array lookups
            if 0 <= map_row < MAP_SIZE and 0 <= map_col < MAP_SIZE:
                if GAME_MAP[map_row][map_col] == 1:
                    # Fish-eye lens correction logic
                    corrected_dist = distance * math.cos(ray_angle - player_angle)
                    
                    # Calculate the exact slice height to project onto screen space
                    proj_wall_height = (TILE_SIZE / (corrected_dist + 0.0001)) * DIST_TO_PROJ_PLANE
                    
                    # Determine color shading gradient based on proximity depth
                    shade = 255 / (1 + corrected_dist * corrected_dist * 0.0001)
                    wall_color = (shade, shade // 2, shade // 4)  # Retro brownish-red tint
                    
                    # Draw the column vertical strip slice
                    scale_factor = SCREEN_WIDTH / NUM_RAYS
                    pygame.draw.rect(screen, wall_color, (
                        ray * scale_factor, 
                        (SCREEN_HEIGHT / 2) - (proj_wall_height / 2), 
                        scale_factor + 1, 
                        proj_wall_height
                    ))
                    break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

