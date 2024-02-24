import java.util.*;

public class RecursiveDescentParsing {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Dictionary<String, List<String>> grammar = new Hashtable<String, List<String>>();

        System.out.print("Enter the number of grammar: ");
        int n = scanner.nextInt();
        System.out.print("Enter an input string: ");
        String s = scanner.next();

        for (int i = 0; i < n; i++) {
            String key = scanner.next();
            String temp = scanner.next();
            String[] words = temp.split("|");
            List<String> list = new ArrayList<String>();
            for (String word : words) {
                list.add(word);
            }
            grammar.put(key, list);
        }

        parse(s, grammar);
    }

    private static boolean parse(String s, Dictionary<String, List<String>> grammar, String iterator, int index) {
        if (iterator == null) {
            iterator = "S";
        }

        return false;
    }
    private static boolean isNonTerminal(String symbol) {
        return symbol.length() == 1 && Character.isUpperCase(symbol.charAt(0));
    }
}
