#7. Гуси и кролики. У гусе и кроликов 2n лап. Сколько может быть гусей и
#кроликов (вывести все возможные сочетания)?

n = int(input("Введите число N лап: "))
print('Всего лап:', 2 * n);
g = (2*n % 4) / 2;
k = (2*n - 2*g) / 4;
print("%6s %16s" % ("гуси", "кролики"));
while k != 0:
    print("%5s %15s" % (int(g), int(k)));
    g += 2;
    k -= 1;
