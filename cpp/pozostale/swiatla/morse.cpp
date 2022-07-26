#include <Arduino.h>
#include <vector>
using namespace std;

void kreska() {
	digitalWrite(LED_BUILTIN, LOW);
	delay(1000);
	digitalWrite(LED_BUILTIN, HIGH);
	delay(500);
}

void kropka() {
	digitalWrite(LED_BUILTIN, LOW);
	delay(300);
	digitalWrite(LED_BUILTIN, HIGH);
	delay(500);
}

void tlumacz(char znak) {
	vector<string> morse = {".-", "-...", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"};
	int ascii_numer = int(znak);
	if (ascii_numer >= 97) {
		string znak_morsem = morse[ascii_numer - 97];
		for (int i = 0; i < znak_morsem.size(); i++) {
			if (znak_morsem[i] == '.') {
				kropka();
			}
			if (znak_morsem[i] == '-') {
				kreska();
			}
		}
	}
	else if (ascii_numer >= 48) {
		string znak_morsem = morse[ascii_numer - 23];
		for (int i = 0; i < znak_morsem.size(); i++) {
			if (znak_morsem[i] == '.') {
				kropka();
			}
			if (znak_morsem[i] == '-') {
				kreska();
			}
		}
	}
	else if (ascii_numer == 32) {
		delay(1500);
	}
}

void setup() {
	// put your setup code here, to run once:
	pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
	// put your main code here, to run repeatedly:
	string tekst = "ala ma kota";
	for (int i = 0; i < tekst.size(); i++) {
		tlumacz(tekst[i]);
		delay(1000);
	}
	delay(25000);
}
