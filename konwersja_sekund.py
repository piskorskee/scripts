#to je wazne!! W jaki sposob zmienic sekundy na minuty etc
def calc_time(sek):
        days = (sek // 86400) % 86400
        hours = (sek // 3600) % 3600
        minutes = (sek // 60) % 60
        seconds = sek % 60
        print(days, hours, minutes, seconds)

wci = float(input('podaj liczbe sek'))
calc_time(wci)