
p = 12181492810988664495017491178372233835381077107491386374099654651874882048862073437146220579332510437000029696005029005194843775013033539704552333899762179  # openssl prime -safe -generate -bits 512
a = 20891563773462123896204418683194062596038182229362433041917251470169172667990238136369636970581723525230222565705995177166942411535234742247842882232671835  # from /dev/urandom
g = 5  # from spec

g_b_mod_p = 1516175301443637426131882779316154559936339848638096263390014710382066296168727316102600290100930665054572003397946894505779463189661166674146250661830725


def mod_exp(x, y, N):
    if y == 0:
        return 1

    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:  # If y is even
        return (z ** 2) % N
    else:  # If y is odd
        return (x * (z ** 2)) % N


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Hard coded values:\np = {p}\na = {a}\ng = {g}\ng^b % p = {g_b_mod_p}\n')

    g_a_mod_p = mod_exp(g, a, p)
    print(f'g^a % p = {g_a_mod_p}')

    g_ab_mod_p = mod_exp(g_b_mod_p, a, p)

    print(f'g^ab % p = {g_ab_mod_p}')
