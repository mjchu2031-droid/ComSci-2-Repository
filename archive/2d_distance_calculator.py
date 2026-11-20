"""
2D Distance Calculator
----------------------
Author: MARKELLUS JHAMES CHU
Course: Computer Science 2
Description: Calculates the straight-line (Euclidean) distance between 
             two 2D coordinates using Python's math library.
"""

import math

"""
2D Distance Calculator
----------------------
Calculates the straight-line (Euclidean) distance between two points 
(x1, y1) and (x2, y2) on a 2D Cartesian plane using Python's math library.
"""

import math


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the Euclidean distance between two 2D points.

    Parameters:
        x1, y1 (float): Coordinates of the first point.
        x2, y2 (float): Coordinates of the second point.

    Returns:
        float: The straight-line distance between the two points.
    """
    delta_x = x2 - x1
    delta_y = y2 - y1
    return math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))


def main():
    print("=== 2D Distance Calculator ===")

    # Input: Collect coordinates from the user
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Calculation: Compute the distance between points
    distance = calculate_distance(x1, y1, x2, y2)

    # Output: Print formatted result
    print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")


if __name__ == "__main__":
    main()
