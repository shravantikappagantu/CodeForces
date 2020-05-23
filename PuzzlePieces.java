import java.util.Arrays;
import java.util.Scanner;
public class PuzzlePieces
{
    public static void main(String [] args) 
    {
        Scanner sc= new Scanner(System.in);
        int t= sc.nextInt();
        int a[][]= new int[t][5];
        for(int i=0;i<t;i++)
        {
            for(int j=0;j<2;j++)
            {
                a[i][j]= sc.nextInt();
            }
        }
        for(int i=0;i<t;i++)
        {
            if(a[i][0]==1 || a[i][1]==1)
                System.out.println("YES");
            else if(a[i][0]<=2 && a[i][1]<=2)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
}