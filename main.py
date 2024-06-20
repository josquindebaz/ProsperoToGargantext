import glob
import os.path


def get_values_from_ctx(txt_path, ctx_path):
    with open(ctx_path, 'r') as buf_ctx:
        lines = buf_ctx.readlines()

    values = {
        "title": lines[1].strip(),
        "authors": lines[2].strip(),
        "date": lines[5].strip(),
    }

    with open(txt_path, 'r') as buf_txt:
        values['abstract'] = buf_txt.read()

    return values

def format_csv(line):
    day, month, year = values["date"].split("/")
    return f"{day}\t{month}\t{year}\t{values['authors']}\t{values['title']}\t\t{values['abstract']}"

def to_csv(lines):
    with open("test.csv", "w") as csvFile:
        for line in lines:
            csvFile.write(line+"\n")


if __name__ == "__main__":
    txts = glob.glob("test_streamlit/*.txt")
    lines = []
    for txt_path in txts:
        rac = os.path.splitext(txt_path)
        ctx_path = rac[0] + '.ctx'

        if os.path.isfile(ctx_path):
            values = get_values_from_ctx(txt_path, ctx_path)
            lines.append(format_csv(values))
    if lines:
        to_csv(lines)