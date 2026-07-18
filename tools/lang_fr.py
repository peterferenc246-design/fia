# FR — mapovanie na odseky povodneho SK Wordu (index -> [(text, bold)])
PARA = {
 2:  [("Peter Ferenc", True)],
 3:  [("Rammelkam 2, 84036 Kumhausen, Allemagne", True)],
 6:  [("Tribunal de l'Union européenne", True)],
 7:  [("Greffe du Tribunal", False)],
 8:  [("Rue du Fort Niedergrünewald L-2925 Luxembourg", False)],
 11: [("24 décembre 2025", True)],
 13: [("Objet :", True), (" Réponse à la communication relative à l'impossibilité de faire droit à la demande d'ouverture d'un compte d'accès à l'application e-Curia", False)],
 14: [("Numéro de référence :", True), (" DEM10029674", False)],
 16: [("RÉPONSE À LA COMMUNICATION DE REJET DE LA DEMANDE D'ACCÈS À e-CURIA", True)],
 19: [("Monsieur le Greffier,", False)],
 21: [("J'accuse réception de votre communication du 22 décembre 2025, par laquelle j'ai été informé qu'il ne pouvait être fait droit à ma demande d'ouverture d'un compte d'accès à l'application e-Curia en raison du non-respect de certaines conditions formelles.", False)],
 22: [("Je me permets d'exposer les éléments suivants, aux seules fins de clarification procédurale de la situation :", False)],
 23: [("Ma demande d'accès à l'application e-Curia n'a pas été introduite en vue d'agir en qualité de représentant d'autres personnes, d'un État membre ou d'une institution de l'Union européenne", True), (", mais", False)],
 24: [("exclusivement en ma qualité de personne physique – requérant potentiel.", False)],
 25: [("Je prends acte de ce que ", False), ("l'ouverture d'un compte d'accès e-Curia est subordonnée à la qualité d'avocat ou de représentant habilité", True), (", et que, en tant que personne physique dépourvue d'une telle habilitation, je ne remplis pas les conditions requises pour son ouverture.", False)],
 26: [("Je confirme en outre expressément avoir connaissance de ce que ", False), ("l'introduction d'un recours relevant de la compétence du Tribunal de l'Union européenne requiert obligatoirement la représentation par un avocat", True), (" habilité à exercer devant une juridiction d'un État membre ou d'un autre État partie à l'accord EEE.", False)],
 28: [("Dans le prolongement de ce qui précède, je me permets d'indiquer que ", False), ("je prépare actuellement le dépôt d'une demande d'aide juridictionnelle au titre des articles 146 à 150 du règlement de procédure du Tribunal", True), (", laquelle doit constituer la condition procédurale préalable à la désignation d'un représentant légal ; je vous en informe par la présente. La demande est introduite parallèlement sous forme papier, conformément au règlement de procédure.", False)],
 29: [("La présente réponse revêt un caractère exclusivement ", False), ("informatif et de clarification procédurale ", True), ("et ne tend pas au réexamen de la décision de ne pas ouvrir l'accès à l'application e-Curia.", False)],
 30: [("À la suite de la liste des conditions non remplies qui m'a été communiquée, je me permets d'apporter la précision suivante :", False)],
 31: [("J'ai ", False), ("imprimé le formulaire de demande, l'ai signé de ma main et l'ai adressé par voie postale en recommandé avec remise en main propre ", True), ("au Tribunal de l'Union européenne, conformément à l'article 147, paragraphe 6, du règlement de procédure.", False)],
 32: [("Je relève par ailleurs que, dans la communication reçue, ", False), ("ni le point 1, ni le point 2", True), (", ", False), ("ni le point 4,", True)],
 33: [("à savoir la signature du formulaire et la copie de la pièce d'identité, ne sont cochés comme conditions non remplies. Seul le point 3, relatif à l'habilitation à représenter dans une procédure devant une instance juridictionnelle, est coché.", False)],
 34: [("Je me permets de souligner que ", False), ("je n'ai pas sollicité l'accès à l'application e-Curia en qualité d'avocat ni de représentant de tiers", True), (", mais en tant que personne physique – requérant potentiel. Dans ce contexte, l'habilitation visée au point 3 ne saurait constituer une condition pertinente", False)],
 35: [("de rejet de ma demande d'ouverture d'un compte d'accès à l'application e-Curia du 19/12/2025, enregistrée sous la référence ", False), ("DEM10029674.", True)],
 36: [("En conséquence, je me permets de solliciter une précision sur le fond,", True)],
 37: [("le point de savoir si mon envoi papier, signé de ma main, a été reçu et enregistré,", False)],
 38: [("et pour quel motif la communication fait état du non-respect de la condition visée au point 3, laquelle ne s'applique pas à ma qualité de personne physique – requérant potentiel –, en indiquant le fondement juridique.", False)],
 39: [("Je me permets également de vous informer que, en raison de mon insolvabilité, je dépose parallèlement à la présente réponse une demande d'aide juridictionnelle et de désignation d'un représentant légal, conformément aux articles 146 à 150 du règlement de procédure du Tribunal.", False)],
 40: [("Ces deux documents sont transmis par courrier électronique, revêtus d'une signature électronique qualifiée (QES), dans le prolongement de la correspondance électronique en cours avec le greffe du Tribunal.", False)],
 41: [("Cet envoi revêt un caractère documentaire et informatif. Le dépôt régulier sera effectué conformément au règlement de procédure.", False)],
}
# odseky s hypertextovym e-mailom — prekladame LEN popisky, adresa a odkaz ostavaju
LABELS = {
 4: [("E-Mail:", "E-mail :"), ("Telefon:", "Téléphone :")],
 9: [("E-Mail:", "E-mail :")],
}
# textboxy (zaver + podpis)
BOXES = {
 "S úctou": "Respectueusement,",
 "V Kumhausene 24.12.2025": "Kumhausen, le 24.12.2025",
}
