
Code no solve world hunger alone. Big problem need food, peace, roads, money, fair rule. But code help send food to places with biggest need first.

```python
from dataclasses import dataclass


@dataclass
class Region:
    name: str
    people_in_need: int
    food_available: int = 0


def allocate_food(regions: list[Region], total_food: int) -> dict[str, int]:
    allocation = {region.name: 0 for region in regions}

    # Place with more hungry people get food first.
    regions_by_need = sorted(
        regions,
        key=lambda region: region.people_in_need - region.food_available,
        reverse=True,
    )

    for region in regions_by_need:
        unmet_need = max(0, region.people_in_need - region.food_available)
        food_given = min(unmet_need, total_food)

        allocation[region.name] = food_given
        total_food -= food_given

        if total_food == 0:
            break

    return allocation


def main() -> None:
    regions = [
        Region("North Village", people_in_need=5000, food_available=1200),
        Region("River Town", people_in_need=3000, food_available=400),
        Region("Dry Plains", people_in_need=8000, food_available=1000),
    ]

    food_units = 9000
    plan = allocate_food(regions, food_units)

    print("Food plan:")
    for region_name, amount in plan.items():
        print(f"{region_name}: {amount} food units")


if __name__ == "__main__":
    main()
```

Real system need good data, nutrition units, transport cost, spoilage, local leaders, and fair checks.

