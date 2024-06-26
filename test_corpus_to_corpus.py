from unittest import TestCase

from corpus_to_corpus import get_values_from_files, extract_ctx_values, format_csv_line, txt_and_ctx, \
    get_valid_txt_and_ctx_list


class Test(TestCase):
    def test_get_values_from_ctx(self):
        txt_path = "samples/TWIT22414A.txt"
        ctx_path = "samples/TWIT22414A.ctx"
        expected = {'title': 'Posts de MichelF29015597',
                    'authors': 'MichelF29015597',
                    'date': '14/04/2022',
                    'source': 'X/Twitter',
                    'abstract': 'Vous je ne sais pas, mais moi, voir des jeunes de 18 ans manifester contre la retraite à 65 ou 64 ans,\nje me dis que la vie ne sera pas forcément facile pour eux.'}

        result = get_values_from_files(txt_path, ctx_path)

        assert result == expected

    def test_get_ctx_values(self):
        ctx_lines_buffer = ['fileCtx0005\n',
                            'Posts de MichelF29015597\n',
                            'MichelF29015597\n',
                            '\n',
                            '\n',
                            '14/04/2022\n',
                            'X/Twitter\n',
                            'tweet\n',
                            '\n',
                            '\n',
                            '\n',
                            'Processed by Tiresias on 2024-05-29 15:38:27\n',
                            '\n',
                            'n\n',
                            'n\n',
                            '12:30:12']

        result = extract_ctx_values(ctx_lines_buffer)

        assert result == {'title': 'Posts de MichelF29015597',
                          'authors': 'MichelF29015597',
                          'date': '14/04/2022',
                          'source': 'X/Twitter'}

    def test_format_csv_line(self):
        values = {'title': 'Posts de MichelF29015597',
                  'authors': 'MichelF29015597',
                  'date': '14/04/2022',
                  'source': 'X/Twitter',
                  'abstract': 'Vous je ne sais pas, mais moi, voir des jeunes de 18 ans manifester contre la retraite à 65 ou 64 ans,\nje me dis que la vie ne sera pas forcément facile pour eux.'}

        expected = ['14',
                    '04',
                    '2022',
                    'MichelF29015597',
                    'X/Twitter',
                    'Posts de MichelF29015597',
                    'Vous je ne sais pas, mais moi, voir des jeunes de 18 ans manifester contre la retraite à 65 ou 64 ans,\nje me dis que la vie ne sera pas forcément facile pour eux.']

        result = format_csv_line(values)

        assert result == expected

    def test_txt_and_ctx(self):
        txt_path = "samples/TWIT22414A.txt"
        ctx_path = "samples/TWIT22414A.ctx"
        expected = [txt_path, ctx_path]

        result = txt_and_ctx(txt_path)

        assert result == expected

        result = txt_and_ctx("missing_ctx.txt")
        assert result is None

    def test_get_valid_txt_and_ctx_list(self):
        txt_list = ["samples/TWIT22414A.txt", "samples/TWIT22414MR.txt", "missing_ctx.txt"]
        expected = [['samples/TWIT22414A.txt', 'samples/TWIT22414A.ctx'], ['samples/TWIT22414MR.txt', 'samples/TWIT22414MR.ctx']]

        result = get_valid_txt_and_ctx_list(txt_list)

        assert result == expected