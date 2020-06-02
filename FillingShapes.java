import java.util.Scanner;
public class FillingShapes 
{
    public static void main(String [] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n % 2 != 0){
            System.out.print(0);
        }
        else{
            System.out.print((int)Math.pow(2,n/2));
        }
    }
    
}