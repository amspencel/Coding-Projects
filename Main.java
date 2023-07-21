import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ToyISAConverter ISA = new ToyISAConverter(input.nextLine());
        System.out.println(ISA.convert());

    }
}
