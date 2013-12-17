import java.io.Console;

public class Challenge144 {
  public static void main(String[] args) {
    int n = Integer.parseInt(System.console().readLine());
    String[] o = read(n, new String[n]);
    String[] n = read(n, new String[n]);
    
  }

  public static String[] read(int n, String[] lines) {
    if (n == 0) return lines;
    lines[n - 1] = System.console().readLine();
    return read(n - 1, lines);
  }
}
