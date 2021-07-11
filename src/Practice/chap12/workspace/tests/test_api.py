import unittest
import sys
import json
from io import StringIO
from unittest.mock import patch, MagicMock


class BuildUrlTest(unittest.TestCase):
    def test_build_url(self):
        # build_url()がテスト対象の処理
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?q=python'
        actual = build_url({'q': 'python'})
        self.assertEqual(expected, actual)

    def test_build_url_multi(self):
        from booksearch.api import build_url
        base = 'https://www.googleapis.com/books/v1/volumes?'

        params = (
            (f'{base}q=python', {'q': 'python'}),
            (f'{base}q=python&maxResults=1',
             {'q': 'python', 'maxResults': 1}),
            (f'{base}q=python&langRestrict=en', {
             'q': 'python', 'langRestrict': 'en'}),
        )
        for expected, param in params:
            with self.subTest(**param):
                actual = build_url(param)
                self.assertEqual(expected, actual)

    def test_build_url_empty_param(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes?'
        actual = build_url({})
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_build_url_fail(self):
        from booksearch.api import build_url
        expected = 'https://www.googleapis.com/books/v1/volumes'
        actual = build_url({})
        self.assertEqual(expected, actual, msg='このテストは失敗します。')

    @unittest.skip('this isa skip test example')
    def test_nothing_skip(self):
        pass

    @unittest.skipIf(sys.version_info > (3, 6), 'this is a skipIf test')
    def test_nothing_skipIf(self):
        pass

    def test_get_json(self):
        from booksearch.api import get_json
        with patch('booksearch.api.request.urlopen') as mock_urlopen:
            expected_response = {'id': 'test'}
            fp = StringIO(json.dumps(expected_response))

            mock = MagicMock()
            mock.__enter__.return_value = fp
            mock_urlopen.return_value = mock
            actual = get_json({'q': 'python'})
            self.assertEqual(expected_response, actual)
