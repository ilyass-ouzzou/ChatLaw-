Chatbot des Codes Marocains
📝 Description
Le Chatbot des Codes Marocains est une application web interactive qui permet aux utilisateurs de poser des questions sur les codes juridiques marocains et d'obtenir des réponses instantanées. Le chatbot est basé sur des documents juridiques tels que le Code pénal, le Code du travail, la Moudawana, le Code des obligations et des contrats, et le Code de procédure pénale.

Le projet utilise des technologies modernes comme Flask pour le backend, Ollama pour interagir avec le modèle de langage Mistral, et FAISS pour la recherche sémantique. L'interface utilisateur est conçue avec Bootstrap pour une expérience utilisateur fluide et moderne.

🚀 Fonctionnalités
Recherche sémantique : Trouvez des réponses précises en fonction des documents juridiques indexés.

Interface utilisateur intuitive : Posez des questions et obtenez des réponses en temps réel.

Multilingue : Support du français et de l'arabe (à étendre).

Mode sombre : Basculez entre le mode clair et sombre pour un confort visuel.

Historique des conversations : Consultez les questions et réponses précédentes.

Export en PDF : Téléchargez la conversation au format PDF.

Recherche par mots-clés : Recherchez des articles pertinents dans les documents.

🛠 Technologies utilisées
Backend :

Flask : Framework web en Python pour créer l'application.

Ollama : Pour interagir avec le modèle de langage Mistral.

FAISS : Pour la recherche sémantique et l'indexation des documents.

Sentence Transformers : Pour encoder les phrases en vecteurs.

PyPDF2 : Pour extraire le texte des fichiers PDF.

Frontend :

Bootstrap : Pour une interface utilisateur moderne et responsive.

JavaScript : Pour les interactions dynamiques.

HTML/CSS : Pour la structure et le style de l'interface.

Autres outils :

FPDF2 : Pour générer des fichiers PDF.

Font Awesome : Pour les icônes.

📂 Structure du projet
Copy
ChatLaw/
│
├── app.py                  # Application Flask
├── templates/
│   ├── index.html          # Page d'accueil
│   └── chat.html           # Page du chatbot
├── static/
│   ├── styles.css          # Fichier CSS pour le style
│   └── images/             # Dossier pour les logos des codes
├── indexing.py             # Script d'indexation des documents
├── requirements.txt        # Dépendances du projet
└── data/                   # Dossier pour les fichiers PDF et les index
🚀 Installation
Prérequis
Python 3.8 ou supérieur

Git (optionnel, pour cloner le dépôt)

Étapes d'installation
Cloner le dépôt (ou télécharger le projet) :

bash
Copy
git clone https://github.com/votre-utilisateur/chatbot-codes-marocains.git
cd chatbot-codes-marocains
Créer un environnement virtuel (recommandé) :

bash
Copy
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
Installer les dépendances :

bash
Copy
pip install -r requirements.txt
Ajouter les fichiers PDF :

Placez les fichiers PDF des codes juridiques dans le dossier data/.

Assurez-vous que les fichiers sont nommés correctement (par exemple, code_penal.pdf, moudawana.pdf, etc.).

Indexer les documents :

Exécutez le script d'indexation pour créer les index FAISS :

bash
Copy
python indexing.py
🖥 Exécution
Démarrer l'application Flask :

bash
Copy
python app.py
Accéder à l'application :

Ouvrez votre navigateur et accédez à http://127.0.0.1:5000/.

🎨 Utilisation
Page d'accueil :

Lisez la description du projet et cliquez sur Commencer pour accéder au chatbot.

Page du chatbot :

Sélectionnez un document (par exemple, Code pénal).

Posez une question dans la zone de texte.

Consultez la réponse générée par le chatbot.

Utilisez les fonctionnalités supplémentaires comme :

Mode sombre : Basculez entre le mode clair et sombre.

Télécharger la conversation : Exportez la conversation en PDF.

Historique des conversations : Consultez les questions et réponses précédentes.

📄 Exemples de questions
Code pénal :

"Quelle est la peine pour le vol simple ?"

"Explique la différence entre meurtre et homicide involontaire."

Code du travail :

"Quels sont les droits des travailleurs en cas de licenciement abusif ?"

"Combien de jours de congé payé un employé a-t-il droit ?"

Moudawana :

"Quelles sont les conditions pour divorcer selon la Moudawana ?"

"Explique les droits des femmes en matière de garde d'enfants."

📜 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

🤝 Contribution
Les contributions sont les bienvenues ! Voici comment contribuer :

Forker le projet.

Créer une branche pour votre fonctionnalité (git checkout -b feature/NouvelleFonctionnalité).

Commiter vos changements (git commit -m 'Ajouter une nouvelle fonctionnalité').

Pusher la branche (git push origin feature/NouvelleFonctionnalité).

Ouvrir une Pull Request.

📞 Contact
Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter :

Email : votre-email@example.com

GitHub : votre-utilisateur

🙏 Remerciements
Merci à Ollama et Mistral pour le modèle de langage.

Merci à Bootstrap pour l'interface utilisateur.

Merci à la communauté Flask pour le support.

Profitez du Chatbot des Codes Marocains ! 🚀
