"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteGenre
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateGenre

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5575/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/genres_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def genres_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_genres_afficher = """SELECT * from t_apprenti"""
                    mc_afficher.execute(strsql_genres_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_genre_sel}
                    strsql_genres_afficher = """SELECT * FROM t_apprenti WHERE id_apprennti = %(value_id_apprennti_selected)z"""

                    mc_afficher.execute(strsql_genres_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_genres_afficher = """SELECT * FROM t_apprenti ORDER BY id_apprennti DESC"""

                    mc_afficher.execute(strsql_genres_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_genre" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données genres affichés !!", "success")

        except Exception as Exception_genres_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{genres_afficher.__name__} ; "
                                          f"{Exception_genres_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("genres/genres_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genres_ajouter", methods=['GET', 'POST'])
def genres_ajouter_wtf():
    form = FormWTFAjouterGenres()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_apprenti_wtf = form.nom_apprenti_wtf.data
                prenom_apprenti_wtf = form.prenom_apprenti_wtf.data
                ordonance_apprenti_wtf = form.ordonance_apprenti_wtf.data
                filiere_apprenti_wtf = form.filiere_apprenti_wtf.data
                valeurs_insertion_dictionnaire = {"value_nom_apprenti": nom_apprenti_wtf,
                                                  "value_prenom_apprenti": prenom_apprenti_wtf,
                                                  "value_filiere_apprenti": filiere_apprenti_wtf,
                                                  "value_ordonance_apprenti": ordonance_apprenti_wtf,
                                                  }
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_apprenti (id_apprennti, nom_apprenti, prenom_apprenti, filiere_apprenti, ordonance_apprenti) 
                         VALUES (NULL, %(value_nom_apprenti)s, %(value_prenom_apprenti)s, %(value_filiere_apprenti)s, %(value_ordonance_apprenti)s)"""

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('genres_afficher', order_by='DESC', id_genre_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{genres_ajouter_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("genres/genres_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/genre_update", methods=['GET', 'POST'])
def genre_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    id_apprennti_update = request.values['id_genre_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateGenre()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            nom_apprenti_update = form_update.nom_apprenti_update_wtf.data
            prenom_apprenti_update = form_update.prenom_apprenti_update_wtf.data
            filiere_apprenti_update = form_update.filiere_apprenti_update_wtf.data
            ordonance_apprenti_update = form_update.filiere_apprenti_update_wtf.data


            valeur_update_dictionnaire = {"value_id_apprennti": id_apprennti_update,
                                          "value_nom_apprenti": nom_apprenti_update,
                                          "value_prenom_apprenti": prenom_apprenti_update,
                                          "value_filiere_apprenti": filiere_apprenti_update,
                                          "value_ordonance_apprenti": ordonance_apprenti_update,
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulegenre = """UPDATE t_apprenti SET nom_apprenti = %(value_nom_apprenti)s, 
            prenom_apprenti = %(value_prenom_apprenti)s, filiere_apprenti = %(value_filiere_apprenti)s, ordonance_apprenti = %(value_ordonance_apprenti)s WHERE id_apprennti = %(value_id_apprennti)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=id_apprennti_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_apprennti = "SELECT id_apprennti, nom_apprenti, prenom_apprenti, filiere_apprenti, ordonance_apprenti FROM t_apprenti " \
                               "WHERE id_apprennti = %(value_id_apprennti)s"
            valeur_select_dictionnaire = {"value_id_apprennti": id_apprennti_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_apprennti, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_apprennti = mybd_conn.fetchone()
            print("data_nom_apprenti ", data_nom_apprennti, " type ", type(data_nom_apprennti), " apprenti ",
                  data_nom_apprennti["nom_apprenti"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "genre_update_wtf.html"
            form_update.nom_apprenti_update_wtf.data = data_nom_apprennti["nom_apprenti"]
            form_update.prenom_apprenti_update_wtf.data = data_nom_apprennti["prenom_apprenti"]
            form_update.filiere_apprenti_update_wtf.data = data_nom_apprennti["filiere_apprenti"]
            form_update.ordonance_apprenti_update_wtf.data = data_nom_apprennti["ordonance_apprenti"]


    except Exception as Exception_genre_update_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{genre_update_wtf.__name__} ; "
                                      f"{Exception_genre_update_wtf}")

    return render_template("genres/genre_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"
    
    Remarque :  Dans le champ "nom_genre_delete_wtf" du formulaire "genres/genre_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/genre_delete", methods=['GET', 'POST'])
def genre_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None

    # Use request.form.get to safely get the value, avoiding KeyError
    id_apprennti_delete = request.form.get('id_apprennti_btn_delete_html')

    if not id_apprennti_delete:
        flash("Erreur, aucun apprenti sélectionné pour la suppression.", "danger")
        return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))

    form_delete = FormWTFDeleteGenre()
    if request.method == "POST" and form_delete.validate_on_submit():
        if form_delete.submit_btn_annuler.data:
            return redirect(url_for("genres_afficher", order_by="ASC", id_genre_sel=0))

        if form_delete.submit_btn_conf_del.data:
            data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
            flash("Effacer le genre de façon définitive de la BD !!!", "danger")
            btn_submit_del = True

        if form_delete.submit_btn_del.data:
            valeur_delete_dictionnaire = {"value_id_apprennti": id_apprennti_delete}
            str_sql_delete_apprenti = "DELETE FROM t_apprenti WHERE id_apprennti = %(value_id_apprennti)s"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_apprenti, valeur_delete_dictionnaire)

            flash("Apprenti définitivement effacé !!", "success")
            return redirect(url_for('genres_afficher', order_by="ASC", id_genre_sel=0))
    elif request.method == "GET":
        valeur_select_dictionnaire = {"value_id_apprennti": id_apprennti_delete}
        str_sql_genres_films_delete = """
            SELECT id_apprennti, nom_apprenti, prenom_apprenti, filiere_apprenti, ordonance_apprenti 
            FROM t_apprenti WHERE id_apprennti = %(value_id_apprennti)s
        """
        with DBconnection() as mydb_conn:
            mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
            data_films_attribue_genre_delete = mydb_conn.fetchall()
            session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

        str_sql_id_genre = ""




