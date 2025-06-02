
import java.util.Arrays;

class Dp_solutions {

    public static final int INF = (int)1e9 + 9;

    public int coin_change (int sum , int[] coins) {

        int[] dp = new int[sum];

        Arrays.fill (dp , INF);

        dp[0] = 0;

        for (int coin : coins) {
            
            for (int s = 0; s <= sum - coin; s++) {
                dp[s + coin] = Math.min(dp[s] + 1, dp[s + coin]);
            }

        }

        return dp[sum];

    }

    public int maxWDynNonRec (int[][] G) {
        int n = G.length , m = G[0].length;
        int[][] H = new int[n][m];

        H[n-1][m-1] = G[n-1][m-1];

        for (int i = n-1; i >= 0; i--) {
            for (int j = m-1; j >= 0; j--) {
                if (i + j == n + m - 2) continue;
                H[i][j] = G[i][j] + Math.max(H[i+1][j] , H[i][j+1]);
            }
        }

        return H[0][0];

    }

    public int maxWGreedy (int[][] G) {
        int ret = G[0][0];
        int n = G.length , m = G[0].length;
        int x = 0 , y = 0;
        while (x + y < n+m-2) {
            if (x == n-1) {
                y++;
            }
            else if (y == m-1) {
                x++;

            }
            else if (G[x+1][y] > G[x][y+1]){
                x++;
            }
            else y++;
            ret += G[x][y];
        }

        return ret;
    }

} 




public class Td4 {
    
    public static void main (String[] args) {

        

    }

}
