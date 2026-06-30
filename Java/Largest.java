import java.util.Arrays;

class solution {
    public static int largest(int[] arr) {
        Arrays.sort(arr);
        return arr[arr.length - 1];
    }
}

public class Largest {
    public static void main(String[] args) {
        int[] arr = { 2, 5, 1, 3, 0 };
        System.out.println("The largest element is :" + solution.largest(arr));
    }

}