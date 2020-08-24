import math
import numpy as np
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from zquantum.core.bitstring_distribution import BitstringDistribution


def compute_kl_divergence(
    target_distribution: "BitstringDistribution",
    measured_distribution: "BitstringDistribution",
    distance_measure_parameters: Dict,
) -> float:
    """ Compute the squared KL-divergence distance measure between between a target bitstring distribution
    and a measured bitstring distribution.
        Args:
            target_distribution (BitstringDistribution): The target bitstring probability distribution.
            measured_distribution (BitstringDistribution): The measured bitstring probability distribution.
            distance_measure_parameters (dict):
            - epsilon (float): The small parameter needed to regularize log computation when argument is zero. The default value is 1e-9.
        Returns:
            float: The value of the maximum mean discrepancy.
    """

    epsilon = distance_measure_parameters.get("epsilon", 1e-9)
    value = 0.0
    target_keys = target_distribution.distribution_dict.keys()
    measured_keys = measured_distribution.distribution_dict.keys()
    all_keys = set(target_keys).union(measured_keys)

    for bitstring in all_keys:
        target_bitstring_value = target_distribution.distribution_dict.get(bitstring, 0)
        measured_bitstring_value = measured_distribution.distribution_dict.get(
            bitstring, 0
        )

        value += target_bitstring_value * math.log(
            max(epsilon, measured_bitstring_value)
        )

        value -= target_bitstring_value * math.log(
            max(epsilon, target_bitstring_value)
        )

    return -value
