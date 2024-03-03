import java.util.*;

class BellmanFord {
    private int V;
    private int[][] weightMatrix;

    BellmanFord(int v) {
        V = v;
        weightMatrix = new int[V][V];
    }

    void addEdge(int source, int destination, int weight) {
        weightMatrix[source][destination] = weight;
    }

    void bellmanFord(int source) {
        int[] distance = new int[V];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[source] = 0;

        for (int i = 0; i < V - 1; ++i) {
            for (int u = 0; u < V; ++u) {
                for (int v = 0; v < V; ++v) {
                    if (weightMatrix[u][v] != 0 && distance[u] != Integer.MAX_VALUE && distance[u] + weightMatrix[u][v] < distance[v]) {
                        distance[v] = distance[u] + weightMatrix[u][v];
                    }
                }
            }
        }

        for (int u = 0; u < V; ++u) {
            for (int v = 0; v < V; ++v) {
                if (weightMatrix[u][v] != 0 && distance[u] != Integer.MAX_VALUE && distance[u] + weightMatrix[u][v] < distance[v]) {
                    System.out.println("Graph contains negative weight cycle");
                    return;
                }
            }
        }

        printSolution(distance);
    }

    private void printSolution(int[] distance) {
        System.out.println("Vertex \t Distance from Source");
        for (int i = 0; i < V; ++i)
            System.out.println(i + "\t\t" + distance[i]);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of nodes: ");
        int V = scanner.nextInt();

        BellmanFord graph = new BellmanFord(V);

        System.out.println("Enter the weight matrix (enter 0 for no edge):");
        for (int i = 0; i < V; ++i) {
            for (int j = 0; j < V; ++j) {
                graph.weightMatrix[i][j] = scanner.nextInt();
            }
        }

        System.out.print("Enter the source vertex: ");
        int source = scanner.nextInt();

        graph.bellmanFord(source);

        scanner.close();
    }
}
