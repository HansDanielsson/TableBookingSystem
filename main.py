from typing import Dict, List, Set

MAX_PER_TABLE = 4


def input_visitors() -> Dict[str, Set[str]]:
    """
    Frågar användaren efter deltagare och vilka andra deltagare
    de inte kan sitta med.

    :return:
    En ordbok där nycklar är deltagarens namn och värdet
    är en set med namn som de inte fungerar med.
    """
    visitors: Dict[str, Set[str]] = {}

    while True:
        name = input('Deltagare: ').strip()
        if not name:
            print('Namn kan inte vara tomt.')
            continue

        if name in visitors:
            print('Deltagaren finns redan, ange nytt namn.')
            continue

        conflicts = input('Ange namn separerade med kommatecken: ')

        # Dela upp, trimma, och filtrera bort tomma poster
        conflict_set = {c.strip() for c in conflicts.split(',') if c.strip()}

        visitors[name] = conflict_set

        if input('Mera besökare (j/n): ').strip().lower() == "n":
            break

    return visitors


def can_sit(visitor: str, table: List[str], conflicts: Dict[str, Set[str]]) -> bool:
    """
    Hjälprutin:
    Kontrollera om visitor kan sitta vid bordet.
    """
    return all(visitor not in conflicts.get(person, set()) and
               person not in conflicts.get(visitor, set())
               for person in table
               )


def place_visitors(visitors: Dict[str, Set[str]]) -> Dict[int, List[str]]:
    """
    Placera deltagare vid bord (max 4 per bord)
    med hänsyn till konflikter.
    :param visitors:
    :return: tables
    """
    tables: Dict[int, List[str]] = {}

    for visitor in visitors:
        placed = False

        for table in tables.values():
            if len(table) < MAX_PER_TABLE and can_sit(visitor, table, visitors):
                table.append(visitor)
                placed = True
                break

        if not placed:
            tables[len(tables) + 1] = [visitor]

    return tables


def print_tables(tables: Dict[int, List[str]]) -> None:
    for table_number, people in tables.items():
        print(f'Table {table_number}:', ', '.join(people))


if __name__ == '__main__':
    print_tables(place_visitors(input_visitors()))
