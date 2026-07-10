import random

# Create Game Characters
class GameCharacter:
    """A character in the Emberwild Trial game with elemental abilities."""
    
    def __init__(self, name, element, health=15, attack_power=5):
        """
        Initialize a GameCharacter.
        
        Args:
            name (str): Character's name
            element (str): Element tribe ('fire', 'water', 'earth', 'storm')
            health (int): Character's health points (default 15)
            attack_power (int): Character's base attack damage (default 5)
        
        Raises:
            KeyError: If element is not a valid tribe
            ValueError: If health or attack_power are not positive integers
        """
        if element.lower() not in ELEMENTAL_TRIBES:
            raise KeyError(f"'{element}' is not a valid tribe. Choose from: {list(ELEMENTAL_TRIBES.keys())}")
        
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")
        
        if not isinstance(attack_power, int) or attack_power <= 0:
            raise ValueError("Attack power must be a positive integer")
        
        self.name = name
        self.element = element.lower()
        self.health = health
        self.attack_power = attack_power
    
    def print_status(self):
        """Display character's current status."""
        tribe_info = ELEMENTAL_TRIBES[self.element]
        print(f"\n--- {self.name} ({self.element.upper()}) ---")
        print(f"Personality: {tribe_info['personality']}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Special Skill: {tribe_info['skill']['name']}")
    
    def is_defeated(self):
        """Check if character is defeated (health <= 0)."""
        return self.health <= 0
    
    def take_damage(self, amount):
        """Reduce health by damage amount."""
        self.health -= amount
    
    def attack(self, target):
        """
        Perform a basic attack on target character.
        
        Args:
            target (GameCharacter): The target to attack
        
        Raises:
            TypeError: If target is not a GameCharacter instance
        """
        if not isinstance(target, GameCharacter):
            raise TypeError(f"Can only attack GameCharacter instances, not {type(target).__name__}")
        
        damage = self.attack_power
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
    
    def elemental_skill(self, target):
        """
        Perform an elemental skill attack on target character.
        
        Args:
            target (GameCharacter): The target to attack
        
        Raises:
            TypeError: If target is not a GameCharacter instance
        """
        if not isinstance(target, GameCharacter):
            raise TypeError(f"Can only attack GameCharacter instances, not {type(target).__name__}")
        
        tribe_info = ELEMENTAL_TRIBES[self.element]
        skill = tribe_info["skill"]
        
        # Base skill damage
        damage = skill.get("damage", skill.get("damage_reduction", 0))
        
        # Apply elemental bonus if target is weak to this element
        if target.element == tribe_info["bonus"]["against"]:
            damage += tribe_info["bonus"]["damage"]
            print(f"{self.name} uses {skill['name']} on {target.name} for {damage} damage! (Bonus vs {target.element}!)")
        else:
            print(f"{self.name} uses {skill['name']} on {target.name} for {damage} damage!")
        
        target.take_damage(damage)
    
    @classmethod
    def create_player_character(cls):
        """
        Prompt user to create their companion character with input validation and retries.
        
        Returns:
            GameCharacter: Player's character
        
        Raises:
            KeyError: If max retries exceeded with invalid element
        """
        print("\n=== Create Your Companion ===")
        
        # Get companion name (with validation)
        while True:
            name = input("Enter your companion's name: ").strip()
            if name:
                break
            print("✗ Name cannot be empty. Please try again.")
        
        # Get valid element with retry loop
        max_attempts = 3
        attempts = 0
        
        while attempts < max_attempts:
            print(f"\nAvailable tribes: {', '.join(ELEMENTAL_TRIBES.keys())}")
            element = input("Choose a tribe (fire/water/earth/storm): ").strip()
            
            try:
                character = cls(name, element)
                print(f"\n✓ {character.name} the {element.upper()} creature has been summoned!")
                character.print_status()
                return character
            except KeyError as e:
                attempts += 1
                if attempts < max_attempts:
                    print(f"✗ Error: {e}")
                    print(f"Attempt {attempts}/{max_attempts}. Try again.\n")
                else:
                    print(f"✗ Error: {e}")
                    print(f"Maximum attempts ({max_attempts}) reached. Exiting game...")
                    raise
    
    @classmethod
    def create_opponent(cls, player_element):
        """
        Create a random opponent with a different element than the player.
        
        Args:
            player_element (str): The player's element (to avoid duplication)
        
        Returns:
            GameCharacter: Computer-controlled opponent
        """
        available_tribes = [t for t in ELEMENTAL_TRIBES.keys() if t != player_element.lower()]
        opponent_element = random.choice(available_tribes)
        opponent_name = f"Stormbeast-{random.randint(1, 999)}"
        
        opponent = cls(opponent_name, opponent_element, health=12, attack_power=4)
        print(f"\n⚡ An opponent has appeared: {opponent.name}!")
        opponent.print_status()
        return opponent


# Elemental Tribes Dictionary
ELEMENTAL_TRIBES = {
    "fire": {
        "personality": "Aggressive, impulsive",
        "bonus": {"against": "earth", "damage": 2},
        "weakness": {"against": "water", "damage": 2},
        "skill": {
            "name": "Flame Burst",
            "damage": 2
        }
    },
    "water": {
        "personality": "Adaptive, fluid",
        "bonus": {"against": "fire", "damage": 2},
        "weakness": {"against": "storm", "damage": 2},
        "skill": {
            "name": "Tide Push",
            "damage": 2
        }
    },
    "earth": {
        "personality": "Sturdy, defensive",
        "bonus": {"against": "storm", "damage": -2},  # reduces damage taken
        "weakness": {"against": "fire", "damage": 2},
        "skill": {
            "name": "Stone Guard",
            "damage_reduction": 2
        }
    },
    "storm": {
        "personality": "Chaotic, fast",
        "bonus": {"against": "water", "damage": 2},
        "weakness": {"against": "earth", "damage": 2},
        "skill": {
            "name": "Shock Pulse",
            "damage": 2
        }
    }
} 


# Print Introduction
def print_intro():
    """Display game introduction and instructions."""
    print("\n" + "="*60)
    print("  EMBERWILD TRIAL - Elemental Battle Simulator".center(60))
    print("="*60)
    print("""
Welcome, summoner! You stand at the threshold of the Emberwild Trial.

YOUR QUEST:
Summon a companion creature and battle it against a mysterious opponent
in a single, decisive encounter. Your companion must defeat the opponent
to complete the trial!

GAMEPLAY:
• You will create your companion with a name and elemental tribe
• Your opponent will be randomly generated with a different element
• Each turn, choose to ATTACK or use an ELEMENTAL SKILL
• First character to reach 0 health loses

ACTIONS:
  1. ATTACK - Basic attack using your creature's attack power
  2. SKILL - Unleash your creature's special elemental ability

STRATEGY TIP:
Pay attention to elemental advantages! Some elements deal bonus damage
to certain opponents. Can you exploit the weaknesses?

Good luck, summoner! The trial awaits...
""")
    print("="*60 + "\n"*3)


# Function to tell character to perform an action
def perform_action(actor, opponent):
    """
    Handle player's action choice and perform the action.
    
    Args:
        actor (GameCharacter): The character performing the action
        opponent (GameCharacter): The target of the action
    
    Returns:
        bool: True if action was successful, False if invalid
    
    Raises:
        ValueError: If user input is invalid
        TypeError: If attack target is invalid
    """
    print(f"\n{actor.name}'s turn!")
    print("Choose action:")
    print("  1 - ATTACK (basic attack)")
    print("  2 - SKILL (elemental ability)")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
        
        if choice == "1":
            actor.attack(opponent)
            return True
        elif choice == "2":
            actor.elemental_skill(opponent)
            return True
        else:
            raise ValueError("Invalid choice. Please enter 1 or 2.")
    except ValueError as e:
        print(f"✗ Input Error: {e}")
        return False
    except TypeError as e:
        print(f"✗ Action Error: {e}")
        return False


def print_battle_status(player, opponent):
    """Display current status of both combatants."""
    print("\n" + "-"*60)
    print(f"{player.name} (PLAYER)".ljust(30) + f"{opponent.name} (OPPONENT)".rjust(30))
    print(f"Health: {player.health}".ljust(30) + f"Health: {opponent.health}".rjust(30))
    print("-"*60)

# Function for the main game play loop
def main():
    try:
        # 1. Print intro
        print_intro()
        
        # 2. Create user companion
        try:
            player = GameCharacter.create_player_character()
        except (KeyError, ValueError) as e:
            print(f"\n✗ Failed to create companion: {e}")
            print("Exiting game...")
            return
        
        # 3. Create opponent
        opponent = GameCharacter.create_opponent(player.element)
        
        # 4. Print face-off info
        print("\n" + "="*60)
        print("BATTLE START!".center(60))
        print("="*60)
        print_battle_status(player, opponent)
        
        # 5. Game loop - Ask user to choose action and resolve until someone is defeated
        round_count = 0
        while not player.is_defeated() and not opponent.is_defeated():
            round_count += 1
            print(f"\n--- ROUND {round_count} ---")
            
            # Player's turn
            action_valid = False
            while not action_valid:
                action_valid = perform_action(player, opponent)
            
            # Check if opponent is defeated
            if opponent.is_defeated():
                break
            
            print_battle_status(player, opponent)
            
            # Opponent's turn (simple AI - random action)
            opponent_action = random.choice(["attack", "skill"])
            print(f"\n{opponent.name}'s turn!")
            
            try:
                if opponent_action == "attack":
                    opponent.attack(player)
                else:
                    opponent.elemental_skill(player)
            except TypeError as e:
                print(f"✗ Opponent action failed: {e}")
            
            # Check if player is defeated
            if player.is_defeated():
                break
            
            print_battle_status(player, opponent)
        
        # 8. Print outcome
        print("\n" + "="*60)
        if player.is_defeated():
            print("DEFEAT!".center(60))
            print("="*60)
            print(f"\n{opponent.name} has vanquished {player.name}...")
            print("The trial was not to be. Better luck next time, summoner.")
        else:
            print("VICTORY!".center(60))
            print("="*60)
            print(f"\n{player.name} has emerged victorious!")
            print(f"{opponent.name} has been defeated in {round_count} rounds!")
            print("You have successfully completed the Emberwild Trial!")
        print("="*60 + "\n")
    
    except Exception as e:
        print(f"\n✗ Unexpected error occurred: {e}")
        print("Game terminated.")

# Main if function to run the game (calling other functions)
if __name__ == "__main__":
    main()
