#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
int n, c, k;
int a[6];

void solve()
{
    cin >> k >> n;
    long long sum = 0;

    for (int i = 1; i <= k; i++)
    {
        cin >> a[i];
        sum += a[i];
    }
    long long cnt = (n / k);
    sum *= cnt;
    sort(a + 1, a + k + 1);
    int oc = n % k;
    for (int i = k; i >= 1; i--)
    {
        if (oc == 0)
        {
            break;
        }
        sum += a[i];
        oc--;
    }
    cout << sum << endl;
}

int main()
{
    ios::sync_with_stdio(NULL), cin.tie(0), cout.tie(0);
    cout.setf(ios::fixed), cout.precision(7);
    // freopen("input.txt", "r", stdin);
    //  freopen("output.txt", "w", stdout);
    solve();
}