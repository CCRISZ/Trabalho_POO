import pygame
pygame.init()

def tiros_multidirecionais(x, y):
    direcoes = [
        (0, -1), (0, 1), (-1, 0), (1, 0),  # Cima, baixo, esquerda, direita
        (1, -1), (-1, -1), (1, 1), (-1, 1)  # Diagonais
    ]
    for dx, dy in direcoes:
        rect_tiro = pygame.Rect(x + 20, y + 20, 10, 10)
        tiros.append([rect_tiro, (dx, dy)])  # salva o rect + direção

# ===== CONFIGURAÇÃO =====
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ataques com Retângulos")

# ===== JOGADOR =====
x, y = 100, 300
velocidade = 0.5

# ===== INIMIGO =====
inimigo_x, inimigo_y = 600, 300
inimigo_vel = 0.2

# ===== PROJÉTEIS =====
tiros = []
vel_tiro = 5
ultimo_tiro = 0
intervalo_tiro = 2000  # a cada 2 segundos

rodando = True
clock = pygame.time.Clock()

while rodando:
    clock.tick(60)
    tempo_atual = pygame.time.get_ticks()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # ===== TIRO AUTOMÁTICO A CADA 2 SEGUNDOS =====
    if tempo_atual - ultimo_tiro >= intervalo_tiro:
        tiros_multidirecionais(x, y)
        ultimo_tiro = tempo_atual

    # ===== MOVIMENTO DO JOGADOR =====
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # ===== MOVIMENTO DO INIMIGO =====
    inimigo_x -= inimigo_vel
    if inimigo_x < 0 or inimigo_x > 750:
        inimigo_vel *= -1

    inimigo_rect = pygame.Rect(inimigo_x, inimigo_y, 50, 50)
    jogador_rect = pygame.Rect(x, y, 50, 50)

    # ===== MOVIMENTO DOS TIROS =====
    for tiro in tiros[:]:
        rect, (dx, dy) = tiro
        rect.x += dx * vel_tiro
        rect.y += dy * vel_tiro

        # Remove tiro se sair da tela
        if rect.x < 0 or rect.x > 800 or rect.y < 0 or rect.y > 600:
            tiros.remove(tiro)

        # Checa colisão
        if rect.colliderect(inimigo_rect):
            print("Inimigo atingido!")
            tiros.remove(tiro)

    # ===== DESENHO =====
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, (255, 255, 0), jogador_rect)
    pygame.draw.rect(tela, (255, 0, 0), inimigo_rect)
    for rect, _ in tiros:
        pygame.draw.rect(tela, (0, 150, 255), rect)
    pygame.display.update()

pygame.quit()
