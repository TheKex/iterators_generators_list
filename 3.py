class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.index = -1
        self.inner_list = []
        return self

    def __next__(self):
        if len(self.inner_list) > 0:
            return self.inner_list.pop(0)
        self.index += 1
        if self.index >= len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.index]

        if isinstance(item, list):
            self.inner_list = list(FlatIterator(item))
            while len(self.inner_list) == 0:
                self.index += 1
                if self.index >= len(self.list_of_list):
                    raise StopIteration
                item = self.list_of_list[self.index]
                if item is None:
                    return None
                if isinstance(item, list):
                    self.inner_list = list(FlatIterator(item))
            if len(self.inner_list) > 0:
                return self.inner_list.pop(0)
        else:
            return self.list_of_list[self.index]


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_3()
