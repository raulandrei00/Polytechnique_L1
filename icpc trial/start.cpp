#include <iostream>
#include <vector>
#include <queue>
#include<bits/stdc++.h>

using namespace std;
using ll = long long;
const int N = 1003;

const ll oo = 1e18;
int n, m;
vector<pair<int, int>> vs[N+1];
ll dist[N+1][N+1];

ll dp[N+1];

int u[N+1] , t[N+1];
int s[N+1];

void dijkstra(int u0) {
    for (int i = 1; i <= n; i++)
    {
        dist[u0][i] = oo;
    }
    dist[u0][u0] = 0;
	priority_queue<pair<ll, int>  , vector<pair<ll , int> > , greater<pair<ll , int> > > q;
	q.emplace(0, u0);
	while (!q.empty()) {
		auto [d , nod] = q.top();
        q.pop();
        if (d > dist[u0][nod]) continue;
        for (auto [to , c] : vs[nod])
        {
            if (dist[u0][nod] + c < dist[u0][to])
            {
                dist[u0][to] = dist[u0][nod] + c;
                q.push({dist[u0][to] , to});
            }
        }
	}
}

int main() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++)
    {
        int x, y , w; cin >> x >> y >> w;
        vs[x].push_back({y , w});
        vs[y].push_back({x , w});
    }

    for (int i = 1; i <= n; i++)
    {
        dijkstra(i);
    }


    int k; cin >> k;
    for (int i = 1; i <= k; i++)
    {
        cin >> s[i] >> u[i] >> t[i];
    }
    for (int i = 1; i <= n; i++)
    {
        dist[0][i] = dist[i][0] = 0;
    }

    function<bool(ll)> check = [&] (ll delta) -> bool {
        dp[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            dp[i] = oo;
        }

        for (int lst = 0; lst < k; lst++)
        {
            int r = lst;
            ll time = dist[1][u[r+1]];
            int ind = lst + 1;
            multiset<ll> st;
            while (r < k && max(dp[lst] , 1ll * t[r+1]) + dist[1][u[lst+1]] - s[lst+1] <= delta)
            {
                r++;
                
                // pt j = lst+1...r
                // s[j] >= time - delta + max(dp[j], t[r])
                // pt t[r] > dp[j]
                // s[j] >= time - delta + t[r]
                // altfel
                // s[j] - dp[j] >= time - delta
                st.insert(s[r] - dp[r]);
                while (ind <= r && dp[ind] <= t[r]) {
                    st.erase(st.find(s[ind] - dp[ind]));
                    ind++;
                }
                ll old_val = s[r] - dp[r];
                //if (st.size() && *st.begin() >= time - delta && s[lst + 1] >= time - delta + t[r])
                if (max<ll>(dp[lst], t[r]) + time - s[r] <= delta)
                    dp[r] = min(dp[r] , max(dp[lst] , 1ll * t[r]) + time);
                else break;
                st.erase(st.find(old_val));
                st.insert(s[r] - dp[r]);
                time += dist[u[r]][u[r+1]];
            }
            
        }
        return dp[n] < oo;
    };

    ll delta = 0;

    for (ll bit = (1ll << 59); bit > 0; bit /= 2)
    {
        if (!check (delta | bit)) delta |= bit;
    }

    if (!check(delta)) delta++;
    cout << delta << '\n';

    return 0;
    
}