# I assumed the indentation errors are not intentional and have fixed them while answering these questions
""" 
1. The Parent is the class Spell and the child is both the class Accio and Confundo.
2.  Accio
    Summoning Charm Accio
    No description
    Confundus Charm Confundo
    Causes the victim to become confused and befuddled
3. The get description returns 'Causes the victim to become confused and befuddled' because we have initiated the get_description method in the confundo class and changed
    it's return value.
4. We need to execute the get_description method inside the class Accio and set the appropriate return value.

"""
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self,'Accio','Summoning Charm')
    def get_description(self):
        return "This charm summons an object to the caster, potentially over a significant distance"
