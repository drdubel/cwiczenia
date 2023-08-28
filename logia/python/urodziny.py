dzien_roku = {
    1: 0,
    2: 31,
    3: 59,
    4: 90,
    5: 120,
    6: 151,
    7: 181,
    8: 212,
    9: 243,
    10: 273,
    11: 304,
    12: 334,
    31: "02",
    59: "03",
    90: "04",
    120: "05",
    151: "06",
    181: "07",
    212: "08",
    243: "09",
    273: "10",
    304: "11",
    334: "12",
}


def czy_przes(rok):
    if rok % 100 != 0 and rok % 4 == 0 or rok % 400 == 0:
        return 366
    return 365


def który_dzien_roku(data, il_dni_roku):
    dzien = 0
    miesiac = int(data[3:5])
    if miesiac > 2 and il_dni_roku == 366:
        dzien += 1
    dzien += dzien_roku[miesiac]
    dzien += int(data[1:3])
    return dzien


def data_dni_temu(ile_dni, il_dni_roku, data):
    dzien = który_dzien_roku(data, il_dni_roku)
    if dzien <= ile_dni:
        ile_dni -= dzien
        data = f"u3112{int(data[5:9])-1}"
        il_dni_roku = czy_przes(int(data[5:9]))
        dzien = il_dni_roku
    dzien -= ile_dni
    dzien_w_miesiacu = 1
    while dzien not in dzien_roku:
        dzien -= 1
        dzien_w_miesiacu += 1
    miesiac = dzien_roku[dzien]
    dzien_w_miesiacu -= il_dni_roku - 364
    if dzien_w_miesiacu < 10:
        dzien_w_miesiacu = f"0{dzien_w_miesiacu}"
    data = f"u{dzien_w_miesiacu}{miesiac}{data[5:9]}"
    return data


def urodziny(urodzenie, która):
    rok = int(urodzenie[5:9])
    ile_dni = 0
    while ile_dni < która * 1000:
        ile_dni += czy_przes(rok)
        rok += 1
    urodzenie = urodzenie[0:5] + str(rok)
    return data_dni_temu(ile_dni - która * 1000, czy_przes(rok), urodzenie)


print(urodziny("u13022004", 2))
