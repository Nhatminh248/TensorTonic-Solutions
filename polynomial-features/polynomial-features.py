def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    return [[value ** d for d in range(degree + 1)] for value in values]