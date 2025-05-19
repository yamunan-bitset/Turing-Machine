import pygame
import sys
import turing

pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turing Machine Visualization")

rules = [
    ['1RB', '1LB'],
    ['1LA', '0LC'],
    ['---', '1LD'],
    ['1RD', '0RA']
] # BB(4) champion, should halt after BB(4)=107 steps
tm = turing.TuringMachine(rules, start_length=3)

font = pygame.font.SysFont(None, 48)

rect = []
num_rows = 1
start_row = (HEIGHT // 60 - num_rows) // 2
for row in range(start_row, start_row + num_rows):
    for col in range(1, len(tm.number_sequence)):
        rect.append(pygame.Rect(col * 60, row * 60, 60, 60))

current_rule = font.render("Current rule: " + str(rules[tm.current_rule]), True, (200, 0, 0))

rules_txt = [
    [font.render("Instructions:", True, (200, 0, 0)), font.render("", True, (200, 0, 0))],
    [font.render("0", True, (200, 0, 0)), font.render("1", True, (200, 0, 0))]
]
rules_txt = [
    ["Instructions:", ""],
    ["0", "1"]
]

for i in rules:
    rules_txt.append([str(i[0]), str(i[1])])

text = []
for i in range(1, len(tm.number_sequence)):
    text.append(font.render(str(tm.number_sequence[i]), True, (200, 0, 0)))

offset = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not tm.done:
                if event.key == pygame.K_SPACE:
                    tm.next_move()
                    rect = []
                    num_rows = 1
                    start_row = (HEIGHT // 60 - num_rows) // 2
                    for row in range(start_row, start_row + num_rows):
                        for col in range(1, len(tm.number_sequence)):
                            rect.append(pygame.Rect(col * 60, row * 60, 60, 60))
                    
                    current_rule = font.render("Current rule: " + str(rules[tm.current_rule]), True, (200, 0, 0))

                    text = []
                    for i in range(1, len(tm.number_sequence)):
                        text.append(font.render(str(tm.number_sequence[i]), True, (200, 0, 0)))

    screen.fill((173, 216, 230))

    for x in range(0, WIDTH, 60):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, 60):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (WIDTH, y))

    for i in range(len(rect)):
        pygame.draw.rect(screen, (255, 255, 255) if tm.number_sequence[i + 1] == 0 else (10, 10, 40), rect[i])

    screen.blit(font.render("Turing machine halted after " + str(tm.number_of_moves) + " moves" if tm.done 
                            else "Step: " + str(tm.number_of_moves) + " moves", True, (200, 0, 0)), (50, HEIGHT-100))


    for i in range(len(tm.number_sequence) - 1):
        screen.blit(text[i], text[i].get_rect(center=rect[i].center))
    screen.blit(current_rule, (0, 0))
    for i in range(len(rules) + 1):
        if i > 1: screen.blit(font.render("Rule: " + chr(ord('@') + i - 1), True, (200, 0, 0)), (WIDTH/2 - 150, 50 + i * 50))
        screen.blit(font.render(rules_txt[i][0], True, (200, 0, 0)), (WIDTH/2, 50 + i * 50))
        screen.blit(font.render(rules_txt[i][1], True, (200, 0, 0)), (WIDTH/2 + 100, 50 + i * 50))

    pygame.draw.rect(screen, (0, 200, 0), rect[tm.current_pos - 1], 2)

    pygame.display.flip()

pygame.quit()
sys.exit()