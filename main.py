from typing import Dict, List


def input_visitors() -> Dict[str, List[str]]:
    """
    Frågar användaren efter deltagare och vilka andra deltagare
    de inte kan sitta med.

    :return:
    En ordbok där nycklar är deltagarens namn och värdet
    är en lista med namn som de inte fungerar med.
    """
    result: Dict[str, List[str]] = {}

    while True:
        new_visitor = input('Deltagare: ').strip()
        if not new_visitor:
            print('Namn kan inte vara tomt.')
            continue

        # Kontrollera om new_visitor redan finns i listan
        if new_visitor in result:
            print('Deltagaren finns redan, ange nytt namn.')
            continue

        not_visitor = input('Ange namn separerade med kommatecken: ')

        # Dela upp, trimma, och filtrera bort tomma poster
        not_visitors = [name.strip() for name in not_visitor.split(',') if name.strip()]

        result[new_visitor] = not_visitors

        if input('Mera besökare (j/n): ').strip().lower() == "n":
            break

    return result


def place_visitors(visitors: Dict[str, List[str]]) -> Dict[str, List[str]]:
    table: Dict[str, List[str]] = {}
    # Placera ut en i taget till ledigt bord
    for new_visitor in visitors.keys():
        print(new_visitor)
    return table


if __name__ == '__main__':
    visitor_dict = input_visitors()
    print(visitor_dict)
    table_dict = place_visitors(visitor_dict)
    print(table_dict)
