import pygame


pygame.init()

# init screen
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("My rover")

# creating object rover
rover_rect = pygame.Rect(100, 100, 50, 50)  # (x, y, width, height)
rover_color = (245, 212, 125)  # green 
speed = 1  # speed
avoid_speed = speed * 8

# creating obstacle
obstacle_rect = pygame.Rect(300, 200, 100, 100)  # (x, y, width, height)
obstacle_color = (255, 0, 0)  # red
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # LOGIC: moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: rover_rect.x -= speed
    if keys[pygame.K_RIGHT]: rover_rect.x += speed
    if keys[pygame.K_UP]: rover_rect.y -= speed
    if keys[pygame.K_DOWN]: rover_rect.y += speed

    # LOGIC: lidar
    lidar_start_pos = (rover_rect.centerx, rover_rect.centery)
    lidar_end_pos = (rover_rect.centerx + 200, rover_rect.centery)
    lidar_collision = obstacle_rect.clipline(lidar_start_pos, lidar_end_pos)
    
    # LOGIC: second lidar
    lidar_start_pos_1 = (rover_rect.centerx, rover_rect.centery)
    lidar_end_pos_1 = (rover_rect.centerx - 200, rover_rect.centery)
    lidar_collision_1 = obstacle_rect.clipline(lidar_start_pos_1, lidar_end_pos_1)

    # drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, rover_color, rover_rect)  # drawing rover
    pygame.draw.rect(screen, obstacle_color, obstacle_rect)  # drawing obstacle

    # LOGIC: avoiding obstacle
    if lidar_collision:
        rover_rect.x -= avoid_speed
    
    if lidar_collision_1:
        rover_rect.x += avoid_speed

    # visualising lidar
    lidar_color = (255, 0, 0) if lidar_collision else (0, 255, 0)
    pygame.draw.line(screen, lidar_color, lidar_start_pos, lidar_end_pos, 2)
    lidar_color_1 = (255, 0, 0) if lidar_collision_1 else (0, 255, 0)
    pygame.draw.line(screen, lidar_color_1, lidar_start_pos_1, lidar_end_pos_1, 2)
    
    pygame.display.flip()
pygame.quit()
