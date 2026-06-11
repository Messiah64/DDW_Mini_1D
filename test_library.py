from library import gen_random_int, my_sort, create_string, insertion_sort_steps
from library import pancake_sort_steps, pancake_sort_text
from exercise_3_logic import make_menu_items, make_menu_string, sort_menu_text

def test_gen_random_int():
    output = gen_random_int(10, 100)
    assert output == [4, 0, 5, 9, 3, 1, 6, 8, 7, 2]

def test_my_sort():
    array = [10.3,3.8,8.4,47.1,1.0,0,-39.8,8.4,4.7,7.6,-6.5,-5.0]
    my_sort(array)
    assert array == [-39.8, -6.5, -5.0, 0.0, 1.0, 3.8, 4.7, 7.6, 8.4, 8.4, 10.3, 47.1]

def test_create_string():
    array = [4, 0, 5, 9, 3, 1, 6, 8, 7, 2]
    output = create_string(array)
    assert output == "4, 0, 5, 9, 3, 1, 6, 8, 7, 2."

def test_insertion_sort_steps():
    array = [4, 1, 3, 2]
    steps = insertion_sort_steps(array)

    assert array == [4, 1, 3, 2]
    assert steps[-1]["values"] == [1, 2, 3, 4]
    assert steps[-1]["message"] == "Sorted. Every value is now in order."

def test_pancake_sort_text():
    array = ["Blueberry Stack", "apple cinnamon", "Mango Cloud", "banana split"]
    output = pancake_sort_text(array)

    assert array == ["Blueberry Stack", "apple cinnamon", "Mango Cloud", "banana split"]
    assert output == ["apple cinnamon", "banana split", "Blueberry Stack", "Mango Cloud"]

def test_pancake_sort_steps():
    array = ["delta", "alpha", "charlie", "bravo"]
    steps = pancake_sort_steps(array)

    assert array == ["delta", "alpha", "charlie", "bravo"]
    assert steps[-1]["items"] == ["alpha", "bravo", "charlie", "delta"]
    assert steps[-1]["action"] == "Sorted"

def test_make_menu_items():
    output = make_menu_items(" Mango Stack, , apple stack, Banana Stack ")
    assert output == ["Mango Stack", "apple stack", "Banana Stack"]

def test_make_menu_string():
    output = make_menu_string(["Mango Stack", "Apple Stack"])
    assert output == "Mango Stack, Apple Stack"

def test_sort_menu_text():
    output = sort_menu_text("delta, alpha, charlie, bravo")

    assert output["ok"] == True
    assert output["original_items"] == ["delta", "alpha", "charlie", "bravo"]
    assert output["sorted_items"] == ["alpha", "bravo", "charlie", "delta"]
    assert output["steps"][-1]["action"] == "Sorted"

def test_sort_menu_text_with_blank_input():
    output = sort_menu_text(" , , ")

    assert output["ok"] == False
    assert output["error"] == "Please enter at least one menu item."
