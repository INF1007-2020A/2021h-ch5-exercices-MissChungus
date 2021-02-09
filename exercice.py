#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return number*-1
    else:
        return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    return [(prefixes[i]+suffixe) for i in range(len(prefixes))]


def prime_integer_summation() -> int:
    nb_premiers = 1
    somme = 2
    nombre = 3
    while nb_premiers < 100:
        for i in range(2, int(nombre**0.5 + 1)):
            if nombre % i == 0:
                nombre += 1
                break
        else:
            nb_premiers += 1
            somme += nombre
            nombre += 1
    return somme


def factorial(number: int) -> int:
    factorielle = 1
    while number > 1:
        factorielle *= number
        number -= 1
    return factorielle


def use_continue() -> None:
    for i in range(1,11):
        if i == 5:
            continue
        print(i)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    liste_finale = [True for groupe in groups]
    for i in range(len(groups)):
        if len(groups[i]) > 10 or len(groups[i]) <= 3:
            liste_finale[i] = False
            continue
        for i2 in range(len(groups[i])):
            if groups[i][i2] == 25:
                liste_finale[i] = True
                break
            elif groups[i][i2] < 18:
                liste_finale[i] = False
            elif groups[i][i2] > 70:
                for i3 in range(len(groups[i])):
                    if groups[i][i3] == 50:
                        liste_finale[i] = False
    return liste_finale


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
