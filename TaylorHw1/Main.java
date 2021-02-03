import java.util.Scanner;

public class Main {
    public static void main(String [] args) {
        Scanner scnr = new Scanner(System.in);
        int humanYears;
        String name;
        System.out.println("Enter a name: ");
        name = scnr.nextLine();
        System.out.printf("Hi my name is %s", name);
        
    }
}