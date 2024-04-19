<details><summary>Question #1</summary>
Parmi les expressions suivantes, lesquelles définissent un set?

Vous devez sélectionner toutes les affirmations exactes.

- [ ] {1, 2, 3}
- [ ] {1: 1, 2: 2, 3: 3}
- [ ] {}
- [ ] set()
- [ ] [1, 2, 3]
- [ ] (1, 2, 3)

<details><summary>Solution</summary>

- [x] {1, 2, 3}
- [ ] {1: 1, 2: 2, 3: 3}
- [ ] {}
- [x] set()
- [ ] [1, 2, 3]
- [ ] (1, 2, 3)

</details></details>

<details><summary>Question #2</summary>

Où peut-on placer un fichier `mymodule.py`, de sorte qu'il soit automatiquement trouvé lorsqu'on émet une instruction `import mymodule` à partir de n'importe quel
fichier de code Python ?

Vous devez sélectionner toutes les affirmations exactes.

- [ ] Dans l'un des dossiers listés dans la variable d'environnement PYTHONPATH
- [ ] Dans l'un des dossiers listés dans la variable d'environnement PATH
- [ ] Dans le dossier site-packages/ de la distribution Python
- [ ] Dans le dossier personnel de l'utilisateur, ~/
- [ ] Dans un dossier ./python_modules/ à l'intérieur du répertoire de travail actuel

<details><summary>Solution</summary>

- [x] Dans l'un des dossiers listés dans la variable d'environnement PYTHONPATH
- [ ] Dans l'un des dossiers listés dans la variable d'environnement PATH
- [x] Dans le dossier site-packages/ de la distribution Python
- [ ] Dans le dossier personnel de l'utilisateur, ~/
- [ ] Dans un dossier ./python_modules/ à l'intérieur du répertoire de travail actuel

</details></details>

<details><summary>Question #3</summary>

Sélectionnez tous les littéraux Python int valides.

Vous devez sélectionner toutes les affirmations exactes.

- [ ] 1257823489853
- [ ] 0xABCDEF
- [ ] 0B110101
- [ ] 4,321,678
- [ ] 1_234_56
- [ ] 0
- [ ] "123"
- [ ] 0L9223372036854775807
- [ ] 1.234
- [ ] 0x1A3C5D7G

<details><summary>Solution</summary>

- [x] 1257823489853
- [x] 0xABCDEF
- [x] 0B110101
- [ ] 4,321,678
- [x] 1_234_56
- [x] 0
- [ ] "123"
- [ ] 0L9223372036854775807
    - Ceci n'est pas / plus valide avec Python 3. Était utilisé en Python 2 pour indiquer les entiers "long".
- [ ] 1.234
- [ ] 0x1A3C5D7G
    - Invalide à cause de la lettre G (doit être A-F pour les chiffres hexadécimaux)

</details></details>

<details><summary>Question #4</summary>

Lorsque ce code atteint l'appel time.sleep(), combien de chaînes de caractères username différentes sont simultanément présentes dans la mémoire active de
l'interpréteur ?

```python
import time

username = "john"


class User:
    username = "jane"

    def get_username(self):
        username = "jack"
        time.sleep(2)
        return username


user = User().get_username()
print(user)
```

- [ ] 1 chaîne de caractères.
- [ ] 2 chaîne de caractères.
- [ ] 3 chaîne de caractères.
- [ ] 4 chaîne de caractères.
- [ ] 5 chaîne de caractères.
 
<details><summary>Solution</summary>

- [ ] 1 chaîne de caractères.
- [ ] 2 chaîne de caractères.
- [x] 3 chaîne de caractères.
- [ ] 4 chaîne de caractères.
- [ ] 5 chaîne de caractères.
</details></details>