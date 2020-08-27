def compute_zero_cost(
    target_distribution, measured_distribution, distance_measure_parameters
):
    """Returns 0 all the time.
    """

    epsilon = distance_measure_parameters.get("epsilon", 1e-9)
    value = 0.0
    target_keys = target_distribution.distribution_dict.keys()
    measured_keys = measured_distribution.distribution_dict.keys()
    return value
