# The first half is just boiler-plate stuff...

import pygame

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# The rest is code where you implement your game using the Scenes model

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.menu_items = ["New Game", "Continue", "Exit"]
        self.active_item_index = 0
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                if(self.active_item_index == 2):
                    self.Terminate()
                else:
                    self.SwitchToScene(GameScene())
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.active_item_index = self.active_item_index - 1
                if self.active_item_index < 0:
                    self.active_item_index = len(self.menu_items)  - 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.active_item_index = self.active_item_index + 1
                if self.active_item_index >= len(self.menu_items):
                    self.active_item_index = 0
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))
        font = pygame.font.SysFont("comicsansms", 20)
        for i in range(len(self.menu_items)):
            title = self.menu_items[i]

            if i == self.active_item_index:
                title = "+" + title

            text = font.render(title, True, (0, 0, 0))
            screen.blit(text, (150, 50 + i * 20))


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))

run_game(400, 300, 60, TitleScene())# The first half is just boiler-plate stuff...