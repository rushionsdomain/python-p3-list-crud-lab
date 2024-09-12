def create_an_empty_list():
    """Creates and returns an empty list."""
    return []

def create_a_list():
    """Creates and returns a list of length 4."""
    return [1, 2, 3, 4]

def add_element_to_end_of_list(lst, element):
    """Adds an element to the end of a list."""
    lst.append(element)
    return lst

def add_element_to_start_of_list(lst, element):
    """Adds an element to the start of a list."""
    lst.insert(0, element)
    return lst

def remove_element_from_end_of_list(lst):
    """Removes an element from the end of a list."""
    if lst:  # Ensure the list is not empty
        lst.pop()
    return lst

def remove_element_from_start_of_list(lst):
    """Removes an element from the start of a list."""
    if lst:  # Ensure the list is not empty
        lst.pop(0)
    return lst

def retrieve_first_element_from_list(lst):
    """Retrieves the first element from a list."""
    if lst:  # Ensure the list is not empty
        return lst[0]
    return None

def retrieve_element_from_index(lst, index):
    """Retrieves an element from a list by its index."""
    return lst[index] if 0 <= index < len(lst) else None

def retrieve_last_element_from_list(lst):
    """Retrieves the last element from a list."""
    if lst:  # Ensure the list is not empty
        return lst[-1]
    return None
