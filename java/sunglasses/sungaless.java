import java.util.Arrays;
import java.util.*;

public class sungaless {


    public static void main(String[] args){

        int[][] sunglasses = new int[5][5];
        sunglasses = fillSunGlasses();

        int iStart=0, iFinish=0, jStart = 0, jFinish = 0;
        List<Integer> tot = new ArrayList<Integer>();

        for(int i=0;i<sunglasses.length;i++){
            for(int j=0;j<sunglasses[i].length;j++){

                iStart = i;
                iFinish = i+(sunglasses.length/2);
                jStart = j;
                jFinish = j+(sunglasses[i].length/2);

                if(iFinish<7){
                    if(jFinish<7){
                        //System.out.println(String.format("%s, %s, %s, %s", iStart, iFinish, jStart, jFinish));
                        int totalMax = extractSunglasses(iStart, iFinish, jStart, jFinish, sunglasses);
                        tot.add(totalMax);
                    }
                }
            }
        }
        System.out.println("Maximo: " + Collections.max(tot));
        
    }

    public static int extractSunglasses(int iStart, int iFinish, int jStart, int jFinish, int[][] sunglasse){
        int total = 0;
        List<List<Integer>> v = new ArrayList<List<Integer>>();

        //First I construct an array of Integers where I know their positions
        for(int i=iStart;i<iFinish;i++){
            List<Integer> t = new ArrayList<Integer>();
            for(int j=jStart;j<jFinish;j++){
                t.add(sunglasse[i][j]);
            }
            v.add(t);
        }

        //After I read and set to 0 the indices in the 2nd row tro avoid extra number in my result
        for(int i=0;i<v.size();i++){
            for(int j=0;j<v.get(i).size();j++){
                if (i == 1){
                    if(j == 0){
                        v.get(i).set(j, 0);
                    }
                    if(j == 2){
                        v.get(i).set(j, 0);
                    }
                }
                System.out.print(v.get(i).get(j) + "\t");
                total += v.get(i).get(j);
            }
            System.out.println("\r");
        }
        System.out.println(String.format("Total: %s\n", total));
        return total;
        //for (List<Integer> is : v) {
         //   for(Integer x : is){
          //      System.out.print("Indice: " + x.hashCode() + " = " + x + "\t");
         //   }
         //   System.out.println("\r");
        //}
        //System.out.println("Total: \n");

    }


    public static int[][] fillSunGlasses(){
        int[][] sunglasses = new int[5][5];

        sunglasses = new int[][]{{-9, -9, -9,1,1,1}, 
                                {0,-9,0,4,3,2},
                                {-9,-9,-9,1,2,3},
                                {0,0,8, 6, 6, 0},
                                {0,0,0,-2,0,0}, 
                                {0,0,1,2,4,0}};

        return sunglasses;
    }


}