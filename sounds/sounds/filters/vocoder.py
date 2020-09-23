from sounds.effects import echo  # Both an absolute import 
from ..effects.echo import echo_func  # And a relative import works..

def vocode():
    print(echo.echo_func())
    print(echo_func())