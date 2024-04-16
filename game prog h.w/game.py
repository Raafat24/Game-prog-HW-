import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Road Hazard Game")

# Load resources
road = pygame.image.load("Road.png")
car = pygame.image.load("Car.png")
hazard = pygame.image.load("Hazard.png")
font = pygame.font.SysFont(None, 36)

# Set up initial game variables
road_y = [0, -road.get_height() + 2, -2 * road.get_height() + 4]
velocity_y = 0.3
car_position = pygame.Rect(280, 440, int(car.get_width() * 0.2), int(car.get_height() * 0.2))
hazard_position = pygame.Rect(275, -int(hazard.get_height() * 0.4), int(hazard.get_width() * 0.4), int(hazard.get_height() * 0.4))
move_car_x = 160
current_state = "Running"
def scroll_road():
    global road_y
    for i in range(len(road_y)):
        road_y[i] += int(velocity_y * clock.tick(60) / 1000)
        if road_y[i] >= screen_height:
            last_road_index = i
            for j in range(len(road_y)):
                if road_y[j] < road_y[last_road_index]:
                    last_road_index = j
            road_y[i] = road_y[last_road_index] - road.get_height() + 2

def update_hazard():
    global hazard_position
    hazard_position.y += int(velocity_y * clock.tick(60) / 1000)
    if hazard_position.y > screen_height:
        hazard_position.x = 275
        if random.randint(1, 3) == 2:
            hazard_position.x = 440
        hazard_position.y = -hazard.get_height() * 0.4

def handle_events():
    global move_car_x, current_state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_SPACE and current_state == "Running":
                car_position.x += move_car_x
                move_car_x *= -1
            elif event.key == pygame.K_RETURN and current_state == "Crash":
                start_game()
def start_game():
    global road_y, velocity_y, car_position, hazard_position, current_state
    road_y = [0, -road.get_height() + 2, -2 * road.get_height() + 4]
    velocity_y = 0.3
    car_position = pygame.Rect(280, 440, int(car.get_width() * 0.2), int(car.get_height() * 0.2))
    hazard_position = pygame.Rect(275, -int(hazard.get_height() * 0.4), int(hazard.get_width() * 0.4), int(hazard.get_height() * 0.4))
    current_state = "Running"

clock = pygame.time.Clock()

# Main game loop
while True:
    screen.fill((139, 69, 19))  # SaddleBrown color
    scroll_road()
    update_hazard()
    
    if current_state == "Running":
        screen.blit(road, (0, road_y[0]))
        screen.blit(road, (0, road_y[1]))
        screen.blit(road, (0, road_y[2]))
        screen.blit(car, car_position)
        screen.blit(hazard, hazard_position)
    elif current_state == "Crash":
        screen.blit(font.render("Crash!", True, (255, 255, 255)), (5, 200))
        screen.blit(font.render("'Enter' to play again.", True, (255, 255, 255)), (5, 230))
        screen.blit(font.render("'Escape' to exit.", True, (255, 255, 255)), (5, 260))

    pygame.display.update()
    handle_events()
    clock.tick(60)
