import java.util.*;

class Dijkstra {
    private int V;
    private int[][] weightMatrix;

    Dijkstra(int v) {
        V = v;
        weightMatrix = new int[V][V];
    }

    void addEdge(int source, int destination, int weight) {
        weightMatrix[source][destination] = weight;
    }

    void dijkstra(int source) {
        int[] distance = new int[V];
        boolean[] shortestPathTreeSet = new boolean[V];

        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[source] = 0;

        for (int count = 0; count < V - 1; count++) {
            int u = minDistance(distance, shortestPathTreeSet);
            shortestPathTreeSet[u] = true;

            for (int v = 0; v < V; v++) {
                if (!shortestPathTreeSet[v] && weightMatrix[u][v] != 0 && distance[u] != Integer.MAX_VALUE
                        && distance[u] + weightMatrix[u][v] < distance[v]) {
                    distance[v] = distance[u] + weightMatrix[u][v];
                }
            }
        }

        printSolution(distance);
    }

    private int minDistance(int[] distance, boolean[] shortestPathTreeSet) {
        int min = Integer.MAX_VALUE, minIndex = -1;

        for (int v = 0; v < V; v++) {
            if (!shortestPathTreeSet[v] && distance[v] <= min) {
                min = distance[v];
                minIndex = v;
            }
        }

        return minIndex;
    }

    private void printSolution(int[] distance) {
        System.out.println("Vertex \t Distance from Source");
        for (int i = 0; i < V; i++)
            System.out.println(i + "\t\t" + distance[i]);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of nodes: ");
        int V = scanner.nextInt();

        Dijkstra graph = new Dijkstra(V);

        System.out.println("Enter the weight matrix (enter 0 for no edge):");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph.weightMatrix[i][j] = scanner.nextInt();
            }
        }

        System.out.print("Enter the source vertex: ");
        int source = scanner.nextInt();

        graph.dijkstra(source);

        scanner.close();
    }
}
