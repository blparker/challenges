import java.util.*;

class Challenge184 {
  static class Node {
    public int val;
    public Node next;
    public Node prev;

    public Node(int val) {
      this.val = val;
    }

    public String toString() {
      return "Val: " + val;
    }
  }

  static class LList {
    private Node stackHead;
    private int size;
    private Node root;

    public void push(int num) {
      ++size;

      if (stackHead == null) {
        stackHead = new Node(num);
        root = new Node(num);
        return;
      }

      Node n = new Node(num);
      n.next = stackHead;
      stackHead.prev = n;
      stackHead = n;

      insert(num);
    }

    public int pop() {
      if (stackHead == null) return -1;
      --size;

      int val = stackHead.val;
      stackHead.next.prev = null;
      stackHead = stackHead.next;

      return val;
    }

    private void insert(int num) {
      Node n = root;
      Node p = null;

      while (n != null) {
        if (num > n.val) {
          p = n;
          n = n.next;
        } else if (num < n.val) {
          p = n;
          n = n.prev;
        }
      }

      if (num > p.val) {
        p.next = new Node(num);
      } else if (num < p.val) {
        p.prev = new Node(num);
      }
    }

    private void delete(int num) {
      traverseDelete(root, null, num);
    }

    private void replaceInParent(Node n, Node p, int num) {
      if (n.val > p.val) {
        p.next = null
      } else if (n.val < p.val) {
        p.prev = null;
      }
    }

    private void traverseDelete(Node n, Node p, int num) {
      if (n == null) return;

      if (num < n.prev) {
        traverseDelete(n.prev, n, num);
      } else if (num > n.next) {
        traverseDelete(n.next, n, num);
      } else {  // Do the delete here
        if (n.prev != null && n.next != null) { // Both children present

        } else if (n.prev != null) {            // Replace me with left child
          if (n.val > p.val) {
            p.next = n.prev;
            n.prev = null;
          } else if (n.val < p.val) {
            p.prev = n.prev;
            n.prev = null;
          }
        } else if (n.next != null) {            // Replace me with right child
          if (n.val > p.val) {
            p.next = n.next;
            n.next = null;
          } else if (n.val < p.val) {
            p.prev = n.next;
            n.next = null;
          }
        } else {                                // No children
          if (n.val > p.val) {
            p.next = null
          } else if (n.val < p.val) {
            p.prev = null;
          }
        }
      }
    }

    public void displayStack() {
      Node n = stackHead;
      while (n != null) {
        System.out.println(n.val);
        n = n.next;
      }
    }

    public void displayOrdered() {
      traverse(root);
    }

    private void traverse(Node n) {
      if (n == null) return;

      traverse(n.prev);
      System.out.println(n.val);
      traverse(n.next);
    }

    public int size() {
      return size;
    }
  }

  public static void main(String[] args) {
    LList l = new LList();
    l.push(4);
    l.push(1);
    l.push(9);
    l.push(3);

    l.displayStack();
    System.out.println("######");
    l.pop();
    l.displayStack();
    //l.displayOrdered();
    //System.out.println(l.size());
  }
}
