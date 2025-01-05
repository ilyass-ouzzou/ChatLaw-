Installation
===========

Prérequis
---------

* Python 3.8 ou supérieur
* Git
* Pip

Installation étape par étape
--------------------------

1. Cloner le dépôt
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/votre-utilisateur/chatbot-codes-marocains.git
   cd chatbot-codes-marocains

2. Créer un environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate

3. Installer les dépendances
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pip install -r requirements.txt

4. Configuration des données
~~~~~~~~~~~~~~~~~~~~~~~~~

* Placez vos fichiers PDF dans le dossier ``data/``
* Exécutez le script d'indexation

.. code-block:: bash

   python indexing.py