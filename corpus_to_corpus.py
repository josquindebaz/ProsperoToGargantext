import csv
import glob
import os.path


def get_values_from_files(txt_path, ctx_path):
    with open(ctx_path, 'r') as buf_ctx:
        lines = buf_ctx.readlines()

    values = get_ctx_values(lines)

    with open(txt_path, 'r') as buf_txt:
        values['abstract'] = buf_txt.read()

    return values


def get_ctx_values(lines):
    values = {
        "title": lines[1].strip(),
        "authors": lines[2].strip(),
        "date": lines[5].strip(),
        "source": lines[6].strip(),
    }

    return values


def format_csv(values):
    day, month, year = values["date"].split("/")

    return [day,
            month,
            year,
            values['authors'],
            values['source'],
            values['title'],
            values['abstract']
            ]


def to_csv(lines, target_file):
    with open(target_file, "w", newline='') as csv_file:
        header = ["Publication Day",
                  "Publication Month",
                  "Publication Year",
                  "Authors",
                  "Title",
                  "Source",
                  "Abstract"]

        writer = csv.writer(csv_file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for line in lines:
            writer.writerow(line)


if __name__ == "__main__":
    dir_path = "test_streamlit/*.txt"
    txts = glob.glob(dir_path)
    lines = []
    for txt_path in txts:
        rac = os.path.splitext(txt_path)
        ctx_path = rac[0] + '.ctx'

        if os.path.isfile(ctx_path):
            values = get_values_from_files(txt_path, ctx_path)
            lines.append(format_csv(values))
    if lines:
        to_csv(lines,
               target_file="samples/test_streamlit.csv")
