from sympy import symbols, parse_expr
import itertools


def beautify_formula(input_str):
    words = input_str.split()
    beautiful_str = ' '.join(words)
    return beautiful_str


def binary_to_decimal(binary_str):
    decimal_int = int(binary_str, 2)
    return decimal_int


def replace_spaces_with_commas(input_string):
    numbers = input_string.split()
    output_string = ", ".join(numbers)
    output_string = output_string.rstrip()
    return output_string


def print_doc():
    print("Калькулятор таблиці істинності для булевих функцій з трьома змінними")
    print("Довідка:")
    print("( ) - дужки")
    print("~ - заперечення")
    print("& - кон'юнкція (І)")
    print("| - диз'юнкція (АБО)")
    print(">> - імплікація (→)")
    print("== - еквівалентність (↔)")
    print("^ - XOR (виключне І)")
    print("~(x & y) - штрих Шеффера (↑) (NAND) - заперечення кон'юнкції")
    print("~(x | y) - стрілка Пірса (↓) (NOR) - заперечення диз'юнкції")
    print()
    print("Пробіли строго важливі!!")
    print("Програма не підтримує валідацію формул")
    print()
    print("Записувати треба лише саму формулу")
    print()
    print("Приклади формул:")
    print("(x | y) >> y ^ z")
    print("(x & y) | z")
    print("(x | y) & ~(y & z)")
    print("(x ^ y) ^ (~x >> z)")
    print("(x & y) == z")


def main():
    print_doc()
    print("Введіть формулу функції з трьома змінними:")

    x, y, z = symbols('x y z')
    formula_str = input()
    formula_str = beautify_formula(formula_str)
    formula = parse_expr(formula_str)

    print(f"\nf(x, y, z) = {formula_str}\n")
    caption = "| x | y | z | f |"
    print(caption)
    print("-" * len(caption))

    binary_number = ""
    set_numbers = ""
    i = -1

    for combination in itertools.product([0, 1], repeat=3):
        x_val, y_val, z_val = combination
        formula_val = formula.subs({x: x_val, y: y_val, z: z_val})
        formula_val = int(bool(formula_val))
        print(f"| {x_val} | {y_val} | {z_val} | {formula_val} |")
        i += 1
        binary_number += str(formula_val)
        if formula_val == 1:
            set_numbers += f"{i} "

    print("\nПорівняльні номери:")
    print(f"f({binary_number}) f({binary_to_decimal(binary_number)})")
    print("\nНомери наборів на яких функція дорівнює 1:")
    print(f"f = v({replace_spaces_with_commas(set_numbers)})")
    print(" " * 4 + "1")


if __name__ == "__main__":
    main()
