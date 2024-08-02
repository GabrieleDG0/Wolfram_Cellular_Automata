import pygame
import sys

w = 8
width, height = 1000, 700
cells = []
generation = 0
ruleset = [0] * 8  # User input
input_active = True
user_input = ""

def setup():
    global cells, generation
    cells = [[0] * (width // w)]
    cells[0][len(cells[0]) // 2] = 1
    generation = 0  # Reset generation count

def draw(screen):
    global generation, cells

    for gen in range(generation + 1):
        for i in range(len(cells[0])):
            if cells[gen][i] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (i * w, gen * w, w, w))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (i * w, gen * w, w, w))

    for i in range(0, width, w):
        pygame.draw.line(screen, (180, 180, 180), (i, 0), (i, height))  # Vertical lines 
    for j in range(0, height, w):
        pygame.draw.line(screen, (180, 180, 180), (0, j), (width, j))  # Horizontal lines

    if generation < height // w:
        generate()

def generate():
    global generation, cells

    nextgen = [0] * len(cells[0])
    for i in range(len(cells[0])):
        left = cells[generation][(i - 1) % len(cells[0])]
        me = cells[generation][i]
        right = cells[generation][(i + 1) % len(cells[0])]
        nextgen[i] = rules(left, me, right)

    cells.append(nextgen)
    generation += 1

def rules(a, b, c):
    index = a * 4 + b * 2 + c
    return ruleset[7 - index]

def convert_decimal_to_binary(decimal):
    binary = [int(x) for x in format(decimal, '08b')]
    return binary

def is_valid_input(text):
    """Check if the input is a valid number between 0 and 255."""
    if not text.isdigit():
        return False
    number = int(text)
    return 0 <= number <= 255

def draw_input_area(screen, input_box, prompt_text, user_input, color, text_color, input_active):
    font = pygame.font.Font(None, 35)
    prompt_font = pygame.font.Font(None, 28)

    # Draw background for input area
    input_area_rect = pygame.Rect(0, 0, 400, 200)
    input_area_rect.center = (width // 2, height // 2)
    pygame.draw.rect(screen, pygame.Color('lightblue'), input_area_rect, border_radius=15)

    # Draw prompt text
    prompt_surface = prompt_font.render(prompt_text, True, text_color)
    prompt_rect = prompt_surface.get_rect(center=(input_area_rect.centerx, input_area_rect.centery - 50))
    screen.blit(prompt_surface, prompt_rect)

    # Draw input box with rounded corners
    pygame.draw.rect(screen, color, input_box, border_radius=10)
    
    # Draw input text
    txt_surface = font.render(user_input, True, text_color)
    txt_rect = txt_surface.get_rect(center=input_box.center)
    screen.blit(txt_surface, txt_rect)

def main():
    global ruleset, user_input, input_active

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Wolfram - Cellular Automata")

    input_box = pygame.Rect(0, 0, 220, 50)
    input_box.center = (width // 2, height // 2)  # Center the input box

    color_inactive = pygame.Color('grey')
    color_active = pygame.Color('dodgerblue')
    color = color_active if input_active else color_inactive
    text_color = pygame.Color('black')  # Text color black

    prompt_text = 'Enter Ruleset (0 - 255):'

    setup()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                color = color_active if input_active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset and allow new input
                    input_active = True
                    user_input = ""
                    setup()  # Reset cells and generation
                elif input_active:
                    if event.key == pygame.K_RETURN:
                        if is_valid_input(user_input):
                            ruleset = convert_decimal_to_binary(int(user_input))
                            user_input = ''
                            input_active = False
                            setup()  # Reset cells after ruleset input
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

        screen.fill((255, 255, 255))

        if input_active:
            draw_input_area(screen, input_box, prompt_text, user_input, color, text_color, input_active)
        else:
            # Draw the grid and pattern
            draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
