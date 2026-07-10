Title: Emberwild Trial — GameCharacter Design Document
---
1. Game Concept
A short, single‑encounter elemental trial where the player summons a companion creature and faces one opponent. The goal is to defeat the opponent using either a basic attack or an elemental skill.
---
2. Elemental Tribes
Fire Tribe
• Aggressive, impulsive
• Bonus: +2 damage vs Earth
• Weakness: +2 damage taken from Water
• Skill: Flame Burst (+2 damage)
Water Tribe
• Adaptive, fluid
• Bonus: +2 damage vs Fire
• Weakness: +2 damage taken from Storm
• Skill: Tide Push (+2 damage)
Earth Tribe
• Sturdy, defensive
• Bonus: -2 incoming damage from Storm
• Weakness: +2 damage taken from Fire
• Skill: Stone Guard (reduces incoming damage by 2)
Storm Tribe
• Chaotic, fast
• Bonus: +2 damage vs Water
• Weakness: +2 damage taken from Earth
• Skill: Shock Pulse (+2 damage)
---
3. Actions
Generic Attack
• Uses attack_power
• No bonuses
• Same for all creatures
• Shows consistent class behavior
Elemental Skill
• Uses elemental bonuses
• Unique to each tribe
• Shows specialized class behavior
---
4. Win Condition
Single Encounter
Player wins if the opponent’s health reaches zero.
Player loses if their companion’s health reaches zero.
---
5. Class Structure
Class: GameCharacter
Attributes:
• name
• element
• health
• attack_power
Methods:
• attack(target)
• elemental_skill(target)
• take_damage(amount)
• apply_elemental_bonus(target)
• heal(amount) (optional)
• is_defeated()
• print_status()
---
6. Exception Types
Built‑in
• ValueError → invalid numeric input
• TypeError → attacking non‑GameCharacter
• KeyError → invalid element selection
Custom
• CharacterDefeatedError → health drops below zero
---
7. Encounter Flow
main()
1. Print intro
2. Ask user to create companion
3. Validate inputs with try/except
4. Create opponent
5. Ask user to choose action
6. Resolve action
7. Catch exceptions
8. Print outcome
---
8. Opponent Stats (example)
You can choose these later, but here’s a simple baseline:
• Name: “Stormbeast”
• Element: “storm”
• Health: 10
• Attack Power: 4