#include <bits/stdc++.h>
using namespace std;

const int N = 500 + 10;
const long long INF = 1e18;
int n;
long long dist[N][N];
void solve()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> dist[i][j];
            if (dist[i][j] == -1)
            {
                dist[i][j] = INF;
            }
        }
    }
    for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                dist[i][j] = max(dist[i][j], min(dist[i][k], dist[k][j]));
            }
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (dist[i][j] == INF || i == j)
            {
                cout << 2000000023 << " ";
            }
            else
            {
                cout << dist[i][j] << " ";
            }
        }
        cout << endl;
    }
}

int main()
{
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    solve();
}