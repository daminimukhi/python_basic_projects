import pygame
import random

# Initialize Sudoku grid
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Constants
WIDTH, HEIGHT = 540, 540
GRID_SIZE = WIDTH // 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

# Difficulty levels
DIFFICULTY = {
    'easy': 25,
    'medium': 35,
    'hard': 45,
}

# Selected difficulty level
selected_difficulty = None

# Initialize pygame and the font
pygame.init()
font = pygame.font.Font(None, FONT_SIZE)

# Initialize the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Define the new game button
NEW_GAME_BUTTON_RECT = pygame.Rect(400, 10, 100, 30)
NEW_GAME_BUTTON_COLOR = (0, 255, 0)
NEW_GAME_TEXT_COLOR = (0, 0, 0)
font_new_game = pygame.font.Font(None, 32)
new_game_text = font_new_game.render("New Game", True, NEW_GAME_TEXT_COLOR)

# Define the check button
CHECK_BUTTON_RECT = pygame.Rect(400, 50, 100, 30)
CHECK_BUTTON_COLOR = (255, 0, 0)
CHECK_TEXT_COLOR = (0, 0, 0)
font_check = pygame.font.Font(None, 32)
check_text = font_check.render("Check", True, CHECK_TEXT_COLOR)

# Function to draw the Sudoku grid
def draw_grid():
    for i in range(10):
        thick = 2 if i % 3 == 0 else 1
        pygame.draw.line(window, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), thick)
        pygame.draw.line(window, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT), thick)

# Function to check if the Sudoku puzzle is solved
def is_solved(puzzle):
    # Check rows, columns, and 3x3 subgrids
    for i in range(9):
        if len(set(puzzle[i])) != 9:
            return False
        if len(set(row[i] for row in puzzle)) != 9:
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [puzzle[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subgrid)) != 9:
                return False
    return True

# Function to generate a Sudoku puzzle with a specified number of initial values
def generate_sudoku(difficulty):
    puzzle = [[0] * 9 for _ in range(9)]
    for _ in range(DIFFICULTY[difficulty]):
        row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        while puzzle[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        while not is_valid_move(puzzle, row, col, num):
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        puzzle[row][col] = num
    return puzzle

# Function to check if a move is valid
def is_valid_move(puzzle, row, col, num):
    # Check row
    if num in puzzle[row]:
        return False
    # Check column
    if num in [puzzle[i][col] for i in range(9)]:
        return False
    # Check 3x3 subgrid
    subgrid_x, subgrid_y = col // 3, row // 3
    for i in range(subgrid_y * 3, (subgrid_y + 1) * 3):
        for j in range(subgrid_x * 3, (subgrid_x + 1) * 3):
            if puzzle[i][j] == num:
                return False
    return True

# Initialize the current row and column to zero
row, col = 0, 0

# Initialize a variable to track if the puzzle is solved
puzzle_solved = False

# Rectangles for difficulty level buttons
DIFFICULTY_RECTS = []
DIFFICULTY_TEXTS = []
for i, (difficulty, count) in enumerate(DIFFICULTY.items()):
    rect = pygame.Rect(50 + i * 100, 500, 100, 40)
    DIFFICULTY_RECTS.append((difficulty, rect))
    text = font.render(difficulty.capitalize(), True, BLACK)
    DIFFICULTY_TEXTS.append(text)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not puzzle_solved:
                if event.unicode.isnumeric() and grid[row][col] == 0:
                    num = int(event.unicode)
                    grid[row][col] = num
            if event.key == pygame.K_RETURN:
                if not puzzle_solved:
                    if is_solved(grid):
                        print("Sudoku solved correctly!")
                        puzzle_solved = True
                    else:
                        print("Sudoku solution is incorrect.")
            if event.key == pygame.K_RIGHT:
                col = (col + 1) % 9  # Move right
            elif event.key == pygame.K_LEFT:
                col = (col - 1) % 9  # Move left
            elif event.key == pygame.K_DOWN:
                row = (row + 1) % 9  # Move down
            elif event.key == pygame.K_UP:
                row = (row - 1) % 9  # Move up
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if NEW_GAME_BUTTON_RECT.collidepoint(x, y):
                # Generate a new Sudoku puzzle
                if selected_difficulty:
                    grid = generate_sudoku(selected_difficulty)
                puzzle_solved = False
            for difficulty, rect in DIFFICULTY_RECTS:
                if rect.collidepoint(x, y):
                    selected_difficulty = difficulty
                    grid = generate_sudoku(selected_difficulty)
                    puzzle_solved = False

    window.fill(WHITE)
    draw_grid()
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                window.blit(text, (j * GRID_SIZE + 15, i * GRID_SIZE + 10))
    pygame.draw.rect(window, (0, 0, 255), (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 2)  # Highlight current cell
    pygame.draw.rect(window, NEW_GAME_BUTTON_COLOR, NEW_GAME_BUTTON_RECT)
    window.blit(new_game_text, (NEW_GAME_BUTTON_RECT.x + 10, NEW_GAME_BUTTON_RECT.y + 5))
    
    for i, (diff, rect) in enumerate(DIFFICULTY_RECTS):
        pygame.draw.rect(window, (0, 255, 0) if diff == selected_difficulty else (255, 0, 0), rect)
        window.blit(DIFFICULTY_TEXTS[i], (rect.x + 10, rect.y + 5))
    
    pygame.display.update()

pygame.quit()
