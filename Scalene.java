import java.util.*;

public class Scalene {
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int a = sc.nextInt();
      int b = sc.nextInt();
      int c = sc.nextInt();
      
      if((a<=100000) && (b<=100000) && (c<=100000)) {
        if((a!=b) && (b!=c) && (c!=a)) {
          System.out.println("yes");
        }
        else {
          System.out.println("no");
        }
      }
    }
}