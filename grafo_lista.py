import numpy as np


class grafo_lista:
    def __init__(self, V, grafo_orientado):  # Construtor dos atributos básicos
        self.grafo = []  # Lista das arestas e vértices cadastrados
        self.vertices = []  # Lista dos vértices cadastrados
        self.arestas = []
        self.V = V  # Quantidade de vértices
        self.A = 0  # Contador de arestas
        self.criar_vertices(V)  # Cria os vértices do grafo
        self.adj = {}
        self.anterior = {}
        self.f = {}
        self.cor = {}
        self.d = {}
        self.tempo = 0
        self.grafo_orientado = grafo_orientado
        self.comp_conexo = 0
        self.conexo = {}

    def criar_vertices(self, V):  # Cadastra os vértices
        for i in range(0, V):
            vertice = str(input('Informe um vértice: '))
            self.vertices.append(vertice)
        print('\nVértices: ', end='')
        for i in range(0, len(self.vertices)): print('{} '.format(self.vertices[i]), end='')
        print('')

    def checar_grau(self, v):  # Checa o grau do grafo em lista
        cont = 0
        for i in range(0, len(self.grafo)):
            for j in range(0, len(self.grafo[i])):
                if self.grafo[i][0] == v:
                    cont += 1
        if cont >= 1:
            return cont - 1
        else:
            return 0

    def max_grau(self):  # Verifica qual vértice têm o maior grau no grafo em lista
        self.graus = []
        for i in range(0, len(self.vertices)):
            self.vert = []
            self.vert.append(self.checar_grau(self.vertices[i]))
            self.vert.append(self.vertices[i])
            self.graus.append(self.vert)
        self.graus.sort(reverse=True)
        print('\nO vértice {} com grau {} é o maior.'.format(self.graus[0][1], self.graus[0][0]))

    def num_lacos(self):  # Verifica o número de laços no grafo em lista
        self.laco = 0
        for i in range(0, len(self.grafo)):
            for j in range(1, len(self.grafo[i])):
                if self.grafo[i][j] == self.grafo[i][0]:
                    self.laco += 1
        return self.laco

    def grafo_conexo(self):
        self.caminho = []
        self.caminho.append(self.arestas[0][0])
        self.atual = self.caminho[0]
        for i in range(len(self.arestas)):
            if self.arestas[i][0] == self.atual:
                self.caminho.append(self.arestas[i][1])
                self.atual = self.arestas[i][1]
        self.cont = 0
        for i in range(self.V):
            if self.vertices[i] in self.caminho:
                self.cont += 1
        if self.cont >= self.V:
            return True
        return False

    def graf_euller(self):  # Verifica se existe percurso de Euller no grafo em lista
        self.cont = 0
        for i in range(0, len(self.vertices)):
            if (self.checar_grau(self.vertices[i]) % 2) == 1:
                self.cont += 1
        if self.cont == 0 or self.A == 0:
            print('\nO grafo possui percurso de Euller fechado!')
        elif self.cont == 2:
            print('\nO grafo possui percurso de Euller aberto!')
        else:
            print('\nO grafo não possui percurso de Euller!')

    def criar_dict(self):
        for i in range(len(self.grafo)):
            self.aux = []
            for j in range(1, len(self.grafo[i])):
                self.aux.append(self.grafo[i][j])
            self.adj[self.grafo[i][0]] = self.aux

    def dfs(self):
        for u in self.vertices:
            self.anterior[u] = None
            self.cor[u] = 'branco'
            self.d[u] = None
            self.f[u] = None
        for u in self.vertices:
            if self.cor[u] == 'branco':
                self.dfs_visit(u)
                self.comp_conexo += 1

    def dfs_visit(self, u):
        self.cor[u] = 'cinza'
        self.tempo += 1
        self.d[u] = self.tempo
        self.conexo[u] = self.comp_conexo
        for v in self.adj[u]:
            if self.cor[v] == 'branco':
                self.anterior[v] = u
                self.dfs_visit(v)
        self.cor[u] = 'preto'
        self.f[u] = self.tempo + 1
        self.tempo += 1

    def bfs(self, s):  # Obs: DFS corrigido!!!
        for u in self.vertices:
            self.anterior[u] = None
            self.cor[u] = 'branco'
            self.d[u] = 'infinity'
        self.cor[s] = 'cinza'
        self.d[s] = 0
        self.anterior[s] = None
        self.Q = []
        self.Q.append(s)
        while True:
            if len(self.Q) == 0:
                break
            u = self.Q[0]
            del self.Q[0]
            for v in self.adj[u]:
                if self.cor[v] == 'branco':
                    self.cor[v] = 'cinza'
                    self.d[v] = self.d[u] + 1
                    self.anterior[v] = u
                    self.Q.append(v)
            self.cor[u] = 'preto'

    def adicionar(self, a, b):
        for i in range(len(self.grafo)):
            if self.grafo[i][0] == a and (self.grafo.count(b) + 1) <= 2:
                if b not in self.grafo[i] or a == b:
                    self.grafo[i].append(b)

    def criar(self, a, b):
        self.edge = []
        self.edge.append(a)
        self.edge.append(b)
        self.grafo.append(self.edge)

    def checar_listas(self, a):
        for i in range(len(self.grafo)):
            if self.grafo[i][0] == a:
                return True
        return False

    def criar_arestas(self, a, b):
        self.edge = []
        self.edge.append(a)
        self.edge.append(b)
        self.arestas.append(self.edge)

    def adicionar_aresta(self):  # Adiciona aresta ao grafo em matriz
        while True:
            self.a = str(input('Informe o 1º vértice da aresta: '))
            if self.a not in self.vertices:
                print('\nEsse vértice não está cadastrado!')
                break
            self.b = str(input('Informe o 2º vértice da aresta: '))
            if self.b in self.vertices:
                if self.checar_listas(self.a) == True:
                    self.criar_arestas(self.a, self.b)
                    self.adicionar(self.a, self.b)
                    self.A += 1
                else:
                    self.criar_arestas(self.a, self.b)
                    self.criar(self.a, self.b)
                    self.A += 1
                if self.a != self.b and self.grafo_orientado == False:
                    if self.checar_listas(self.b) == True:
                        self.criar_arestas(self.b, self.a)
                        self.adicionar(self.b, self.a)
                    else:
                        self.criar_arestas(self.b, self.a)
                        self.criar(self.b, self.a)
                    self.A += 1
            else:
                print('\nEsse vértice não está cadastrado!')
            self.cad = int(input('\nDeseja continuar cadastrando?\n[1]Sim\n[2]Não\nOpção: '))
            if self.cad == 2:
                break

    def apresentar_grafo(self):  # Apresenta o grafo construído
        self.criar_dict()
        print('\nGRAFO EM LISTA DE ADJACÊNCIA:\n{}'.format(self.adj))
        print('\nArestas: {}\nVértices: {}'.format(self.A, self.V))
        print('\nA: {', end='')
        for aresta in self.arestas: print('{} '.format(aresta), end='')
        print('}', end='')
        print('\nV: {', end='')
        for vertice in self.vertices: print('{} '.format(vertice), end='')
        print('}', end='')
        print('\n\nConexo? ', self.grafo_conexo())
        print('\nGrafo orientado? ', self.grafo_orientado)

        self.dfs()

        print('\nDFS:\n')
        print('Cor: ', self.cor)
        print('Anterior: ', self.anterior)
        print('Tempo inicial: ', self.d)
        print('Tempo final: ', self.f)
        print('Tempo total: ', self.tempo)

        self.bfs(self.vertices[0])

        print('\nBFS:\n')
        print('Cor: ', self.cor)
        print('Anterior: ', self.anterior)
        print('Distância: ', self.d)

        print('\nComponentes: {}\n{}'.format(self.conexo, self.comp_conexo))
