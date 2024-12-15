n, k, l, c, d, p, nl, np = map(int, input().split())

quantite_boisson = k * l
quantite_lime = c * d

toasts_boisson = quantite_boisson // (n * nl)
toasts_lime = quantite_lime // n
toasts_sel = p//(n*np)

max_toast_par_ami = min(toasts_boisson, toasts_lime, toasts_sel)

print(max_toast_par_ami)