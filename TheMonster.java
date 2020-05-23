public class TheMonster
{
	public static void main (String[] args) throws java.lang.Exception
	{
	     Scanner sc=new Scanner(System.in);
	     long a,b,c,d,i,j;
	     a=sc.nextLong();
	     b=sc.nextLong();
	     c=sc.nextLong();
	     d=sc.nextLong();
	     if(c%2==0 && d%2==0 && b%2!=0 && a%2==0 )
	          System.out.println("-1");
	     else if(d%2!=0 && c%2==0 && a%2==0 && b%2==0)
	          System.out.println("-1");
	     else {
	     for(i=b;i<9999;i+=a)
	     {
	          for(j=d;j<=i;j+=c)
	          {
	               if(j==i)
	               {    System.out.println(j);
	                    break;}
	          }
	          if(j==i)
	          break;
	     }
	     if(i>=9999)
	        System.out.println("-1");
	     }
	}
}
