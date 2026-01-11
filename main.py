import pygame
from calculatrice import Calculator


pygame.init()
WIDTH, HEIGHT = 320, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculatrice PyGame")


WHITE = (245, 245, 245)
BLACK = (30, 30, 30)
LIGHT_BLUE = (173, 216, 230)
LIGHT_ORANGE = (255, 200, 150)
LIGHT_GREEN = (144, 238, 144)
LIGHT_RED = (255, 180, 180)


font = pygame.font.SysFont("arial", 28)
display_font = pygame.font.SysFont("arial", 36)

# ----- Classe Button -----
class Button:
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

# ----- Obtenir la couleur -----
def get_button_color(text):
    if text.isdigit() or text == ".":
        return LIGHT_BLUE
    elif text in "+-*/()×":
        return LIGHT_ORANGE
    elif text == "=":
        return LIGHT_GREEN
    elif text in ["C", "←"]:
        return LIGHT_RED

# ----- Grille des boutons -----
grid = [
    ["C", "←", "(", ")"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "/", "="]
]

# ----- Création automatique des boutons -----
buttons = []
button_width = 60
button_height = 50
spacing = 10
margin = 10

for row_index, row in enumerate(grid):
    for col_index, text in enumerate(row):
        x = margin + col_index * (button_width + spacing)
        y = 80 + row_index * (button_height + spacing)
        color = get_button_color(text)
        btn = Button(text, x, y, button_width, button_height, color)
        buttons.append(btn)

# ----- Expression affichée -----
expression = ""

# ----- Boucle principale PyGame -----
running = True
while running:
    screen.fill(WHITE)

    # Afficher l'expression
    expr_surface = display_font.render(expression, True, BLACK)
    screen.blit(expr_surface, (margin, 20))

    # Afficher les boutons
    for btn in buttons:
        pygame.draw.rect(screen, btn.color, btn.rect)
        txt_surface = font.render(btn.text, True, BLACK)
        txt_rect = txt_surface.get_rect(center=btn.rect.center)
        screen.blit(txt_surface, txt_rect)

    # Gestion des clics
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for btn in buttons:
                if btn.rect.collidepoint(mouse_pos):
                    if btn.text == "C":
                        expression = ""
                    elif btn.text == "←":
                        expression = expression[:-1]
                    elif btn.text == "=":
                        try:
                            calc = Calculator(expression.replace("×", "*"))
                            expression = str(calc.calculate())
                        except:
                            expression = "Erreur"
                    else:
                        expression += btn.text

    pygame.display.flip()

pygame.quit()
