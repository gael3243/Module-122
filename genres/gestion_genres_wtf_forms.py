from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Regexp, DataRequired

class FormWTFAjouterGenres(FlaskForm):
    nom_apprenti_wtf = StringField("Nom", validators=[DataRequired(), Length(min=2, max=50), Regexp(r"^[A-Za-z\s\-]+$", message="Caractères alphabétiques uniquement")])
    prenom_apprenti_wtf = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=50), Regexp(r"^[A-Za-z\s\-]+$", message="Caractères alphabétiques uniquement")])
    filiere_apprenti_wtf = StringField("Filière", validators=[DataRequired(), Length(min=2, max=50)])
    ordonance_apprenti_wtf = StringField("Ordonnance", validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField("Ajouter")

class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_apprenti_update_regexp = ""
    nom_apprenti_update_wtf = StringField("Clavioter le genre ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_apprenti_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    prenom_apprenti_update_regexp = ""
    prenom_apprenti_update_wtf = StringField("Clavioter le genre ",
                                          validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                      Regexp(prenom_apprenti_update_regexp,
                                                             message="Pas de chiffres, de "
                                                                     "caractères "
                                                                     "spéciaux, "
                                                                     "d'espace à double, de double "
                                                                     "apostrophe, de double trait "
                                                                     "union")
                                                      ])
    filiere_apprenti_update_regexp = ""
    filiere_apprenti_update_wtf = StringField("Clavioter le genre ",
                                          validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                      Regexp(filiere_apprenti_update_regexp,
                                                             message="Pas de chiffres, de "
                                                                     "caractères "
                                                                     "spéciaux, "
                                                                     "d'espace à double, de double "
                                                                     "apostrophe, de double trait "
                                                                     "union")
                                                      ])
    ordonance_apprenti_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    ordonance_apprenti_update_wtf = StringField("Clavioter le genre ",
                                          validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                      Regexp(ordonance_apprenti_update_regexp,
                                                             message="Pas de chiffres, de "
                                                                     "caractères "
                                                                     "spéciaux, "
                                                                     "d'espace à double, de double "
                                                                     "apostrophe, de double trait "
                                                                     "union")
                                                      ])
    submit = SubmitField("Update genre")

class FormWTFDeleteGenre(FlaskForm):
    id_apprennti_delete_wtf = StringField("ID")
    nom_apprenti_delete_wtf = StringField("Nom")
    prenom_apprenti_delete_wtf = StringField("Prénom")
    filiere_apprenti_delete_wtf = StringField("Filière")
    ordonance_apprenti_delete_wtf = StringField("Ordonnance")
    submit_btn_del = SubmitField("Effacer apprenti")
    submit_btn_conf_del = SubmitField("Êtes-vous sûr de vouloir effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
