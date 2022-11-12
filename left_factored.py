# 1.      
# Write a program to demonstrate left factoring
# from a left factored grammar.
grammar = open("grammar.txt", "r")

left_prod = []
right_prod = {}

for prod in grammar:
    [l, r] = prod.split("->")
    l = l.strip("/n").strip()
    left_prod.append(l)
    r = r.split("|")
    r = [rule.strip(" ").strip("\n") for rule in r]
    right_prod[l] = r


def get_common_characters(values):
    common_characters = []
    for char in values[0]:
        x = 1
        while x < len(values):
            if char in values[x]:
                if x == len(values) - 1:
                    common_characters.append(char)

            x += 1

    return "".join(common_characters)


f_prod_no_lf = []

for l in left_prod:
    if l in right_prod:
        common_seq = get_common_characters(right_prod[l])

        if len(common_seq) != 0:
            f_prod_no_lf.append(f"{l} -> {common_seq}{l}'\n")
            uncommon_char = []
            for char in right_prod[l]:
                [alpha, beta] = char.split(common_seq)
                uncommon_char.append(beta)

            beta = " | ".join(uncommon_char)
            f_prod_no_lf.append(f"{l}' -> {beta}\n")


def main():
    grammar = open("grammar.txt", "r")

    print("***Grammar with Common Prefixes***\n")
    for line in grammar:
        print(line)

    print("****Grammar after Left Factored****\n")
    for word in f_prod_no_lf:
        print(word)


if __name__ == "__main__":
    main()
