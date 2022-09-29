import L1
import L2
import L3

pil = input("Program Machine TBO\n1.L1 bahasa yang diawali oleh simbol yang sama dengan akhir sigma=(0,1)\n2.L2 bahasa terdapat jumlah 0 mod 3 =1 sigma=(0,1)\n3.L3 bahasa yang memiliki substring 000 didalamnya sigma=(1,0)\npilihan:")
print("tulis kata:")
match pil:
    case "1":
        L1.mulai(input())
    case "2":
        L2.mulai(input())
    case "3":
        L3.mulai(input())