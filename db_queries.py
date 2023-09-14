import sqlite3


def create_md(tb: list[tuple[str, str | None]]):
    """header, delimiter, body"""
    h, d, b = "| name_product | name_category |", f"\n|-|-|\n", "\n".join(f'|{np} | {nc}|' for np, nc in tb)
    result = f"{h}{d}{b}"
    open('select_prots_cats.md', 'w').write(result)


with sqlite3.connect('my_db.sqlite3') as conn:
    cur = conn.cursor()

    # init db
    cur.executescript(open('script_db.sql').read())
    # select Имя продукта – Имя категории
    cur.execute(open('select_prots_cats.sql').read())

    table = cur.fetchall()
    create_md(table)
