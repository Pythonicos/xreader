from unittest import TestCase

from core.xreader import XReader


class ReadTest(TestCase):
    def test_read_file__return_lines_lazy(self):
        # fixture
        reader = XReader('teste.txt', chunk_size=2)

        # test
        lines = []
        for line in reader.readlines():
            lines.append(line)

        # assert
        self.assertEqual(4, len(lines))
