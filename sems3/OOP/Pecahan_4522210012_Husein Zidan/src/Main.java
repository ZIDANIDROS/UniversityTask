import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("masukan pecahan ke-satu (pembilang/penyebut): ");
        int pembilang1 = input.nextInt();
        int penyebut1 = input.nextInt();
        Pecahan fraction1 = new Pecahan(pembilang1, penyebut1);

        System.out.print("masukan pecahan ke-dua (numerator/denominator): ");
        int num2 = input.nextInt();
        int den2 = input.nextInt();
        Pecahan fraction2 = new Pecahan(num2, den2);

        System.out.println("1. Add");
        System.out.println("2. Subtract");
        System.out.println("3. Multiply");
        System.out.println("4. Divide");
        System.out.print("Enter your choice: ");
        int choice = input.nextInt();

        Pecahan result;
        switch (choice) {
            case 1:
                result = fraction1.add(fraction2);
                break;
            case 2:
                result = fraction1.subtract(fraction2);
                break;
            case 3:
                result = fraction1.multiply(fraction2);
                break;
            case 4:
                result = fraction1.divide(fraction2);
                break;
            default:
                System.out.println("Invalid choice.");
                return;
        }

        System.out.println("Result: " + result);
    }
}