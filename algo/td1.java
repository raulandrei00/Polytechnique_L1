// import javax.swing.plaf.synth.SynthStyle;
// import java.security.cert.CollectionCertStoreParameters;

import java.util.*;

public class td1 {

    public static void main (String[] args)
    {
        //System.out.println("hello there");
        // List<Integer> l = Arrays.asList(2 , 4 , 5 , 7 , 19);
        // System.out.println(binarySearch(l , 2));
        // List<Integer> rez = Arrays.asList(243 , 5 , 2 , -1 , 9 , 1010, 66 , 2735);
        // quicksort(rez , 0 , 7);
        // for (int x : rez) {
        //     System.out.print(x + " ");
        // }

        // System.out.println( prime_check_brute(45) );
        System.out.println( pi(23462346) ); // ca va

    }

    public static int pi (int n) {

        List<Boolean> sieve = new ArrayList<Boolean>(Arrays.asList(false,false));
        
        for (int i = 2; i <= n; i++) 
        {
            sieve.add(false);
        }

        int rez = 0;

        for (int i = 2; i <= n; i++) 
        {
            if (sieve.get(i) == false){
                rez++;
                for (int k = 2*i; k <= n; k += i) {
                    sieve.set(k , true);
                }
            }
        }

        return rez;
    }


    public static List<Integer> merge (List<Integer> l1 , List<Integer> l2) {

        int index_l1 = 0 , index_l2 = 0;

        List<Integer> l = new ArrayList<Integer>();

        while (index_l1 < l1.size() || index_l2 < l2.size())
        {
            if (index_l1 == l1.size()) {
                l.add(l2.get(index_l2));
                index_l2++;
            }
            else if (index_l2 == l2.size()) {
                l.add(l1.get(index_l1));
                index_l1++;
            }
            else if (l1.get(index_l1) < l2.get(index_l2)) {
                l.add(l1.get(index_l1));
                index_l1++;
            }
            else {
                l.add(l2.get(index_l2));
                index_l2++;
            }
        }

        return l;
    }

    public static int lomuto (List<Integer> l , int b , int e) {

        int p = b;

        for (int i = b; i < e; i++) {

            if (l.get(i) < l.get(e)) {
                Collections.swap(l , i , p);
                p++;
            }

        }

        Collections.swap(l , e , p);

        return p;

    }

    public static int hoare_partitioning_scheme (List<Integer> l , int b , int e) {

        int piv = l.get((b + e) / 2) , i = b , j = e;

        while (i < j) {
            if (l.get(i) >= piv && piv >= l.get(j)) {
                Collections.swap(l , i , j);
                i++; j++;
            }
            while (l.get(i) < piv) i++;
            while (l.get(j) > piv) j--;
        }

        int p = j;
        return p;
    }

    public static void quicksort (List<Integer> l , int left , int right) {
        // System.out.println(left + " " + right);
        // try {
        //     Thread.sleep(1000);
        // } catch (InterruptedException e) {
        //     Thread.currentThread().interrupt();
        // }
        if (left >= right) return;
        int pivot = hoare_partitioning_scheme(l, left , right);
        quicksort(l, left, pivot-1);
        quicksort(l, pivot+1, right);
        
    }

    public static List<Integer> merge_sort (List<Integer> l) {
        List<Integer> l_sorted = new ArrayList<Integer>();

        if (l.size() < 2) {
            return l;
        }

        List<Integer> l1 = new ArrayList<Integer>(), l2 = new ArrayList<Integer>();
        
        int mid = l.size() / 2;
        for (int i = 0; i < mid; i++) {
            l1.add(l.get(i));
        }
        for (int i = mid; i < l.size(); i++) {
            l2.add(l.get(i));
        }

        l1 = merge_sort(l1);
        l2 = merge_sort(l2);

        
        l_sorted = merge(l1 , l2);
        

        return l_sorted;
    }

    public static void counting_sort () {}

    public static boolean prime_check_brute (int n) {

        for (int d = 2; d * d <= n; d++) {
            if (n % d == 0) return false;
        }

        return true;
    }


    public static Integer binarySearch (List<Integer> l , int a)
    {
        
        int left = 0 , right = l.size()-1 , mid = -1;

        while (left != right) {

            mid = (left + right) / 2;

            if (l.get(mid) < a) {
                left = mid+1;
            }
            else if (l.get(mid) == a) {
                return mid;
            }
            else {
                right = mid;
            }

        }

        if (l.get(left) == a) return left;

        return -1;
    }

}