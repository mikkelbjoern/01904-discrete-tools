def print_row(row):
    for elem in row:
        print(elem, end="\t")
    print("\n", end="")

    
def euclidean_extended_algorithm(a,b):
    print_row("i s_i t_i q_i r_i".split(" "))
    i = 0
    # Using _u and _l to denote the upper and lower row respectively
    s_u, s_l = 1, 0
    t_u, t_l = 0, 1
    r_u, r_l = a, b
    # Print first row, as it will not be printed in the loop (" " makes the space below q empty")
    print_row([-1, s_u, t_u, " ", a])
    
    # Choosing a value for q that makes its place in the printed table empty (pretty hacky I know)
    q = " "
    while r_l != 0:
        print_row([i, s_l, t_l, q, r_l])
        i += 1
        q = r_u // r_l
        new_r = r_u - q * r_l
        new_t = t_u - q * t_l
        new_s = s_u - q * s_l
        
        s_u, s_l = s_l, new_s
        t_u, t_l = t_l, new_t
        r_u, r_l = r_l, new_r
