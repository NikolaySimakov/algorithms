#include <bits/stdc++.h>
using namespace std;

const int N = 100 + 1;
int a[N][7];
int n;
void solve()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= 6; j++)
        {
            cin >> a[i][j];
        }
    }
    double ans = 0;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (i == j)
            {
                continue;
            }
            double ver = n * (n - 1);
            for (int k = 1; k <= 6; k++)
            {
                for (int t = 1; t <= 6; t++)
                {
                    ans += (a[i][k] + a[j][t]) * (a[i][k] + a[j][t]) * (a[i][k] + a[j][t]) / ver / 36.0;
                }
            }
        }
    }
    cout << ans << endl;
}

int main()
{
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    cout.setf(ios::fixed), cout.precision(7);
    solve();
}