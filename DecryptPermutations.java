 import java.util.*;

public class DecryptPermutations {

 
    public static List<String> generatePermutations(String str) {
        List<String> permutations = new ArrayList<>();
        permute("", str, permutations);
        return permutations;
    }

    private static void permute(String prefix, String str, List<String> permutations) {
        int n = str.length();
        if (n == 0) {
            permutations.add(prefix);
        } else {
            for (int i = 0; i < n; i++) {
                permute(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n), permutations);
            }
        }
    }


    public static String decrypt(String ciphertext, String perm) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        Map<Character, Character> decryptMap = new HashMap<>();

        for (int i = 0; i < alphabet.length(); i++) {
            decryptMap.put(alphabet.charAt(i), perm.charAt(i));
        }

        StringBuilder decryptedText = new StringBuilder();

        for (char c : ciphertext.toCharArray()) {
            char lowerChar = Character.toLowerCase(c);
            if (decryptMap.containsKey(lowerChar)) {
                char decryptedChar = decryptMap.get(lowerChar);
                decryptedText.append(Character.isUpperCase(c) ? Character.toUpperCase(decryptedChar) : decryptedChar);
            } else {
                decryptedText.append(c);
            }
        }

        return decryptedText.toString();
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the encrypted message: ");
            String ciphertext = scanner.nextLine();
            
            String alphabet = "abcdefghijklmnopqrstuvwxyz";
            List<String> permutations = generatePermutations(alphabet);
            
            int permutationCount = 0;
            for (String perm : permutations) {
                permutationCount++;
                String decryptedText = decrypt(ciphertext, perm);
                System.out.println("Permutation #" + permutationCount + ": " + decryptedText);
            }
        }
    }
}
