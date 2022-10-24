#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
	int n, m, a, b;
	cin >> n >> m >> a >> b;
	//cout << n  << ' ' << m << ' ' << a << ' ' << b << endl;
	vector<vector<int>> d (n, vector<int> (m));

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			cin >> d[i][j];

	int maxx = 0;

	for (int p = a - 1; p > -1; --p) {
		for (int q = b - 1; q > -1; --q) {
			for (int r = a - 1; r < n; ++r) {
				for (int s = b - 1; s < m; ++s) {
					int x = d[p][q] + d[r][s] + 2 * (r - p + 1 + s - q + 1);
					maxx = max(maxx, x);
					//cout << p << ' ' << q << ' ' << r << ' ' << s << ' ' << x << ' ' << maxx << endl;
				}
			} 
		} 
	} 
	cout << maxx << endl;
}