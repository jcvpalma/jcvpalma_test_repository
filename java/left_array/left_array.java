import java.util.*;

public class left_array {
    

    public static void main(String[] args){

        int[] vector = new int[]{ 1, 2, 3, 4, 5 };
        int d = 4;

        //print original
        for(int k=0;k<vector.length;k++){
            System.out.print(vector[k]);
        }
        System.out.println(" ------- ");

        //System.out.println("Antes: "+ vector);
        for(int i=0;i<d;i++){
            vector = shiftArrayToLeft(vector);
            for(int k=0;k<vector.length;k++){
                System.out.print(vector[k]);
            }
            System.out.println(" ");
        }

    }

    public static int[] shiftArrayToLeft(int[] a){
        int firstEl = 0;

        //save the first
        firstEl = a[0];
        
        //shift the rest of elements
        for(int i =0;i<a.length;i++){
            //shift values
            if ((i+1) < (a.length)){
                a[i] = a[i+1];
                //System.out.print("pos" + i +":"+ a[i] + " - pos2:"+ (i+1) + ":"+ a[i+1] + " S: "+ a.length);
            }
            //System.out.println(" ");
        }
        a[a.length-1]=firstEl;

        return a;
    }

}