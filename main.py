import random
import pygame


class Button():
    def __init__(self, x, y, pos, width, height):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = width
        self.height = height
        
        
    def clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False


class RpsGame():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("Rock Paper Scissors")

        self.bg = pygame.image.load("rps/bg.png")
        self.bg = pygame.transform.scale(self.bg, (960, 640))
        self.r_btn = pygame.image.load("rps/rock.png").convert_alpha()
        self.p_btn = pygame.image.load("rps/paper.png").convert_alpha()
        self.s_btn = pygame.image.load("rps/scissors.png").convert_alpha()

        self.choose_rock = pygame.image.load("rps/r.png").convert_alpha()
        self.choose_rock = pygame.transform.scale(self.choose_rock, (150, 150))
        self.choose_paper = pygame.image.load("rps/p.png").convert_alpha()
        self.choose_paper = pygame.transform.scale(self.choose_paper, (150, 150))
        self.choose_scissors = pygame.image.load("rps/s.png").convert_alpha()
        self.choose_scissors = pygame.transform.scale(self.choose_scissors, (150, 150))

        self.tie = pygame.image.load("rps/tie.png").convert_alpha()
        self.win = pygame.image.load("rps/win.png").convert_alpha()
        self.lose = pygame.image.load("rps/lose.png").convert_alpha()
        self.pc_random_choice = ""

        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))

        self.rock_btn = Button(30, 520, (30, 520), 250, 100)
        self.paper_btn = Button(340, 520, (340, 520), 250, 100)
        self.scissors_btn = Button(640, 520, (640, 520), 250, 100)


    

    def output(self):
        global pc
        pc = self.pc_random_choice
        
        
        if self.rock_btn.clicked(30):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (200, 200))
            if pc == "rock":
                self.screen.blit(self.tie, (360, 50))
            elif pc == "paper":
                self.screen.blit(self.lose, (360, 50))
            elif pc == "scissors":
                self.screen.blit(self.win, (360, 50))
        elif self.paper_btn.clicked(30):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (200, 200))
            if pc == "rock":
                self.screen.blit(self.win, (360, 50))
            elif pc == "paper":
                self.screen.blit(self.tie, (360, 50))
            elif pc == "scissors":
                self.screen.blit(self.lose, (360, 50))
        elif self.scissors_btn.clicked(30):
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors, (200, 200))
            if pc == "rock":
                self.screen.blit(self.lose, (360, 50))
            elif pc == "paper":
                self.screen.blit(self.win, (360, 50))
            elif pc == "scissors":
                self.screen.blit(self.tie, (360, 50))

        return self.p_option, pc
        

    def computer(self):
        self.pc_random_choice = " "
        option = ["rock", "paper", "scissors"]
        pc_choice = random.choice(list(option))
        if pc_choice == "rock":
            self.pc_random_choice = "rock"
            pc_choice = self.choose_rock
        elif pc_choice == "paper":
            self.pc_random_choice = "paper"
            pc_choice = self.choose_paper
        else:
            self.pc_random_choice = "scissors"
            pc_choice = self.choose_scissors
        pc_option = self.screen.blit(pc_choice, (600, 200))
        return pc_option




    def image_reset(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        pass

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()
        rps_game = RpsGame()
        
        while run:
            pygame.display.update()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rock_btn.clicked(30) or self.paper_btn.clicked(340) or self.scissors_btn.clicked(640):
                        rps_game.image_reset()
                        rps_game.computer()
                        rps_game.output()
                        pc = self.pc_random_choice
                        
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()


if __name__ == '__main__':
    game = RpsGame()
    game.game_loop()
