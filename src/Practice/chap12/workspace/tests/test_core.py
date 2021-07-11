import pathlib
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch
from urllib.error import URLError

THUMBNAIL_URL = (
    'http://books.google.com/books/content'
    '?id=OgtBw760Y5EC&printsec=frontcover'
    '&img=1&zoom=1&edge=curl&source=gbs_api'
)


class SaveThumbnailsTest(unittest.TestCase):
    def setUp(self) -> None:
        # 一時ディレクトリを作成する
        self.tmp = TemporaryDirectory()

    def tearDown(self) -> None:
        # 一時ディレクトリを片づける
        self.tmp.cleanup()

    @patch('booksearch.core.get_data')
    def test_save_thumbnails(self, mock_get_data):
        from booksearch.core import Book

        data_path = pathlib.Path(__file__).with_name('data')
        mock_get_data.return_value = (
            data_path / 'iLrrDwAAQBAJ_thumbnail.jpeg').read_bytes()

        book = Book({'id': '', 'volumeInfo': {
            'imageLinks':  {
                'thumbnail': THUMBNAIL_URL
            }}})

        # 処理を実行し、ファイルが作成される事を確認する
        filename = book.save_thumbnails(self.tmp.name)[0]

        mock_get_data.assert_called_with(THUMBNAIL_URL)
        self.assertTrue(pathlib.Path(filename).exists())

    def test_get_books_no_connection(self):
        from booksearch.core import get_books

        with patch('socket.socket.connect') as mock:
            mock.return_value = None
            with self.assertRaisesRegex(URLError, 'urlopen error'):
                get_books(q='python')
