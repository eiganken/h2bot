import database as db


def run(props):
    result = db.get_col_values_of('creator_id')
    creators = [row[0] for row in result]
    return to_string(creators)

def to_string(result_raw):
    s = ""
    for creator in result_raw:
        s += "@" + creator + "\n"
    return s