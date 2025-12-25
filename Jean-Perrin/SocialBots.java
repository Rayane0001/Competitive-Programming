import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class SocialBots {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        int botCount = 0;
        Pattern botPattern = Pattern.compile("\\d{5,}$");
        for (int i = 0; i < N; i++) {
            String account = scanner.nextLine().trim();
            Matcher matcher = botPattern.matcher(account);
            if (matcher.find()) {
                botCount++;
            }
        }
        System.out.println(botCount);
        scanner.close();
    }
}
