import java.util.Arrays;
import java.util.Scanner;
public class NastyaAndRice
{
    public static void main(String args[]) {
        Scanner sc= new Scanner(System.in);
        int t= sc.nextInt();
        int a[][]= new int[t][5];
        for(int i=0;i<t;i++)
        {
            for(int j=0;j<5;j++)
            {
                a[i][j]= sc.nextInt();
            }
        }
        for(int i=0;i<t;i++)
        {
            //for(int j=0;j<5;j++)
            
                int num1= a[i][0]*(a[i][1]+a[i][2]);
                int num2= a[i][0]*(a[i][1]-a[i][2]);
                int c = a[i][3]-a[i][4];
                int d = a[i][3]+a[i][4];
                if((num1>=c && num1<=d) || (num2>=c && num2<=d) || (num2<c && num1>d))
                {
                    System.out.println("YES");
                }
                else{
                    System.out.println("NO");
                }
            
        }
        
    }
}