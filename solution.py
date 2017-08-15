assignments = []


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


def cross(rows, cols):
    """
    Cross product of elements in rows and elements in cols.

    Args:
        rows (list): a list of rows
        cols (list): a list of columns


    Returns:
        dict: vectorial product of rows x columns

    """
    pass


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

    pass


def display(sudoku):
    """
    Display the values as a 2-D grid.

    Args:
        sudoku (dict): The sudoku in dictionary form

    """

    pass


def eliminate(sudoku):
    """
    Go through all the boxes, and whenever there is a box with a value,
    eliminate this value from the values of all its peers.

    Args:
        sudoku (dict): Partially or totally solved sudoku puzzle

    Returns:
        dict: Sudoku with values eliminated of all its peers

    """

    pass


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
    pass


def reduce_puzzle(sudoku):
    """
    Reduce number of unsolved boxes in the sudoku

    Args:
        sudoku (dict): Partially solved sudoku puzzle

    Returns:
        dict: Partially or totally solved puzzle

    """

    pass


def search(sudoku):
    """
    Args:
        sudoku(dict): Puzzle

    """

    pass


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

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass

    except:
        print('We could not visualize your board due to a pygame issue.')
        print('Not a problem! It is not a requirement.')
