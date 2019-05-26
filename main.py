import grafo_lista
import grafo_matriz

grafo_orientado = False

while True:
  print('___________________________')
  op = int(input('[1] Lista\n[2] Matriz\nOpção: '))
  print('\n___________________________')
  if op == 1:
    grafo = grafo_lista.grafo_lista(6, grafo_orientado)
    break
  elif op == 2:
    grafo = grafo_matriz.grafo_matriz(6, grafo_orientado)
    break
  else:
    print('\nOpção inválida!\n')
while True:
  print('\n___________________________')
  print('\n[1] CADASTRAR ARESTA\n[2] IMPRIMIR GRAFO\n[3] VERIFICAR GRAU DE VÉRTICE\n[4] VERIFICAR MAIOR GRAU\n[5] VERIFICAR LAÇOS\n[6] VERIFICAR PERCURSO DE EULLER\n[7] SAIR')
  op = int(input('\nInforme sua opção: '))
  print('\n___________________________')
  if op == 1:
    grafo.adicionar_aresta()
  elif op == 2:
    grafo.apresentar_grafo()
  elif op == 3:
    v = int(input('Informe o o vértice que deseja checar: '))
    if v in grafo.vertices:
      print('\nGrau do vértice {} é {}'.format(v,grafo.checar_grau(v)))
    else:
      print('\nVértice inválido!')
  elif op == 4:
    grafo.max_grau()
  elif op == 5:
    print('\nO grafo possui {} laços.'.format(grafo.num_lacos()))
  elif op == 6:
    grafo.graf_euller()
  elif op == 7:
    grafo.dfs()
    print('\nSaindo...')
    break