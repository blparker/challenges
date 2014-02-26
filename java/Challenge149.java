import java.util.Scanner;

/*
  Execute by:
  echo "all those who believe in psychokinesis raise my hand" | java Challenge149
*/

class Challenge149 {
  public static void main(String[] args) {
    StringBuffer consts = new StringBuffer();
    StringBuffer vowels = new StringBuffer();

    for (char c : new Scanner(System.in).nextLine().toCharArray()) {
      if (isVowel(c)) {
        vowels.append(c);
      } else {
        consts.append(c);
      }
    }

    System.out.printf("%s\n%s\n", consts.toString(), vowels.toString());
  }

  private static boolean isVowel(char c) {
    return "aeiou ".contains(String.valueOf(c));
  }
}
