import pygame,sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

        self.head_up = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-up.png").convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up,(cell_size,cell_size))
        self.head_down = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-down.png").convert_alpha()
        self.head_down = pygame.transform.scale(self.head_down,(cell_size,cell_size))
        self.head_right = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-right.png").convert_alpha()
        self.head_right = pygame.transform.scale(self.head_right,(cell_size,cell_size))
        self.head_left = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-left.png").convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left,(cell_size,cell_size))
        
        self.tail_up = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-tail-up.png").convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up,(cell_size,cell_size))
        self.tail_down = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-tail-down.png").convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down,(cell_size,cell_size))
        self.tail_left = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-tail-left.png").convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left,(cell_size,cell_size))
        self.tail_right = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-tail-right.png").convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right,(cell_size,cell_size))

        self.body_vertical = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-body-vertical.png").convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical,(cell_size,cell_size))
        self.body_horizontal = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-body-horizontal.png").convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal,(cell_size,cell_size))

        self.body_tr = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-top-right.png").convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr,(cell_size,cell_size))
        self.body_tl = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-top-left.png").convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl,(cell_size,cell_size))
        self.body_br = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-bottom-right.png").convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br,(cell_size,cell_size))
        self.body_bl = pygame.image.load(r"C:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\snake-bottom-left.png").convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl,(cell_size,cell_size))
        
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        
        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] -block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)     

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):
            self.head = self.head_left
        elif head_relation == Vector2(-1,0):
            self.head = self.head_right
        elif head_relation == Vector2(0,1):
            self.head = self.head_up
        elif head_relation == Vector2(0,-1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1):
            self.tail = self.tail_down
                        
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 ==0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)


pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))      
clock = pygame.time.Clock()
apple = pygame.image.load(r"c:\Users\aksha\OneDrive\Documents\Python\SNAKE GAME\apple.png").convert_alpha()
apple = pygame.transform.scale(apple,(cell_size,cell_size))
game_font = pygame.font.Font(None,25)

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


while True:                                      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            
    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)                               
    
