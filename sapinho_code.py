# -*- coding: utf-8 -*-
import sys, pygame, os, time
pygame.init()

#estudar isso para grupos: http://www.pygame.org/docs/ref/sprite.html

#CONSTANTES
LADO_QUADRADO=80
TELA_ALTURA=LADO_QUADRADO*7
TELA_LARGURA=LADO_QUADRADO*7
FPS=60 #frames po segundo

TEMPO_TRAVESIA=30
VIDA_INICIAL=3
TELA_TAMANHO = TELA_LARGURA, TELA_ALTURA
AUMENTO_VELOCIDADE=1
tela = pygame.display.set_mode(TELA_TAMANHO)
COR_FUNDO = (0, 0, 0)
COR_LETRAS = (255, 255, 255)

class Chegada(pygame.sprite.Sprite):
	"""classe para o chegada"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.direcaox = 0
		self.direcaoy = 0
		self.imagem, self.rect = carregar_imagem('chegada.png')
		pos_incio=calcula_pos(1,4)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
		
	def terminou_fase(self, personagem):
		if pygame.sprite.collide_rect(self, personagem)== 1:
			return 1;
		else: return 0;
		
class Calcada(pygame.sprite.Sprite):
	"""classe para o chegada"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.direcaox = 0
		self.direcaoy = 0
		self.imagem, self.rect = carregar_imagem('calcada.png')
		pos_incio=calcula_pos(6,4)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]


class Sapo(pygame.sprite.Sprite):
	"""classe para o sapo"""
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		self.vivo=1
		self.direcaox = 0
		self.direcaoy = 0
		self.imagem, self.rect = carregar_imagem('sapo.png')
		pos_incio=calcula_pos(linha,coluna)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
    
	def parar(self):
		self.rect.move_ip(0,0)
		
	def update(self):
		self.rect.move_ip(self.direcaox*LADO_QUADRADO,self.direcaoy*LADO_QUADRADO)
		
	def posicionar(self, linha, coluna):
		pos=calcula_pos(linha,coluna)
		self.rect.centerx = pos[0]
		self.rect.centery = pos[1]
			
	def morte(self,posx,posy,tempo):
		#self.vivo=0
		
		if tempo == FPS:
			self.vivo=0
			self.imagem, self.rect = carregar_imagem('sapo_morto.png')
			self.rect.centerx = posx
			self.rect.centery = posy

		elif tempo == 0:
			self.vivo=1
			self.imagem, self.rect = carregar_imagem('sapo.png')		
			self.posicionar(6,4)
			#tela.blit(self.imagem, self.rect)

		
		#reiniciar()		
			
	def destruir(self):
		del(self)
	#def colidir(self):
class Carro(pygame.sprite.Sprite):
	"""classe para a carro"""
	def __init__(self, linha, coluna, velocidade):
		pygame.sprite.Sprite.__init__(self)
		self.velocidade = [velocidade,0]
		self.imagem, self.rect = carregar_imagem('carro.png')
		pos_incio=calcula_pos(linha,coluna)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
		self.init_pos = pos_incio
    
	def muda_velocidade(self, multiplicador):
		self.velocidade = multiplicador*self.velocidade
	
	def posicionar(self, linha, coluna):
		pos=calcula_pos(linha,coluna)
		self.rect.centerx = pos[0]
		self.rect.centery = pos[1]
	
	def update(self):
		self.rect.move_ip(self.velocidade)
		
		if self.rect.left < -LADO_QUADRADO and self.velocidade[0] < 0:
			self.rect.centerx = TELA_LARGURA+LADO_QUADRADO/2
		if self.rect.right > TELA_LARGURA+LADO_QUADRADO and self.velocidade[0] > 0:
			self.rect.centerx = -LADO_QUADRADO/2
	
	def destruir(self):
		del(self)
		
	def parar(self):
		self.velocidade= [0,0]
		
class Moto(pygame.sprite.Sprite):
	"""classe para a moto"""
	def __init__(self, linha, coluna, velocidade):
		pygame.sprite.Sprite.__init__(self)
		self.velocidade = [velocidade,0]
		self.imagem, self.rect = carregar_imagem('moto.png')
		pos_incio=calcula_pos(linha,coluna)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
		self.init_pos = pos_incio
    
	def posicionar(self, linha, coluna):
		pos=calcula_pos(linha,coluna)
		self.rect.centerx = pos[0]
		self.rect.centery = pos[1]
	
	def update(self):
		self.rect.move_ip(self.velocidade)
		
		if self.rect.left < -LADO_QUADRADO and self.velocidade[0] < 0:
			self.rect.centerx = TELA_LARGURA+LADO_QUADRADO/2
		if self.rect.right > TELA_LARGURA+LADO_QUADRADO and self.velocidade[0] > 0:
			self.rect.centerx = -LADO_QUADRADO/2
	
	def destruir(self):
		del(self)
		
	def parar(self):
		self.velocidade= [0,0]
		
class Caminhao(pygame.sprite.Sprite):
	"""classe para a carro"""
	def __init__(self, linha, coluna, velocidade):
		pygame.sprite.Sprite.__init__(self)
		self.velocidade = [velocidade,0]
		self.imagem, self.rect = carregar_imagem('caminhao.png')
		pos_incio=calcula_pos(linha,coluna)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
		self.init_pos = pos_incio
    
	def posicionar(self, linha, coluna):
		pos=calcula_pos(linha,coluna)
		self.rect.centerx = pos[0]
		self.rect.centery = pos[1]
	
	def update(self):
		self.rect.move_ip(self.velocidade)
		
		if self.rect.left < -LADO_QUADRADO and self.velocidade[0] < 0:
			self.rect.centerx = TELA_LARGURA+LADO_QUADRADO/2
		if self.rect.right > TELA_LARGURA+LADO_QUADRADO and self.velocidade[0] > 0:
			self.rect.centerx = -LADO_QUADRADO/2
	
	def destruir(self):
		del(self)
		
	def parar(self):
		self.velocidade= [0,0]
		
		
class Vida(pygame.sprite.Sprite):
	def __init__(self):
		#texto = str(contador_tempo)
		pygame.sprite.Sprite.__init__(self)
		self.velocidade = [0,0]
		self.imagem, self.rect = carregar_imagem('core3.png')
		pos_incio=calcula_pos(7,1)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
		self.init_pos = pos_incio
		self.restante = VIDA_INICIAL
		
		'''
		#Rect(left, top, width, height)
		self.imagem = texto
		self.rect=Rect(self)
		pos_incio=calcula_pos(7, 7)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
		self.init_pos = pos_incio
		texto = str(self.restante)
	'''
	def decrementa(self):
		self.restante=self.restante-1
		if self.restante == 3:
			self.imagem, self.rect = carregar_imagem('core3.png')
		elif self.restante == 2:
			self.imagem, self.rect = carregar_imagem('core2.png')
		elif self.restante == 1:
			self.imagem, self.rect = carregar_imagem('core1.png')
		elif self.restante == 0:
			self.imagem, self.rect = carregar_imagem('core0.png')
		pos_incio=calcula_pos(7,1)
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
		
	def fim_de_jogo(self):
		tela.fill(COR_FUNDO)
		sys.exit()
		
	def texto(self):
		#return str(self.restante)
		return unicode(str(self.restante), "utf-8")
    		
def calcula_pos(linha,coluna):
	if linha == 0:
		x=-LADO_QUADRADO/2
	else:
		if linha > 1:
			x=linha
			x=x-1
			x=x*LADO_QUADRADO
		else:
			x=0
		x+=LADO_QUADRADO/2
	
	if coluna == 0:
		y=-LADO_QUADRADO/2
	else:
		if coluna > 1:
			y=coluna
			y=y-1
			y=y*LADO_QUADRADO
		else:
			y=0
		y+=LADO_QUADRADO/2
	return y,x 
	
def carregar_imagem(name):
	"""carrega uma imagem na memoria, e retorna a imagem e o seu rect (retangulo)"""
#	fullname = os.path.join('imagens', name)
#   try:
	imagem = pygame.image.load(name)
#   except pygame.error, message:
#       print 'Cannot load imagem:', fullname
#       raise SystemExit, message
	return imagem, imagem.get_rect()
			
			
class Pista(pygame.sprite.Sprite):
	def __init__(self,numero_da_pista):
		self.alcancada=0
		pygame.sprite.Sprite.__init__(self)
		self.direcaox = 0
		self.direcaoy = 0
		self.imagem, self.rect = carregar_imagem('pista.png')
		pos_incio=calcula_pos((6-numero_da_pista),4)
		self.lugar=numero_da_pista
		self.rect.centerx = pos_incio[0]
		self.rect.centery = pos_incio[1]
	
	def update(self,pista_do_personagem):
		if self.lugar == pista_do_personagem:
			self.alcancada=1
			
class Fase():
	def __init__(self):
		self.fase_atual=0
		
	def nova_fase(self,vida,tempo):
		self.fase_atual=self.fase_atual+1
		vida.restante=VIDA_INICIAL
		tempo=TEMPO_TRAVESIA
		
		
FATOR_MULTIPLICATIVO_DE_VIDA=0.3
class Pontuacao():
	def __init__(self):
		self.ponto=0
		#COLOCA NO CANTO DA TELA A PONTUACAO
		
	def update(self, pista_atual, pista_maxima):
		if pista_atual==pista_maxima:
			self.ponto=self.ponto+pista_atual
		#COLOCA NO CANTO DA TELA A PONTUACAO
		
	def morre(self, vida, pista, tempo):
		self.ponto = (self.ponto+pista+tempo) + (self.ponto+pista+tempo)*vida*FATOR_MULTIPLICATIVO_DE_VIDA
		#FIMMMM, PONTO FINAL
		
			
	
		
def main():
    #cria os nossos objetos (sapo e veiculos)
	
	velocidade_das_pistas = (0,0,-2,2,-1,1,0,0)
	
	chegada = Chegada()
	calcada = Calcada()
	pista1 = Pista(1)
	pista2 = Pista(2)
	pista3 = Pista(3)
	pista4 = Pista(4)
	
	vida = Vida()
	pontuacao = Pontuacao()
	pontuacao_texto=str(pontuacao.ponto)
	pista_atual=0
	pista_maxima=0

	
	#rua 2:	
	moto21 = Moto(2,8,velocidade_das_pistas[2])
	moto22 = Moto(2,8,velocidade_das_pistas[2])
	
	#rua 3:	
	carro31 = Carro(3,0,velocidade_das_pistas[3])
	
	#rua 4:
	caminhao41 = Caminhao(4,8,velocidade_das_pistas[4])
	caminhao42 = Caminhao(4,8,velocidade_das_pistas[4])
	
	#rua 5:
	carro51 = Carro(5,0,velocidade_das_pistas[5])
	
	
	sapo = Sapo(6,4)
	pygame.display.set_caption('Sapinho!')
	clock = pygame.time.Clock()
    
	veiculos = pygame.sprite.Group()
	veiculos.add(moto21)
	veiculos.add(carro31)
	veiculos.add(caminhao41)
	veiculos.add(carro51)
	  

	#nova_fase
	fase=1
	contador_tempo=TEMPO_TRAVESIA
		
	tempo_animacao_morte=FPS
	tamanho_da_fonte=25
	fundo = 255, 255, 255
	contador_texto = str(contador_tempo).rjust(3)
	pygame.time.set_timer(pygame.USEREVENT, 1000) #evento a cada 1000 milisegundos
	fonte = pygame.font.SysFont('comicsansms', tamanho_da_fonte)
	
	while 1:
		#garante que o programa nao vai rodar a mais que 60fps
		clock.tick(FPS)
        
		pos = calcula_pos(2,3)
		if moto21.rect.centerx == pos[0] and moto21.rect.centery == pos[1] :
			veiculos.add(moto22)
			
		#pos = calcula_pos(3,2)
			
		pos = calcula_pos(4,5)
		if caminhao41.rect.centerx == pos[0] and caminhao41.rect.centery == pos[1] :
			veiculos.add(caminhao42)
			
		#pos = calcula_pos(5,4)
			
		if chegada.terminou_fase(sapo) == 1:
			fase=fase+1
			pista_atual=0
			pista_maxima=0
			time.sleep(1)
			sapo.posicionar(6,4)
			fila=veiculos.sprites()		
			while len(fila) > 0:
				elemento=fila.pop()
				elemento.velocidade[0]=elemento.velocidade[0]+AUMENTO_VELOCIDADE if elemento.velocidade[0] > 0 else elemento.velocidade[0]-AUMENTO_VELOCIDADE
			
		#checa eventos de teclado e tempo
		for event in pygame.event.get():
			if event.type == pygame.USEREVENT:
				if contador_tempo > 0:
					contador_tempo -= 1
				else:
					contador_tempo=TEMPO_TRAVESIA
					vida.decrementa()
				contador_texto = str(contador_tempo).rjust(3)
				pontuacao_texto=str(pontuacao.ponto)
				
			if event.type == pygame.QUIT: 
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if sapo.vivo==1:
					if event.key == pygame.K_LEFT and ( sapo.rect.centerx > (LADO_QUADRADO/2) ):
						sapo.direcaox = -1
						sapo.direcaoy = 0
					elif event.key == pygame.K_RIGHT and ( sapo.rect.centerx < TELA_LARGURA-(LADO_QUADRADO/2) ):
						sapo.direcaox = 1
						sapo.direcaoy = 0
					elif event.key == pygame.K_UP and ( sapo.rect.centery > (LADO_QUADRADO/2) ):
						sapo.direcaox = 0
						sapo.direcaoy = -1
						pista_atual=pista_atual+1  #PONTOOOOOOOOOOOOOOOOOOOOO
						if pista_atual>pista_maxima:
							pista_maxima=pista_atual
						pontuacao.update(pista_atual,pista_maxima)
					elif event.key == pygame.K_DOWN and ( sapo.rect.centery < TELA_ALTURA-(LADO_QUADRADO+LADO_QUADRADO/2) ):
						sapo.direcaox = 0
						sapo.direcaoy = 1
						pista_atual=pista_atual-1
					else:
						sapo.direcaox = 0
						sapo.direcaoy = 0
					sapo.update()
		
		if sapo.vivo == 1:
			veiculo_batido = pygame.sprite.spritecollideany(sapo, veiculos, collided = None)
			if veiculo_batido != None :
				pos_mortex=sapo.rect.centerx
				pos_mortey=sapo.rect.centery
				vida.decrementa()
				tempo_animacao_morte == FPS
				sapo.morte(pos_mortex,pos_mortey,tempo_animacao_morte)
				pista_atual=0
			
		elif sapo.vivo == 0:
			tempo_animacao_morte=tempo_animacao_morte-1
			sapo.morte(pos_mortex,pos_mortey,tempo_animacao_morte)
			if tempo_animacao_morte == 0:
				tempo_animacao_morte=FPS
				pista_alcancada=0
			
		if vida.restante==0 and (tempo_animacao_morte ==1 or contador_tempo ==TEMPO_TRAVESIA):
			vida.fim_de_jogo()
			
		#redesenha a tela
		tela.fill(COR_FUNDO)
		
		tela.blit(fonte.render(contador_texto, True, COR_LETRAS), calcula_pos(7,7))
		tela.blit(fonte.render(pontuacao_texto, True, COR_LETRAS), calcula_pos(7,4))
		
		tela.blit(chegada.imagem, chegada.rect)	
		tela.blit(calcada.imagem, calcada.rect)	
		tela.blit(pista1.imagem, pista1.rect)		
		tela.blit(pista2.imagem, pista2.rect)		
		tela.blit(pista3.imagem, pista3.rect)		
		tela.blit(pista4.imagem, pista4.rect)		
		#atualiza os objetos	
		veiculos.update()
		#pistas.update()
    
		
		#atualiza objetos na tela
		fila=veiculos.sprites()		
		while len(fila) > 0:
			elemento=fila.pop()
			tela.blit(elemento.imagem, elemento.rect)	
		#tela.blit(fonte.render(vida.texto, True, (0, 0, 0)), calcula_pos(7,1))
		tela.blit(sapo.imagem, sapo.rect)
		tela.blit(vida.imagem, vida.rect)
		pygame.display.flip()
    
if __name__ == "__main__":
	main()
