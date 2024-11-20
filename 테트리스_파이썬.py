# pip install pygame
import pygame
import random

# 초기화
pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# 게임 설정
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * (BOARD_WIDTH + 6)
SCREEN_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# 테트리미노 모양
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 1], [1, 1]], # O
    [[1, 1, 1], [0, 1, 0]], # T
    [[1, 1, 1], [1, 0, 0]], # L
    [[1, 1, 1], [0, 0, 1]], # J
    [[1, 1, 0], [0, 1, 1]], # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('테트리스')
        self.clock = pygame.time.Clock()
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.new_piece()
        self.game_over = False
        self.fall_time = 0
        self.fall_speed = 1000  # 1초

    def new_piece(self):
        shape = random.randint(0, len(SHAPES) - 1)
        self.current_piece = {
            'shape': SHAPES[shape],
            'color': COLORS[shape],
            'x': BOARD_WIDTH // 2 - len(SHAPES[shape][0]) // 2,
            'y': 0
        }

    def valid_move(self, dx=0, dy=0, piece=None):
        if piece is None:
            piece = self.current_piece['shape']
        new_x = self.current_piece['x'] + dx
        new_y = self.current_piece['y'] + dy

        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    if (new_x + x < 0 or new_x + x >= BOARD_WIDTH or
                        new_y + y >= BOARD_HEIGHT or
                        new_y + y >= 0 and self.board[new_y + y][new_x + x]):
                        return False
        return True

    def rotate_piece(self):
        new_shape = list(zip(*reversed(self.current_piece['shape'])))
        if self.valid_move(piece=new_shape):
            self.current_piece['shape'] = new_shape

    def freeze_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_piece['y'] + y][self.current_piece['x'] + x] = self.current_piece['color']

    def clear_lines(self):
        lines_cleared = 0
        for y in range(BOARD_HEIGHT - 1, -1, -1):
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0] * BOARD_WIDTH)
                lines_cleared += 1
        self.score += lines_cleared * 100

    def draw(self):
        self.screen.fill(BLACK)
        
        # 보드 그리기
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, cell,
                                   [x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 현재 조각 그리기
        if self.current_piece:
            for y, row in enumerate(self.current_piece['shape']):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, self.current_piece['color'],
                                       [(self.current_piece['x'] + x) * BLOCK_SIZE,
                                        (self.current_piece['y'] + y) * BLOCK_SIZE,
                                        BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 점수 표시
        score_text = self.font.render(f'점수: {self.score}', True, WHITE)
        self.screen.blit(score_text, (BOARD_WIDTH * BLOCK_SIZE + 10, 10))

        pygame.display.flip()

    def run(self):
        while not self.game_over:
            self.fall_time += self.clock.get_rawtime()
            self.clock.tick()

            if self.fall_time >= self.fall_speed:
                if self.valid_move(dy=1):
                    self.current_piece['y'] += 1
                else:
                    self.freeze_piece()
                    self.clear_lines()
                    self.new_piece()
                    if not self.valid_move():
                        self.game_over = True
                self.fall_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.valid_move(dx=-1):
                            self.current_piece['x'] -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.valid_move(dx=1):
                            self.current_piece['x'] += 1
                    elif event.key == pygame.K_DOWN:
                        if self.valid_move(dy=1):
                            self.current_piece['y'] += 1
                    elif event.key == pygame.K_UP:
                        self.rotate_piece()
                    elif event.key == pygame.K_SPACE:
                        while self.valid_move(dy=1):
                            self.current_piece['y'] += 1
                        self.freeze_piece()
                        self.clear_lines()
                        self.new_piece()

            self.draw()

        pygame.quit()

if __name__ == '__main__':
    game = Tetris()
    game.run()