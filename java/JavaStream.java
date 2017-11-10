import java.util.Arrays;

public class JavaStream {

    public static void main(String[] args){
        int[] myIntArray = {1,2,3,4,5};
        int sum = Arrays.stream(myIntArray).sum();
        System.out.println(sum);
    }
}
