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


Here's a step-by-step algorithm for Dijkstra's algorithm:

1. Initialize the distance array to store the shortest distance from the source vertex to all other vertices. Set the distance of the source vertex to 0 and all other distances to infinity.
2. Initialize a boolean array to keep track of vertices included in the shortest path tree (SPT). Set all values to false initially.
3. Repeat the following steps for V-1 times, where V is the number of vertices in the graph:
   a. Find the vertex with the minimum distance from the source vertex that is not yet included in the SPT. Let this vertex be u.
   b. Mark vertex u as visited by setting the corresponding value in the boolean array to true.
   c. Update the distance array for all adjacent vertices of u if the current distance plus the weight of the edge between u and the adjacent vertex is less than the previously recorded distance for the adjacent vertex.
4. After the loop, the distance array contains the shortest distances from the source vertex to all other vertices.
5. Print the distances from the source vertex to all other vertices.

This algorithm efficiently finds the shortest paths in a weighted graph from a given source vertex to all other vertices.