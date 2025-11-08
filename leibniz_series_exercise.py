def approximate_pi(n_terms):
    num = 0
    for i in range(n_terms):
      a = (-1) ** i
      b = (2*i +1)
      c = a/b
      num += c
    return (4 * num)
