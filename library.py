import random


def gen_random_int(number: int, seed: int) -> list[int]:
    random.seed(seed)
    array = list(range(number))
    random.shuffle(array)
    return array


def create_string(array: list[int]) -> str:
    return ", ".join(str(number) for number in array) + "."


def my_sort(array):
    # Insertion sort keeps moving the current value left until it is in order.
    for index in range(1, len(array)):
        current_value = array[index]
        position = index - 1

        while position >= 0 and array[position] > current_value:
            array[position + 1] = array[position]
            position -= 1

        array[position + 1] = current_value


def insertion_sort_steps(array):
    working_array = array[:]
    steps = [
        {
            "values": working_array[:],
            "active_indices": [],
            "sorted_until": 0 if len(working_array) > 0 else -1,
            "message": "Start with the first value as the sorted section.",
        }
    ]

    for index in range(1, len(working_array)):
        current_value = working_array[index]
        position = index - 1

        steps.append(
            {
                "values": working_array[:],
                "active_indices": [index],
                "sorted_until": index - 1,
                "message": f"Pick up {current_value} and compare it with the sorted values.",
            }
        )

        while position >= 0 and working_array[position] > current_value:
            shifted_value = working_array[position]
            working_array[position + 1] = shifted_value

            steps.append(
                {
                    "values": working_array[:],
                    "active_indices": [position, position + 1],
                    "sorted_until": index - 1,
                    "message": f"{shifted_value} is bigger than {current_value}, so shift it right.",
                }
            )

            position -= 1

        working_array[position + 1] = current_value

        steps.append(
            {
                "values": working_array[:],
                "active_indices": [position + 1],
                "sorted_until": index,
                "message": f"Place {current_value} into position {position + 1}.",
            }
        )

    if len(working_array) > 0:
        steps.append(
            {
                "values": working_array[:],
                "active_indices": [],
                "sorted_until": len(working_array) - 1,
                "message": "Sorted. Every value is now in order.",
            }
        )

    return steps


def is_text_sorted(array: list[str]) -> bool:
    for index in range(len(array) - 1):
        if array[index].casefold() > array[index + 1].casefold():
            return False

    return True


def thanos_sort(array: list[str], seed=None) -> tuple[list[str], list[str]]:
    survivors = array[:]
    snapped_items = []
    random_generator = random.Random(seed)

    while len(survivors) > 1 and not is_text_sorted(survivors):
        items_to_snap = len(survivors) // 2

        # The "snap" removes random items until the remaining list is sorted.
        for count in range(items_to_snap):
            target_index = random_generator.randrange(len(survivors))
            snapped_items.append(survivors[target_index])

            next_survivors = []
            for index in range(len(survivors)):
                if index != target_index:
                    next_survivors.append(survivors[index])

            survivors = next_survivors

    return survivors, snapped_items


def compare_text(left: str, right: str) -> int:
    left_key = left.casefold()
    right_key = right.casefold()

    if left_key > right_key:
        return 1

    if left_key < right_key:
        return -1

    return 0


def flip_prefix(array: list[str], end_index: int) -> None:
    left_index = 0
    right_index = end_index

    while left_index < right_index:
        temporary_value = array[left_index]
        array[left_index] = array[right_index]
        array[right_index] = temporary_value
        left_index += 1
        right_index -= 1


def find_largest_text_index(array: list[str], end_index: int) -> int:
    largest_index = 0

    for index in range(1, end_index + 1):
        if compare_text(array[index], array[largest_index]) > 0:
            largest_index = index

    return largest_index


def pancake_sort_text(array: list[str]) -> list[str]:
    sorted_array = array[:]
    unsorted_size = len(sorted_array)

    while unsorted_size > 1:
        largest_index = find_largest_text_index(sorted_array, unsorted_size - 1)

        if largest_index != unsorted_size - 1:
            if largest_index != 0:
                flip_prefix(sorted_array, largest_index)

            flip_prefix(sorted_array, unsorted_size - 1)

        unsorted_size -= 1

    return sorted_array


def pancake_sort_steps(array: list[str]) -> list[dict]:
    working_array = array[:]
    steps = [
        {
            "items": working_array[:],
            "flip_index": -1,
            "active_index": -1,
            "locked_from": len(working_array),
            "message": "Start with the whole stack unsorted. The top pancake is index 0.",
            "action": "Start",
        }
    ]

    unsorted_size = len(working_array)

    while unsorted_size > 1:
        largest_index = find_largest_text_index(working_array, unsorted_size - 1)
        largest_value = working_array[largest_index]

        steps.append(
            {
                "items": working_array[:],
                "flip_index": -1,
                "active_index": largest_index,
                "locked_from": unsorted_size,
                "message": f"Find the alphabetically largest item in the unsorted stack: {largest_value}.",
                "action": "Find largest",
            }
        )

        if largest_index == unsorted_size - 1:
            steps.append(
                {
                    "items": working_array[:],
                    "flip_index": -1,
                    "active_index": largest_index,
                    "locked_from": unsorted_size - 1,
                    "message": f"{largest_value} is already at the bottom of the unsorted stack, so lock it in place.",
                    "action": "Already placed",
                }
            )
        else:
            if largest_index != 0:
                flip_prefix(working_array, largest_index)
                steps.append(
                    {
                        "items": working_array[:],
                        "flip_index": largest_index,
                        "active_index": 0,
                        "locked_from": unsorted_size,
                        "message": f"Flip the top {largest_index + 1} items to bring {largest_value} to the top.",
                        "action": "Flip to top",
                    }
                )

            flip_prefix(working_array, unsorted_size - 1)
            steps.append(
                {
                    "items": working_array[:],
                    "flip_index": unsorted_size - 1,
                    "active_index": unsorted_size - 1,
                    "locked_from": unsorted_size - 1,
                    "message": f"Flip the top {unsorted_size} items to place {largest_value} into its final spot.",
                    "action": "Flip into place",
                }
            )

        unsorted_size -= 1

    steps.append(
        {
            "items": working_array[:],
            "flip_index": -1,
            "active_index": -1,
            "locked_from": 0 if len(working_array) > 0 else 1,
            "message": "Done. The menu items are sorted alphabetically.",
            "action": "Sorted",
        }
    )

    return steps
