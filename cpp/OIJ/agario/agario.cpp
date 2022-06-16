#include <functional>
#include <iostream>
#include <vector>
#include <sstream>
using namespace std;


int agario(int il_przeciwnikow, vector<int> przeciwnicy) {
	int czas = 0;
	int wynik = 2;
	sort(przeciwnicy.begin(), przeciwnicy.end(), greater<int>());
	if (przeciwnicy[-1] >= wynik) {
		return 0;
	}
	int najwiekszy = przeciwnicy[0];
	vector<int> mniejsi;
	for (int i=0; i < il_przeciwnikow; i++)
        cout << przeciwnicy[i] << "\n";
	while (wynik < najwiekszy) {
		while (przeciwnicy[-1] < wynik) {
			mniejsi.push_back(przeciwnicy.back());
			przeciwnicy.pop_back();
		}
		if (mniejsi.size() > 0) {
			wynik += mniejsi.back();
			mniejsi.pop_back();
			czas++;
		}
		else {
			return 0;
		}
	}
	return czas;
}


int main() {
	int il_przeciwnikow;
	cin >> il_przeciwnikow;
	vector<int> przeciwnicy(il_przeciwnikow);
	for (int i = 0; i < il_przeciwnikow; i++) cin >> przeciwnicy[i];
	int czas = agario(il_przeciwnikow, przeciwnicy);
	if (czas == 0) {
		cout << "NIE";
	}
	else {
		cout << czas << "\n";
	}
}
