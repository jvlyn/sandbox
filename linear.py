# NOTE: This is a SAGE script. Will NOT work in plain old Python.
# To download SAGE, visit http://www.sagemath.org/.

import sympy
import itertools

def get_roots(poly):
    k.<a> = GF(3**poly.degree(), modulus=poly)
    R.<x> = PolynomialRing(k, "x")
    poly = R(poly) # coercing polynomial into ring
    factor_obj = poly.factor()
    coeff_list = []
    for factor in factor_obj: # each factor is factor, multiplicity tuple
        coeffs = sympy.Poly(sympy.sympify(factor[0] - R(x)), sympy.var("a")).all_coeffs()
        coeff_list += [coeffs]
    final_list = []
    for row in coeff_list:
        while len(row) < poly.degree():
            row = [0] + row
        final_list += [row]
    return final_list

def find_lines(coeff_list):
    k = GF(3)
    combinations = itertools.combinations(coeff_list, 3) # find all three-element subsets
    # combinations is iterable collection of tuples (containing lists)
    for combo in combinations:
        is_line = True
        for i in range(len(coeff_list[0])): # degree of poly
            if k(int(combo[0][i]) + int(combo[1][i]) + int(combo[2][i])) != k(0):
                is_line = False # not a line
        if is_line:
            return True
    return False

def main():
    degree = int(input("Degree to test: "))
    R.<x> = PolynomialRing(GF(3), "x")
    f = R(x ** (3 ** degree) - x)
    print(f)
    linears = []
    for factor in f.factor():
        if (find_lines(get_roots(factor[0]))):
            linears += [factor[0]]
    for poly in linears:
        print(R(poly).derivative()) # testing formal derivatives

if __name__ == "__main__":
    main()
