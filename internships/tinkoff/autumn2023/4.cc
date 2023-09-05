#include <iostream>
#include <vector>

int main() {
  int n, m;
  std::cin >> n >> m;
  std::vector <int> a(m);
  for (auto& banknote: a) {
    std::cin >> banknote;
  }
  for (int mask = 1; mask < (1 << (m * 2)); ++mask) {
    long long sum = 0;
    for (int banknote = 0; banknote < m; ++banknote) {
      if (mask & (1 << (2 * banknote))) {
        sum += a[banknote];
      }
      if (mask & (1 << (2 * banknote + 1))) {
        sum += a[banknote];
      }
    }
    if (sum == n) {
      std::vector <int> ans;
      for (int banknote = 0; banknote < m; ++banknote) {
        if (mask & (1 << (2 * banknote))) {
          ans.push_back(a[banknote]);
        }
        if (mask & (1 << (2 * banknote + 1))) {
          ans.push_back(a[banknote]);
        }
      }
      std::cout << ans.size() << "\n";
      for (auto& i: ans) {
        std::cout << i << " ";
      }
      return 0;
    }
  }
  std::cout << -1;
}