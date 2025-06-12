#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;
const int NMAX = 2e5;

vector<pair<int , int> > adj[NMAX+1];
int w[NMAX+1]; // w dupa indicele nodului repr

struct Aint {
	// aint cu lazy pe maxime
	int n , offset;
	vector<int> aint , lazy;

	Aint (int _n) : n(_n) {
		offset = 1;
		while (offset < n) offset <<= 1;
		aint.resize(2*offset , 0);
		lazy.resize(2*offset , 0);
		
	}

	void update (int l , int r, int val=1) {
        if (r < l) return;
		upd(1 , 1 , offset , l , r , val);
	}

	void dfs (int nod = 1) {
        push_lazy(nod);
        if (nod >= offset) return;
        auto [f1 , f2] = children(nod);
        dfs(f1);
        dfs(f2);
    }

    vector<int> values () {
		vector<int> ret(n+1 , 0);
        for (int i = offset; i < offset + n; i++) {
            ret[i-offset+1] = aint[i];
        }
        return ret;
    }

	
private:

	pair<int , int> children (int nod) {
		return make_pair(2*nod , 2*nod + 1);
    }


	void upd (int nod , int l , int r , int ul , int ur , int val) {
	    push_lazy(nod);	
        if (ul <= l && r <= ur) {
			lazy[nod] += val;
			push_lazy(nod);
		}
		else if (l > ur || r < ul) return;
		else {
			int m = (l+r) / 2;
			auto [f1 , f2] = children(nod);
			upd(f1 , l , m , ul , ur , val);
			upd(f2 , m+1, r, ul , ur , val);
		}
	}

	void push_lazy (int nod) {
		auto [f1 , f2] = children(nod);
		if (nod < offset) {
			lazy[f1] += lazy[nod];
			lazy[f2] += lazy[nod];
		}
		aint[nod] += lazy[nod];
		lazy[nod] = 0;
	}
};

int depth[NMAX+1];
int subtree[NMAX+1];

struct Lca {
	int n , log2n;
    vector<vector<int> > up;
	Lca (int _n) : n(_n) {
		log2n = log2(n) + 2;
		up.resize(log2n , vector<int> (n+1 , 0));
		dfs(1);
		for (int b = 1; b < log2n; b++) {
			for (int i = 1; i <= n; i++) {
				up[b][i] = up[b-1][up[b-1][i]];
			}
		}

    }

    void dfs (int nod , int par = 0) {

        subtree[nod] = 1;
        depth[nod] = depth[par]+1;
        up[0][nod] = par;
        
        for (auto [to , cost] : adj[nod]) {
            if (to == par) continue;
            dfs(to , nod);
            subtree[nod] += subtree[to];
        }

    }

	int lca (int x , int y) {
		if (depth[x] < depth[y]) swap(x,y);

		int delta = depth[x] - depth[y];
		for (int b = 0; b < log2n; b++) {
			if (delta & (1 << b)) x = up[b][x];
		}

		if (x == y) return x;
		for (int b = log2n-1; b >= 0; b--) {
			if (up[b][x] != up[b][y]) {
				x = up[b][x];
				y = up[b][y];
			}
		}

		return up[0][x];
	}
};

int lant[NMAX+1]; // indicele lantului din care nodul face parte
int pos_lant[NMAX+1]; // pozitia nodului in lantul sau
int size_lant[NMAX+1];
int par_lant[NMAX+1]; // nodul din care se "desparte" lantul
int nr_lanturi = 0;
int start_lant[NMAX+1];
int visited = 0;

vector<int> hld_order = {0};

void heavy_light_dfs (int nod = 1) {
	pair<int , int> heavy_child = {-1 , -1};
	visited++;
	hld_order.push_back(nod);
    for (auto [to , _w] : adj[nod]) {
        if (lant[to]) continue;
        heavy_child = max(heavy_child , make_pair(subtree[to] , to));
        w[to] = _w;
    }

    if (heavy_child.first != -1){
        // dfs heavy
        pos_lant[heavy_child.second] = pos_lant[nod]+1;
        size_lant[nr_lanturi]++;
        lant[heavy_child.second] = nr_lanturi;
        heavy_light_dfs (heavy_child.second);
    }

    for (auto [to , _w] : adj[nod]) {
        if (lant[to]) continue;
        nr_lanturi++;
        lant[to] = nr_lanturi;
        size_lant[nr_lanturi] = 1;
        pos_lant[to] = 1;
        start_lant[nr_lanturi] = visited+1;
        par_lant[nr_lanturi] = nod;
        heavy_light_dfs (to);
    }
}

void init_hld () {
    w[1] = 0;
	lant[1] = 1; // indicele lantului din care nodul face parte
    pos_lant[1] = 1; // pozitia nodului in lantul sau
    size_lant[1] = 1;
    par_lant[1] = 0; // nodul din care se "desparte" lantul
    nr_lanturi = 1;
    start_lant[1] = 1;

	heavy_light_dfs(1);

}

void update_hld (Aint &aint , int from, int to) {

	int nod = from, _lant = lant[from];

	while (_lant != lant[to]) {
		aint.update (start_lant[_lant] , start_lant[_lant] + pos_lant[nod]-1);
		nod = par_lant[_lant];
		_lant = lant[nod];
	}

	aint.update (start_lant[_lant] + pos_lant[to] , start_lant[_lant] + pos_lant[nod] - 1);
	
}

struct Edge {
	bool friend operator < (const Edge &e1 , const Edge &e2) {
		if (e1.app != e2.app) return e1.app < e2.app;
		else return e1.w < e2.w;
	}
	int w , app;

};

const int MOD = 666013;

int main () {

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    freopen("amazon.in" , "r" , stdin);
    freopen("amazon.out" , "w" , stdout);

	int n; cin >> n;
	for (int i = 1; i < n; i++) {
		int x , y , _w; cin >> x >> y >> _w;
        x++ , y++;
		adj[x].push_back({y , _w});
		adj[y].push_back({x , _w});
	}

	Lca comp_lca(n);
	Aint aint(n);
	init_hld();

	int m , k; cin >> m >> k;
	for (int i = 1; i <= m; i++) {

        int x , y; cin >> x >> y;
        x++ , y++;
        int lca = comp_lca.lca(x , y);

        update_hld(aint , x , lca);
        update_hld(aint , y , lca);	

	}

	aint.dfs();
	vector<int> vals = aint.values();
	vector<Edge> edges(n+1 , {0,0});

    // for (auto x : hld_order) cout << x << ' '; cout << '\n';
    
	for (int i = 1; i <= n; i++) {
        edges[i] = {w[hld_order[i]] , vals[i]};
        // cout << hld_order[i] << ' ' << vals[i] << '\n';
        // cout << w[hld_order[i]] << '\n';
	}
    
	sort(edges.begin() , edges.end());
    

	int ind = n;
	while (k && ind > 0) {
		if (k > edges[ind].w) {
			k -= edges[ind].w;
			edges[ind].w = 0;
		}
		else {
			edges[ind].w -= k;
			k = 0;
		}
		ind--;
    }

    long long ans = 0;
    for (int i = 1; i <= n; i++) {
        ans += 1ll * edges[i].w * edges[i].app;
    }

    cout << ans % MOD << '\n';

}

