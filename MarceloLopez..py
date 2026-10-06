# MarceloLopez | LÍMITE: N = 16

def main():
    N = 16
    cedulas, nombres = [None] * N, [None] * N
    total = 0

    while True:
        print(f"\n--- CENSO HOSPITAL SAN RAFAEL [{total}/{N}] ---")
        op = input("1.Agregar 2.Buscar 3.Corregir 4.Dar de baja 5.Reporte 6.Salir\nOpción: ").strip()

        if op == "1":
            if total >= N:
                print("[!] Memoria llena (Límite 16).")
            else:
                c = input("Cédula: ").strip()
                if c in cedulas[:total]:
                    print("[!] Cédula ya registrada.")
                else:
                    cedulas[total], nombres[total] = c, input("Nombre: ").strip()
                    total += 1
                    print("[✓] Registrado.")

        elif op in ["2", "3", "4"]:
            if total == 0:
                print("[!] Censo vacío.")
                continue
            c = input("Cédula a consultar: ").strip()
            pos = cedulas[:total].index(c) if c in cedulas[:total] else -1

            if pos == -1:
                print("[!] No encontrado.")
            elif op == "2":
                print(f"[✓] {nombres[pos]} (Cédula: {cedulas[pos]})")
            elif op == "3":
                nombres[pos] = input("Nuevo nombre: ").strip()
                print("[✓] Actualizado.")
            elif op == "4":
                for j in range(pos, total - 1):
                    cedulas[j], nombres[j] = cedulas[j + 1], nombres[j + 1]
                total -= 1
                cedulas[total], nombres[total] = None, None
                print("[✓] Dado de baja.")

        elif op == "5":
            print(f"\n-- REPORTE ({total}/{N}) --")
            for i in range(total):
                print(f"[{i}] {cedulas[i]} - {nombres[i]}")

        elif op == "6":
            break

if __name__ == "__main__":
    main()
