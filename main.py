import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Свой курсор мыши')
    black = pygame.Color('black')
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                screen.fill(black)
                sprite = pygame.sprite.Sprite
                sprite.image = pygame.image.load("data/arrow.png")
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = event.pos[0]
                sprite.rect.y = event.pos[1]

                if pygame.mouse.get_focused():
                    pygame.mouse.set_visible(False)
                    screen.blit(sprite.image, sprite.rect)
                pygame.display.update()


    exit()
