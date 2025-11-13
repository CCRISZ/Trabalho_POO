import pygame
from aa import *

pygame.init()
tela = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

antonio = Antonio()
boco = Inimigo_um()
inimigos = [boco]  
x, y = 300, 300
velocidade = 3
direcao = "right"
rodando = True

while rodando:
    tempo_atual = pygame.time.get_ticks()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
        direcao = "left"
    elif teclas[pygame.K_RIGHT]:
        x += velocidade
        direcao = "right"
    elif teclas[pygame.K_UP]:
        y -= velocidade
    elif teclas[pygame.K_DOWN]:
        y += velocidade

    tela.fill((0, 0, 0))

    # ======= JOGADOR =======
    pygame.draw.rect(tela, (255, 255, 0), (x, y, 40, 40))
    antonio.desenhar_barra_vida(tela, x, y)
    antonio.rect = pygame.Rect(x, y, 40, 40)

    # ======= INIMIGOS =======
    for inimigo in inimigos[:]:  # copia pra poder remover durante iteração
        inimigo.mover_para(x, y)
        inimigo.atacar(antonio, tempo_atual)

        # Se o inimigo ainda tiver vida, desenha
        if inimigo.vida_atual > 0:
            pygame.draw.rect(tela, inimigo.cor, inimigo.get_rect())
        else:
            print(f"{inimigo.nome} foi derrotado!")
            inimigos.remove(inimigo)  # remove o inimigo da lista

    # ======= ATAQUE DO PERSONAGEM =======
    for arma in antonio.armas:
        if isinstance(arma, Whip):
            arma.attack(tempo_atual, x, y, direcao, inimigos)
            arma.update(tempo_atual)
            arma.draw(tela)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
