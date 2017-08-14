from itertools import product


def cross(rows, cols):
    """
    Cross product of elements in rows and elements in cols.

    Args:
        rows (list): a list of rows
        cols (list): a list of columns

    Returns:
        dict: vectorial product of rows x columns

    """

    return ['%s%s' % item for item in product(rows, cols)]


assignments = []

COLUMNS = '123456789'
ROWS = 'ABCDEFGHI'
BOXES = cross(ROWS, COLUMNS)
ROW_UNITS = [cross(r, COLUMNS) for r in ROWS]
COLUMN_UNITS = [cross(ROWS, c) for c in COLUMNS]
SQUARE_UNITS = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
UNIT_LIST = ROW_UNITS + COLUMN_UNITS + SQUARE_UNITS
UNITS = dict((s, [u for u in UNIT_LIST if s in u]) for s in BOXES)
PEERS = dict((s, set(sum(UNITS[s], [])) - set([s])) for s in BOXES)

DIAGONAL_SUDOKU = ''.join([
    '2........',
    '.....62..',
    '..1....7.',
    '..6..8...',
    '3...9...7',
    '...6..4..',
    '.4....8..',
    '..52.....',
    '........3'
])


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(sudoku):
    """
    Eliminate values using the naked twins strategy.

    Args:
        sudoku (dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        dict: sudoku with the naked twins eliminated from peers.

    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.

    Args:
        grid (string): A grid in string form.

    Returns:
        dict: Grid in dictionary form

            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'.

            If the box has no value, then the value will be '123456789'.

    """

    assert len(grid) == 81
    sudoku = dict(zip(BOXES, grid))
    return {key: val.replace('.', COLUMNS) for key, val in sudoku.items()}


def display(sudoku):
    """
    Display the values as a 2-D grid.

    Args:
        sudoku (dict): The sudoku in dictionary form

    """

    width = 1 + max(map(lambda box: len(sudoku[box]), BOXES))
    line = '+'.join(['-'*(width*3)]*3)

    for row in ROWS:
        puzzle = [sudoku[row + col].center(width) + ('|' if col in '36' else '') for col in COLUMNS]
        print(''.join(puzzle))

        if row in 'CF':
            print(line)

    return


def eliminate(sudoku):
    """
    Go through all the boxes, and whenever there is a box with a value,
    eliminate this value from the values of all its peers.

    Args:
        sudoku (dict): Partially or totally solved sudoku puzzle

    Returns:
        dict: Sudoku with values eliminated of all its peers

    """

    solved_values = filter(lambda box: len(sudoku[box]) == 1, sudoku.keys())

    for box in solved_values:
        digit = sudoku[box]

        for peer in PEERS[box]:
            sudoku[peer] = sudoku[peer].replace(digit, '')

    return sudoku


def only_choice(sudoku):
    """
    Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Args:
        sudoku: Sudoku in dictionary form.

    Returns:
        dict: Sudoku after filling in only choices.

    """

    for unit in UNIT_LIST:
        for digit in COLUMNS:
            box_with_digit = lambda box: digit in sudoku[box]
            digit_places = [_ for _ in filter(box_with_digit, unit)]

            if len(digit_places) == 1:
                sudoku[digit_places[0]] = digit

    return sudoku


def count_solved_boxes(sudoku):
    """
    Args:
        sudoku(dict): Partially or totally solved sudoku puzzle

    Returns:
        int: Number of boxes with a valid solution

    """

    return len({box: values for box, values in sudoku.items() if len(values) == 1})


def sudoku_has_solution(sudoku):
    """
    Args:
        sudoku(dict): Partially or totally solved sudoku puzzle

    Returns:
        bool: False if at least one box has not a solution, True otherwise

    """

    unsolvable_boxes = {box: values for box, values in sudoku.items() if len(values) == 0}
    return len(unsolvable_boxes) == 0


def reduce_puzzle(sudoku):
    """
    Reduce number of unsolved boxes in the sudoku

    Args:
        sudoku (dict): Partially solved sudoku puzzle

    Returns:
        dict: Partially or totally solved puzzle

    """

    has_changed = False

    while not has_changed:
        solved_values_before = count_solved_boxes(sudoku)

        sudoku = eliminate(sudoku)
        sudoku = only_choice(sudoku)
        solved_values_after = count_solved_boxes(sudoku)

        if not sudoku_has_solution(sudoku):
            return False

        has_changed = solved_values_before == solved_values_after

    return sudoku


def sudoku_is_solved(sudoku):
    """
    Args:
        sudoku(dict): Partially or totally solved sudoku puzzle

    Returns:
        bool: True if puzzle is solved, False otherwise

    """

    return all(map(lambda box: len(sudoku[box]) == 1, BOXES))


def find_best_candidate_box(sudoku):
    """
    Args:
        sudoku (dict): Partially solved Sudoku puzzle

    Returns:
        str: Box that is the best candidate to solve the puzzle

    """

    unsolved_box = lambda box: len(sudoku[box]) > 1
    calculate_box_length = lambda box: (len(sudoku[box]), box)

    length, box = min(map(calculate_box_length, filter(unsolved_box, BOXES)))

    return box


def create_possibility_tree(sudoku):
    """
    Args:
        sudoku (dict): Partially solved Sudoku puzzle

    Returns:
        list: Possible solutions picking the best current box

    """

    best_box = find_best_candidate_box(sudoku)
    paths = []

    for best_current_choice in sudoku[best_box]:
        new_sudoku = sudoku.copy()
        new_sudoku[best_box] = best_current_choice
        paths.append(new_sudoku)

    return paths


def search(sudoku):
    """
    Args:
        sudoku(dict): Puzzle

    Returns:
        dict: Partially or totally solved sudoku

    """

    sudoku = reduce_puzzle(sudoku)

    if sudoku is False:
        return False

    if sudoku_is_solved(sudoku):
        return sudoku

    for tree in create_possibility_tree(sudoku):
        attempt = search(tree)

        if attempt:
            return attempt

    return False


def solve(grid):
    """
    Find the solution to a Sudoku grid.

    Args:
        grid (string): a string representing a sudoku grid.

            Example:
            '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns:
        dict: The dictionary representation of the final sudoku grid. False if no solution exists.

    """

    return search(grid_values(grid))


def main():
    """
    Run Sudoku solver program
    """

    display(solve(DIAGONAL_SUDOKU))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass

    except ModuleNotFoundError:
        print('We could not visualize your board due to a pygame issue.')
        print('Not a problem! It is not a requirement.')

if __name__ == '__main__':
    main()
