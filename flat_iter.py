class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.inner_cursor = 0
        return self

    def __next__(self):
        if self.cursor == len(self.list_of_lists):
            raise StopIteration

        l = len(self.list_of_lists[self.cursor])
        if l > 1:
            item = self.list_of_lists[self.cursor][self.inner_cursor]
            self.inner_cursor += 1
            if self.inner_cursor == l:
                self.inner_cursor = 0
                self.cursor += 1
            return item
        else:
            item = self.list_of_lists[self.cursor]
            self.cursor += 1
            return item



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()