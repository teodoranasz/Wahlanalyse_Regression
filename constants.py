unwanted_cols_SPD = ["Wahlberechtigte", "max_abs", "min_abs", "Dif_abs", "max_rel", "min_rel", "Dif_rel", "BTW21_abs", "OBM20_abs", 'OBM20_rel', "LTW19_abs", "SRW19_abs", "BTW17_abs", 'BTW17_rel', 'SRW14_rel', 'LTW14_rel', "SRW14_abs", "LTW14_abs"]
unwanted_cols_wahlbet = ['Stadtbezirk', 'Wahl', 'Wahlberechtigte', 'Briefwaehler', 'Wähler', 'ungültige Stimmen', 'gueltige_Stimmen', 'AfD_abs', 'CDU_abs', 'DIE LINKE_abs', 'SPD_abs', 'FDP_abs', 'Gruene_abs', 'Die Partei_abs', 'Sonstige_abs', 'AFD_rel', 'CDU_rel', 'Linke_rel', 'SPD_rel', 'FDP_rel', 'Gruene_rel', 'Partei_rel', 'Sonstige_rel']
newname_cols_SPD = {'Name':'Gebiet', 'Stadtbezirk':'Bezirk', 'BTW21_rel':'BTW',  'LTW19_rel':'LTW', 'SRW19_rel':'KMW'}

cols_comma = ['Lebenszufriedenheit', 'Nutzfahrzeuge', 'Wohneigentum Quote', 'Arbeitslosenquote',
              'Mietbelastung', 'Haushaltseinkommen', 'Realschulabschlussquote',
              'Hochschulabschlussquote', 'Durchschnittsalter', 'Altenquote', 'Jugendquote']
cols_to_float = cols_comma + ['Einwohner', 'Ausländer', 'Privat-PKW', 'Nutzfahrzeuge', 'Langzeitarbeitslose',
                              'Arbeitslose Frauen', 'Straftaten', 'Kinder insgesamt']
cols_to_scale = ['Ausländer', 'Privat-PKW', 'Nutzfahrzeuge', 'Langzeitarbeitslose',
                 'Straftaten', 'Kinder insgesamt']
cols_to_hundred = cols_to_scale + ['BTW', 'LTW', 'KMW', 'Wahlbeteiligung']

features_needed = [ ('Einwohner.csv', ['2022','Einwohner insgesamt','Einwohner'] ),
                    ('Einwohner.csv', ['2022','   Ausländer','Ausländer'] ),
                    ('Zufriedenheitsfaktoren.csv', ['2021','Lebenszufriedenheit'] ),
                    ('Kraftfahrzeuge.csv', ['2022','Privat-PKW'] ),
                    ('Kraftfahrzeuge.csv', ['2022','Nutzfahrzeuge'] ),
                    ('Wohnsituation.csv', ['2021','Wohneigentum', 'Wohneigentum Quote'] ),
                    ('Arbeitslose.csv', ['2022','Anteil an den Erwerbsfähigen','Arbeitslosenquote'] ),
                    ('Arbeitslose.csv', ['2015','Langzeitarbeitslose'] ),
                    ('Arbeitslose.csv', ['2022', 'Frauen', 'Arbeitslose Frauen']),
                    ('Mieten.csv', ['2021','Mietbelastung'] ),
                    ('Einkommen.csv', ['2021','Haushaltseinkommen'] ),
                    ('Abschlüsse.csv', ['2021','Realschulabschluss','Realschulabschlussquote'] ),
                    ('Abschlüsse.csv', ['2021','Hochschulabschluss','Hochschulabschlussquote'] ),
                    ('Straftaten.csv', ['2022','Straftaten insgesamt','Straftaten'] ),
                    ('Alter.csv', ['2023','Durchschnittsalter'] ),
                    ('Alter.csv', ['2023','Altenquote'] ),
                    ('Alter.csv', ['2023','Jugendquote'] ),
                    ('Kinder_in_Kitas.csv', ['2022','Kinder insgesamt'] )
                   ]

cols_dependent = ['BTW','LTW','KMW','Wahlbeteiligung']
cols_independent = [
       'Einwohner', 'Ausländer', 'Lebenszufriedenheit', 'Privat-PKW', 'Nutzfahrzeuge',
       'Wohneigentum Quote', 'Arbeitslosenquote', 'Langzeitarbeitslose',
       'Arbeitslose Frauen', 'Mietbelastung', 'Haushaltseinkommen',
       'Realschulabschlussquote', 'Hochschulabschlussquote', 'Straftaten',
       'Durchschnittsalter', 'Altenquote', 'Jugendquote', 'Kinder insgesamt']

