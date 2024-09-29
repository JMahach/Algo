# https://leetcode.com/problems/find-the-town-judge/description/
# flake8: noqa


def find_judge(n, trust):
    if n == 1:
        return 1
    entity_trust_counter = {}
    individual_trust_counter = {}
    for el in trust:
        entity_trust_counter[el[1]] = entity_trust_counter.get(el[1], 0) + 1
        individual_trust_counter[el[0]] = individual_trust_counter.get(el[0], 0) + 1

    for person, trusts_count in entity_trust_counter.items():
        if trusts_count == n - 1 and not individual_trust_counter.get(person):
            return person
    return -1
