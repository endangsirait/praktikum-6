import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x*2 + y*2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

# Contoh penggunaan
result_a = a(7)
result_b = b(4, 5)
result_c = c(1, 2, 3, 4, 5, 6, 7)
result_d = d("hello")

print("Hasil fungsi a:", result_a)
print("Hasil fungsi b:", result_b)
print("Hasil fungsi c:", result_c)
print("Hasil fungsi d:", result_d)