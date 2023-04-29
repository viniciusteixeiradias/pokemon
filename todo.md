- [ ] Create database table called pokemon
  - [ ] Fields: (id, name, image, description, strong)

- [ ] Fill the table with the Pokemon API with 50 pokemons
- [ ] Create endpoint to return random pokemon
- [ ] Create endpoint to recive 2 pokemons id and return the winner

Duvidas:

Por que alguns metodos estão acionando session.commit() sendo que o manager já faz isso?

```py
class ProfileDAO():
    def __init__(self, session: Session = Depends(session_manager)):
```

```py
def session_manager(auto_commit=True) -> Session:
```
