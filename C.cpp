#include <iostream>
#include <cmath>
#define ull unsigned long long

using namespace std;

int main() {
	ull n;
	cin >> n;
	ull s = 0;
	ull p = pow(10, 9) + 7;

	if (n % 2 == 0) {
		s = 1;
		ull t = pow(3, 20);
		for (ull i = 0; i < (n / 2) / t; ++i) {
			s *= t;
			while (s > p) {
				s -= p;
			}
		}
		for (ull i = 0; i < (n / 2) % t; ++i) {
			s *= 3;
			while (s > p) {
				s -= p;
			}
		}
		s *= 2;
	} else {
		s = 1;
		ull t = pow(3, 20);
		for (ull i = 0; i < ((n - 1) / 2) / t; ++i) {
			s *= t;
			while (s > p) {
				s -= p;
			}
		}
		for (ull i = 0; i < ((n - 1) / 2) % t; ++i) {
			s *= 3;
			while (s > p) {
				s -= p;
			}
		}
		s *= 4;
	}
	cout << s % p << endl;
}
