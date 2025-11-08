def approximate_pi(n_terms):
    for n in range(n_terms):
        numerator = (-1)**n 
        denominator = (2 * n) + 1
        term = numerator / denominator
        leibniz_series.append(term)
    series_sum = sum(leibniz_series)
    approx_pi = 4 * series_sum
    return approx_pi
