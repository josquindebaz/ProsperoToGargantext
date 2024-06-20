import glob
import os.path
def get_values_from_ctx(ctx_path):
    with open(ctx_path, 'r') as buf_ctx:
        lines = buf_ctx.readlines()

    return {
        "title": lines[1].strip(),
        "author": lines[2].strip(),
        "date": lines[5].strip(),
    }


if __name__ == "__main__":
    txts = glob.glob("test_streamlit/*.txt")

    for txt in txts:
        rac = os.path.splitext(txt)
        ctx_path = rac[0] + '.ctx'

        if os.path.isfile(ctx_path):
            print(txt)
            print(get_values_from_ctx(ctx_path))
