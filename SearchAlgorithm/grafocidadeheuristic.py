"Implementing a 'grafo' data structure for the Artificial Intelligence class"
"Packages needed"
"matplotlib"
"networkx"
import networkx as nx
import matplotlib.pyplot as plt

#Package to work with graphics
class GrafoCidades:
    def __init__(self):
        self.grafo = nx.Graph();
        #Creates a grafo

    def inserir_cidades(self, cidade):
        self.grafo.add_node(cidade, distancia=float('inf'), pedagios=float('inf'));

    def cadastrar_rota(self, cidade_origem, cidade_destino, distancia, pedagios):
        self.grafo.add_edge(cidade_origem, cidade_destino, distancia=distancia, pedagios=pedagios)
        #Insert a node called cidade(city)

    def visualizar_grafo(self):
        nx.draw(self.grafo, with_labels=True, font_weight="bold")
        plt.show()

    def caminhamento_amplitude(self, cidade_inicial):
        try:
            caminho = list(nx.bfs_edges(self.grafo, source=cidade_inicial));
            return caminho;
        except nx.NetworkXError:
            return None;

    def caminhamento_profundidade(self, cidade_inicial):
        try:
            caminho = list(nx.dfs_edges(self.grafo, source=cidade_inicial));
            return caminho
        except nx.NetworkXError:
            return None

    def buscar_caminho(self, cidade_inicial, cidade_final):
        try:
            caminho = nx.shortest_path(self.grafo, source=cidade_inicial, target=cidade_final, weight='distancia')
            return caminho;
        except nx.NetworkXNoPath:
            return None;

    def buscar_caminho_heuristico(self, cidade_inicial, cidade_final):
        try:
            caminho = nx.astar_path(self.grafo, source=cidade_inicial, target=cidade_final, heuristic=self.heuristica)
            return caminho
        except nx.NetworkXNoPath:
            return None

    def heuristica(self, n, goal):
        distancia_objetivo = nx.shortest_path_length(self.grafo, source=n, target=goal, weight='distancia')
        pedagios_objetivo = nx.shortest_path_length(self.grafo, source=n, target=goal, weight='pedagios')
        return distancia_objetivo + pedagios_objetivo

def main():
        grafo_cidades = GrafoCidades()
        while True:
            print("1. Inserir cidade ")
            print("2. Codastrar rota ")
            print("3. Visualizar grafo ")
            print("4. Caminhamento em amplitude ")
            print("5. Caminhamento em profundidade ")
            print("6. Buscar caminho entre cidades ")
            print("7. Buscar caminha heuristico ")
            print("8. Sair")

            escolha = int(input("Escolha uma opcao: "))
            if escolha == 1:
                cidade = input("Digite o nome da cidade: ")
                grafo_cidades.inserir_cidades(cidade);

            elif escolha == 2:
                cidade_origem = input("Digite a cidade de origem: ");
                cidade_destino = input("Digite a cidade de destino: ");
                distancia = float(input("Digite a distancia em km: "))
                pedagios = int(input("Digite o numero de pedagios"))
                grafo_cidades.cadastrar_rota(cidade_origem, cidade_destino, distancia, pedagios);

            elif escolha == 3:
                grafo_cidades.visualizar_grafo()

            elif escolha == 4:
                cidade_inicial = input("Digite a cidade inicial para o caminhamento em amplitude: ");
                resultado = grafo_cidades.caminhamento_amplitude(cidade_inicial);
                print('Caminhamento em Amplitude: ',resultado);

            elif escolha == 5:
                cidade_inicial = input("Digite a cidade inicia para caminhamento em profundidade: ");
                resultado = grafo_cidades.caminhamento_profundidade(cidade_inicial);
                print("Caminhamento em Profundidade: ",resultado);

            elif escolha == 6:
                cidade_inicial = input("Digite a cidade inicial: ");
                cidade_final = input("Digite a cidade final: ");
                resultado = grafo_cidades.buscar_caminho(cidade_inicial, cidade_final);

                if resultado:
                    print("Caminho encontrado: ",resultado);
                else:
                    print("Não existe caminho entre as cidades.")

            elif escolha == 7:
                cidade_inicial = input("Digite a cidade inicial: ")
                cidade_final = input("Digite a cidade final: ")
                resultado = grafo_cidades.buscar_caminho_heuristico(cidade_inicial,cidade_final)
                if resultado:
                    print("Caminho heuristico encontrado: ", resultado)
                else:
                    print("Não existe caminho heuristico entre as cidades.")

            elif escolha == 8:
                print("Programa Encerrado.");
                break;
            else:
                print("Opcao Invalida.");
if __name__ == "__main__":
    main();