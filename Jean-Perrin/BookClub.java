import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class BookClub {
    private static ArrayList<ArrayList<Integer>> graph;
    private static ArrayList<ArrayList<Integer>> reverseGraph;
    private static boolean[] visited;
    private static Stack<Integer> stack;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        graph = new ArrayList<>();
        reverseGraph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
            reverseGraph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            graph.get(a).add(b);
            reverseGraph.get(b).add(a);
        }

        visited = new boolean[n];
        stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs1(i);
            }
        }

        visited = new boolean[n];
        int sccCount = 0;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (!visited[node]) {
                dfs2(node);
                sccCount++;
            }
        }

        System.out.println(sccCount == 1 ? "YES" : "NO");
        scanner.close();
    }

    private static void dfs1(int node) {
        visited[node] = true;
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                dfs1(neighbor);
            }
        }
        stack.push(node);
    }

    private static void dfs2(int node) {
        visited[node] = true;
        for (int neighbor : reverseGraph.get(node)) {
            if (!visited[neighbor]) {
                dfs2(neighbor);
            }
        }
    }
}
