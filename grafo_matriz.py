import numpy as np


class grafo_matriz:
    def __init__(self, V, grafo_orientado):  # Construtor dos atributos básicos
        self.grafo = []  # Lista das arestas e vértices cadastrados
        self.vertices = []  # Lista dos vértices cadastrados
        self.arestas = []
        self.V = V  # Quantidade de vértices
        self.A = 0  # Contador de arestas
        self.criar_vertices(V)  # Cria os vértices do grafo
        self.matriz = np.zeros((V, V), dtype=int)  # Armazena as arestas do grafo em matriz
        self.grafo_orientado = grafo_orientado
        self.adj = {}
        self.anterior = {}
        self.f = {}
        self.cor = {}
        self.d = {}
        self.tempo = 0

    def criar_vertices(self, V):  # Cadastra os vértices
        for i in range(0, V):
            vertice = str(input('Informe um vértice: '))
            self.vertices.append(vertice)
        print('\nVértices: ', end='')
        for i in range(0, len(self.vertices)): print('{} '.format(self.vertices[i]), end='')
        print('')

    def checar_grau(self, v):  # Checa o grau do grafo em matriz
        self.grau = 0
        for i in range(0, len(self.vertices)):  # Encontra o índice referente ao vértice a ser checado
            if self.vertices[i] == v:
                self.indice = i
        for j in range(0, len(self.vertices)):
            if self.matriz[self.indice][j] == 1:
                self.grau += 1
        return self.grau

    def max_grau(self):  # Verifica qual vértice têm o maior grau no grafo em matriz
        self.graus = []
        for i in range(0, len(self.vertices)):
            self.vert = []
            self.vert.append(self.checar_grau(self.vertices[i]))
            self.vert.append(self.vertices[i])
            self.graus.append(self.vert)
        self.graus.sort(reverse=True)
        print('\nO vértice {} com grau {} é o maior.'.format(self.graus[0][1], self.graus[0][0]))

    def num_lacos(self):  # Verifica o número de laços no grafo em matriz
        self.laco = 0
        for i in range(0, len(self.vertices)):
            for j in range(0, len(self.vertices)):
                if i == j and self.matriz[i][j] == 1:
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

    def graf_euller(self):  # Verifica se existe percurso de Euller no grafo em matriz
        self.cont = 0
        for i in range(0, self.V):
            if (self.checar_grau_matriz(self.vertices[i]) % 2) == 1:
                self.cont += 1
        if self.cont == 0 or self.A_matriz == 0:
            print('\nO grafo possui percurso de Euller fechado!')
        elif self.cont == 2:
            print('\nO grafo possui percurso de Euller aberto!')
        else:
            print('\nO grafo não possui percurso de Euller!')

    def checar_indices(self, a, b):  # Checa o índice para adicionar aresta em  matriz
        self.indices = []
        for i in range(len(self.vertices)):
            if self.vertices[i] == a:
                self.indices.append(i)
        for i in range(len(self.vertices)):
            if self.vertices[i] == b:
                self.indices.append(i)
        return self.indices

    def criar_dict(self):
        for i in range(self.V):
            self.aux = []
            for j in range(self.V):
                if self.matriz[i, j] == 1:
                    self.aux.append(self.vertices[j])
            self.adj[self.vertices[i]] = self.aux

    def adicionar_aresta(self):  # Adiciona aresta ao grafo em matriz
        while True:
            self.a = str(input('Informe o 1º vértice da aresta: '))
            if self.a not in self.vertices:
                print('\nEsse vértice não está cadastrado!')
                break
            self.b = str(input('Informe o 2º vértice da aresta: '))
            if self.b in self.vertices:
                self.aresta = []
                self.indices = self.checar_indices(self.a, self.b)
                self.matriz[self.indices[0]][self.indices[1]] = 1
                self.aresta.append(self.a)
                self.aresta.append(self.b)
                self.arestas.append(self.aresta)
                self.A += 1
                if self.a != self.b and self.grafo_orientado == False:
                    self.aresta = []
                    self.indices = self.checar_indices(self.b, self.a)
                    self.matriz[self.indices[0]][self.indices[1]] = 1
                    self.aresta.append(self.b)
                    self.aresta.append(self.a)
                    self.arestas.append(self.aresta)
                    self.A += 1
            else:
                print('\nEsse vértice não está cadastrado!')
            self.cad = int(input('\nDeseja continuar cadastrando?\n[1]Sim\n[2]Não\nOpção: '))
            if self.cad == 2:
                break

    def dfs(self):
        for u in self.vertices:
            self.anterior[u] = None
            self.cor[u] = 'branco'
            self.d[u] = None
            self.f[u] = None
        for u in self.vertices:
            if self.cor[u] == 'branco':
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.cor[u] = 'cinza'
        self.tempo += 1
        self.d[u] = self.tempo
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

    def apresentar_grafo(self):  # Apresenta o grafo construído
        self.criar_dict()
        print('\nGRAFO EM MATRIZ DE ADJACÊNCIA:')
        print('\t', end='')
        for i in range(self.V): print('\t{}'.format(self.vertices[i]), end='')
        print('')
        for i in range(self.V):
            print('\n', self.vertices[i], '\t[', end='')
            for j in range(self.V):
                print('\t{}'.format(self.matriz[i][j]), end='')
            print('\t]', end='')
        print('\n\nArestas: {}\nVértices: {}'.format(self.A, self.V))
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