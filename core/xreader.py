import re


class XReader(object):

    def __init__(self, path, mode: str = 'r', chunk_size: int = 1000):
        self.file_path = path
        self._chunk_size = chunk_size
        self._mode = mode
        self.open_file = open(self.file_path, self._mode)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open_file.close()

    def readlines(self):
        """
        return each line from file lazy
        :return:
        """
        last_piece_line = ''
        while True:
            from_file = self.open_file.read(self._chunk_size)
            part = "{}{}".format(last_piece_line and last_piece_line[0] or '', from_file)

            lines = [l.strip() for l in re.findall('[^\n]+(?=.+\n)', part)]
            last_piece_line = re.search('\n[^\n]+(\n)?(?=\n|)$|^[^\n]+$', part)
            for line in lines[:-1]:
                yield line
            if not from_file:
                break

    def read_all_lines(self):
        """
        Return list of all lines
        :return:
        """
        return self.open_file.readlines()
