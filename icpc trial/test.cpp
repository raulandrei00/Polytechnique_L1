#include<iostream>
#include<vector>

using namespace std;
const int NMAX = 1e5;
vector<int> adj[NMAX+1];
int c[NMAX+1];

int main ()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t; cin >> t;
    while (t--)
    {
        int n; cin >> n;
        for (int i = 1; i < n; i++)
        {
            int x, y; cin >> x >> y;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }
        for (int i = 1; i <= n; i++)
        {
            char x; cin >> x;
            if (x == '0') c[i] = 0;
            else if (x == '1') c[i] = 1;
            else c[i] = 2;
        }

        int ans = 0;
        if (c[1] != 2) {
            int unsure = 0;
            for (int i = 2; i <= n; i++)
            {
                if (adj[i].size() == 1 && c[i] != 2 && c[i] != c[1])
                {
                    ans++;
                }
                else if (adj[i].size() == 1 && c[i] == 2) unsure++;
            }
            ans += (unsure+1) / 2;
        }
        else {
            int o = 0 , z = 0;
            int unsure = 0;
            int useless = 0;
            for (int i = 2; i <= n; i++)
            {
                {
                    if (c[i] == 2) unsure++;
                    else if (c[i] == 1) o++;
                    else z++;
                }
                else if (c[i] == 2) useless++;
            }
            if (o != z)
                ans = max(o , z) + unsure / 2;
            else {
                ans = z + (unsure + useless % 2) / 2;
            }
        }

        cout << ans << '\n';

        for (int i = 1; i <= n; i++)
        {
            adj[i].clear();
        }
    }
}