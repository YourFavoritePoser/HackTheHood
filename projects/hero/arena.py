from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''

    # TODO: create instance variables named team_one and team_two that
    # will hold our teams.

  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = input(
      "What is the max damage of the ability?  ")

    return Ability(name, max_damage)

  def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    # TODO: This method will allow a user to create a weapon.
    # Prompt the user for the necessary information to create a new weapon object.
    # return the new weapon object.
    pass

  def create_armor(self):
    '''Prompt user for Armor information
