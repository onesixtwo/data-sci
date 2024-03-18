import java.util.Scanner;
import java.util.InputMismatchException;

public class AgeClassifier {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt the user to enter their age
            System.out.print("Enter your age: ");

            // Read the age as an integer
            int age = scanner.nextInt();

            // Determine the age group
            String ageGroup = classifyAge(age);

            // Display the result
            System.out.println("You belong to the age group: " + ageGroup);
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid integer for age.");
        } finally {
            // Close the scanner to prevent resource leak
            scanner.close();
        }
    }

    // Function to classify age into groups
    private static String classifyAge(int age) {
        if (age >= 0 && age <= 11) {
            return "Child";
        } else if (age >= 12 && age <= 17) {
            return "Teen";
        } else if (age >= 18 && age <= 64) {
            return "Adult";
        } else {
            return "Invalid age"; // Handle cases outside the specified age groups
        }
    }
}