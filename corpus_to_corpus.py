import csv
import glob
import os


def get_values_from_files(txt_path, ctx_path):
    with open(ctx_path, 'r') as buf_ctx:
        lines = buf_ctx.readlines()

    values = extract_ctx_values(lines)

    with open(txt_path, 'r') as buf_txt:
        values['abstract'] = buf_txt.read()

    return values


def extract_ctx_values(lines):
    values = {
        "title": lines[1].strip(),
        "authors": lines[2].strip(),
        "date": lines[5].strip(),
        "source": lines[6].strip(),
    }

    return values


def format_csv_line(values):
    day, month, year = values["date"].split("/")

    return [
        day,
        month,
        year,
        values['authors'],
        values['source'],
        values['title'],
        values['abstract']
    ]


def to_csv(lines, target_file):
    with open(target_file, "w", newline='') as csv_file:
        writer = csv.writer(csv_file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)

        header = ["Publication Day",
                  "Publication Month",
                  "Publication Year",
                  "Authors",
                  "Title",
                  "Source",
                  "Abstract"]
        writer.writerow(header)

        writer.writerows(lines)


def txt_and_ctx(txt_path):
    """
    Returns a pair [.txt, .ctx] from .txt when .ctx exists
    """
    ctx_path = os.path.splitext(txt_path)[0] + '.ctx'
    if os.path.isfile(ctx_path):
        return [txt_path, ctx_path]


def get_valid_txt_and_ctx_list(txt_list):
    return [
        txt_and_ctx(txt) for txt in txt_list if txt_and_ctx(txt)
    ]


def files_to_lines(txt_list):
    """
    Returns rows with content when .txt has an associated .ctx
    """
    return [
        format_csv_line(get_values_from_files(txt_path, ctx_path))
        for txt_path, ctx_path
        in get_valid_txt_and_ctx_list(txt_list)
    ]


def corpus_from_directory(target):
    """
    Create a Gargantext corpus from .txt and .ctx in target directory
    """

    txt_list = glob.glob(target + "/*.txt")
    gargantext_lines = files_to_lines(txt_list)

    if gargantext_lines:
        to_csv(gargantext_lines,
               target_file=os.path.join(target, "gargantext_from_prospero.csv"))


if __name__ == "__main__":
    dir_path = "samples"
    corpus_from_directory(dir_path)
