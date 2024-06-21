from unittest import TestCase

from main import get_values_from_files, get_ctx_values, format_csv


class Test(TestCase):
    def test_get_values_from_ctx(self):
        txt_path = "test_streamlit/TWIT22414A.txt"
        ctx_path = "test_streamlit/TWIT22414A.ctx"
        expected = {'title': 'Posts de MichelF29015597', 'authors': 'MichelF29015597', 'date': '14/04/2022',
                    'abstract': 'Posts de MichelF29015597\n.\nVous je ne sais pas, mais moi, voir des jeunes de 18 ans manifester contre la retraite à 65 ou 64 ans,\nje me dis que la vie ne sera pas forcément facile pour eux.'}

        result = get_values_from_files(txt_path, ctx_path)

        assert result == expected

    def test_get_ctx_values(self):
        ctx_lines_buffer = ['fileCtx0005\n', 'Posts de MichelF29015597\n', 'MichelF29015597\n', '\n', '\n',
                            '14/04/2022\n', 'Test\n', 'test\n', '\n', '\n', '\n',
                            'Processed by Tiresias on 2024-05-29 15:38:27\n', '\n', 'n\n', 'n\n', '12:30:12']

        result = get_ctx_values(ctx_lines_buffer)

        assert result == {'title': 'Posts de MichelF29015597', 'authors': 'MichelF29015597', 'date': '14/04/2022'}

    def test_format_csv(self):
        values = {'title': 'Posts de MichelF29015597', 'authors': 'MichelF29015597', 'date': '14/04/2022',
                    'abstract': 'Posts de MichelF29015597\n.\nVous je ne sais pas, mais moi, voir des jeunes de 18 ans manifester contre la retraite à 65 ou 64 ans,\nje me dis que la vie ne sera pas forcément facile pour eux.'}

        expected = ['14', '04', '2022', 'MichelF29015597', 'Posts de MichelF29015597', 'Posts de MichelF29015597\n.\nVous je ne sais pas, mais moi, voir des jeunes de 18 ans manifester contre la retraite à 65 ou 64 ans,\nje me dis que la vie ne sera pas forcément facile pour eux.']

        result = format_csv(values)

        assert result == expected