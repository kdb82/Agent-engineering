from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Place:
    name: str
    food: int
    need: int


def share_food(places: List[Place]) -> Dict[str, Dict[str, int]]:
    """
    Make simple food-sharing plan.
    Food and need measured in meal units.
    """

    hungry = [p for p in places if p.need > p.food]
    plenty = [p for p in places if p.food > p.need]

    plan = {}

    for source in plenty:
        extra_food = source.food - source.need

        for target in hungry:
            missing_food = target.need - target.food
            send_food = min(extra_food, missing_food)

            if send_food > 0:
                plan.setdefault(source.name, {})
                plan[source.name][target.name] = send_food

                source.food -= send_food
                target.food += send_food
                extra_food -= send_food

            if extra_food == 0:
                break

    return plan


def show_result(places: List[Place], plan: Dict[str, Dict[str, int]]) -> None:
    print("Food plan:")

    if not plan:
        print("No food move needed.")
        return

    for source, targets in plan.items():
        for target, amount in targets.items():
            print(f"{source} send {amount} meals to {target}")

    print("\nAfter food move:")

    for place in places:
        if place.food >= place.need:
            print(f"{place.name}: enough food")
        else:
            short = place.need - place.food
            print(f"{place.name}: still need {short} meals")


places = [
    Place("Green Valley", food=1000, need=600),
    Place("Dry Plain", food=200, need=700),
    Place("River Town", food=500, need=450),
    Place("Dust Village", food=100, need=500),
]

plan = share_food(places)
show_result(places, plan)