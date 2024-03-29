from linked_list import LinkedList


def sum_linked_lists(first_list: LinkedList, second_list: LinkedList):
    if first_list.len() != second_list.len():
        return None

    summarized_list = []
    node_from_first_list = first_list.head
    node_from_second_list = second_list.head

    while node_from_first_list is not None:
        summarized_list.append(node_from_first_list.value + node_from_second_list.value)

        node_from_first_list = node_from_first_list.next
        node_from_second_list = node_from_second_list.next
    return summarized_list
