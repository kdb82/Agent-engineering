USER: Five houses stand in a row, numbered 1 to 5 from left to right. Each house has one resident, one pet and one favorite drink, and no two houses share any of them.

People: Ava, Ben, Cara, Dev, Eli
Pets: bird, cat, dog, fish, rabbit
Drinks: coffee, juice, milk, tea, water

Clues:

The milk drinker lives in the middle house.
Cara lives in one of the end houses.
Ben lives next door to Cara.
Dev lives somewhere to the left of Eli.
The cat owner lives immediately to the right of Ava.
The rabbit owner lives immediately to the left of the dog owner.
The bird owner does not live in an end house.
The dog owner lives immediately to the right of the coffee drinker.
The fish owner drinks water.
The bird owner drinks neither coffee nor juice.
The tea drinker lives next door to the water drinker.
The juice drinker lives in an end house.
Dev owns neither the cat nor the rabbit.

Question: Who lives in each house, and what pet and drink goes with each house? Explain your reasoning step by step.

AGENT: The solution is:

| House | Resident | Pet | Drink |
|---|---|---|---|
| 1 | Dev | fish | water |
| 2 | Ava | bird | tea |
| 3 | Eli | cat | milk |
| 4 | Ben | rabbit | coffee |
| 5 | Cara | dog | juice |

### Reasoning

1. **Cara is at an end, and Ben is next to Cara.**  
   Therefore, either:
   - Cara is in house 1 and Ben in house 2, or
   - Cara is in house 5 and Ben in house 4.

2. **The milk drinker is in house 3.**

3. The rabbit is immediately left of the dog, and the dog is immediately right of the coffee drinker.  
   Thus, the rabbit and coffee drinker occupy the same house, immediately left of the dog.

4. The dog cannot be in house 4, because then the coffee drinker would be in house 3—but house 3 drinks milk.

5. If the dog were in house 2, the rabbit and coffee would be in house 1. The remaining drinks would force tea and water into nonadjacent houses, so this is impossible.

6. If the dog were in house 3, then:
   - rabbit and coffee would be in house 2,
   - milk would be in house 3,
   - juice would have to be in house 1,
   - tea and water would be in houses 4 and 5.

   Checking the possible resident arrangements leads to either a fish drinking juice or the bird being in an end house, both contradictions. Therefore, the dog is not in house 3.

7. Hence, **the dog is in house 5**, with:
   - rabbit in house 4,
   - coffee in house 4,
   - milk in house 3.

8. Juice must be in an end house. Since houses 1 and 2 must contain adjacent tea and water, juice cannot be in house 1. Therefore:
   - house 5 drinks juice,
   - houses 1 and 2 drink water and tea.

9. Cara cannot be in house 1, because then Ben would be in house 2 and there would be no possible place for Ava’s cat without conflicting with the rabbit or dog. Thus:
   - Cara is in house 5,
   - Ben is in house 4.

10. The remaining residents are Ava, Dev, and Eli in houses 1–3. Since Dev is left of Eli and Ava must be immediately left of the cat:
    - Ava is in house 2,
    - the cat is in house 3,
    - Dev is in house 1,
    - Eli is in house 3.

11. The remaining pets in houses 1 and 2 are bird and fish. The bird cannot be in an end house, so:
    - house 2 has the bird,
    - house 1 has the fish.

12. The fish drinks water, so house 1 is water and house 2 is tea.

Therefore, the completed arrangement is:

**Dev–fish–water, Ava–bird–tea, Eli–cat–milk, Ben–rabbit–coffee, Cara–dog–juice.**
