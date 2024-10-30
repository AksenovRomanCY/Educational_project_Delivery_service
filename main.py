"""This module calculates the minimum number of transport platforms.

A rover on Mars must transport these robots to specific locations on
the planet's surface. To achieve this, it has access to an unlimited
number of transport platforms, each capable of carrying up to a
specified weight limit. Each platform can carry either one robot or
two robots, provided that their combined weight does not exceed the
platform's weight limit.

The algorithm aims to minimize the number of platforms used for
the transportation, while ensuring that no platform exceeds its
weight limit.

Functions provided:
- optimal_number_of_platforms: Calculates the minimum number of
  platforms required to transport all robots based on their
  weights and the weight limit of each platform.
- main: Reads input from stdin, calls the optimal_number_of_platforms
  function, and prints the result.

Input format:
- A list of integers, where each integer represents the weight of a robot.
- An integer representing the weight limit of each platform.

Output format:
- An integer indicating the minimum number of platforms required
  to transport all robots.

Constraints:
- The number of platforms is unlimited.
- Each platform has a maximum weight capacity of `limit`.
- A platform can carry no more than two robots, provided their
  combined weight does not exceed `limit`.
- The weight of a single robot will not exceed `limit`.

This module can be used for resource allocation and optimization
problems where efficient weight distribution is required, such as
in transportation and logistics on extraterrestrial surfaces.
"""
import sys


def optimal_number_of_platforms(
        objects_weight: list[int],
        limit_by_platform: int) -> int:
    """Calculates the optimal number of platforms.

    Args:
        objects_weight (list[int]): A list of weights of the robots to be
                                    transported.
        limit_by_platform (int): The maximum weight limit each platform can
                                 carry.

    Returns:
        int: Minimum number of platforms required to carry all objects
             without exceeding
        the weight limit of each platform.
    """

    # Sort weight of objects.
    objects_weight.sort()

    # Left and right pointers indexes.
    left_pointer = 0
    right_pointer = len(objects_weight) - 1

    # A counter for the number of platforms
    # required to transport all objects.
    platforms_counter = 0

    # The loop lasts until the right pointer is smaller than the left pointer.
    while left_pointer <= right_pointer:

        # Summarizes objects from two different points in the array.
        sum_of_two_of_objects = (
                objects_weight[left_pointer]
                + objects_weight[right_pointer])

        # Checks if the sum of objects is greater than the limit.
        equality_check = sum_of_two_of_objects > limit_by_platform

        # If equality_check True and one of the objects is larger
        # than the other, truncates the index of that object.
        # Else, both indexes are cut.
        if (equality_check
                and objects_weight[left_pointer]
                > objects_weight[right_pointer]):
            left_pointer += 1
        elif (equality_check
                and objects_weight[left_pointer]
                <= objects_weight[right_pointer]):
            right_pointer -= 1
        else:
            left_pointer += 1
            right_pointer -= 1

        # Increases the platform counter.
        platforms_counter += 1

    # Return the required number of platforms.
    return platforms_counter


def main():
    """Main function"""
    # Requests robot weights with a space and converts to
    # a list with elements of type int.
    weight_of_robots = list(map(int, sys.stdin.readline().split()))

    # Requests the maximum weight carried by the platform.
    weight_limit = int(sys.stdin.readline().rstrip())

    # Calls a function to calculate the optimal number of platforms.
    # And prints the result.
    print(optimal_number_of_platforms(
        objects_weight=weight_of_robots,
        limit_by_platform=weight_limit))


# Entry point for the script.
if __name__ == '__main__':
    main()