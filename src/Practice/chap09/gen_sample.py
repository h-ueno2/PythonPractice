def reader(src):
    """ファイルの中身を1行ずつ読み込む
    """
    with open(src) as f:
        for line in f:
            yield line


def convert(line):
    """行単位で変換する
    """
    return line.upper()


def writer(dest, reader):
    with open(dest, 'w') as f:
        for line in reader:
            f.write(convert(line))


writer('dest.txt', reader('src.txt'))
