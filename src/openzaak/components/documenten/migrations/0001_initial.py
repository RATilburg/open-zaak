# Generated by Django 2.2.2 on 2019-08-02 14:25

from django.db import migrations, models
import django.db.models.deletion
import privates.fields
import privates.storages
import uuid
import vng_api_common.fields
import vng_api_common.models
import vng_api_common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnkelvoudigInformatieObjectCanonical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lock', models.CharField(blank=True, default='', help_text='Hash string, which represents id of the lock', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gebruiksrechten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)', unique=True)),
                ('omschrijving_voorwaarden', models.TextField(help_text='Omschrijving van de van toepassing zijnde voorwaarden aan het gebruik anders dan raadpleging', verbose_name='omschrijving voorwaarden')),
                ('startdatum', models.DateTimeField(help_text='Begindatum van de periode waarin de gebruiksrechtvoorwaarden van toepassing zijn. Doorgaans is de datum van creatie van het informatieobject de startdatum.', verbose_name='startdatum')),
                ('einddatum', models.DateTimeField(blank=True, help_text='Einddatum van de periode waarin de gebruiksrechtvoorwaarden van toepassing zijn.', null=True, verbose_name='startdatum')),
                ('informatieobject', models.ForeignKey(help_text='URL-referentie naar het INFORMATIEOBJECT.', on_delete=django.db.models.deletion.CASCADE, to='documenten.EnkelvoudigInformatieObjectCanonical')),
            ],
            options={
                'verbose_name': 'gebruiksrecht informatieobject',
                'verbose_name_plural': 'gebruiksrechten informatieobject',
            },
        ),
        migrations.CreateModel(
            name='ObjectInformatieObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)', unique=True)),
                ('object', models.URLField(help_text='URL-referentie naar het gerelateerde OBJECT (in deze of een andere API).')),
                ('object_type', models.CharField(choices=[('besluit', 'Besluit'), ('zaak', 'Zaak')], help_text='Het type van het gerelateerde OBJECT.', max_length=100, verbose_name='objecttype')),
                ('informatieobject', models.ForeignKey(help_text='URL-referentie naar het INFORMATIEOBJECT.', on_delete=django.db.models.deletion.CASCADE, to='documenten.EnkelvoudigInformatieObjectCanonical')),
            ],
            options={
                'verbose_name': 'Oobject-informatieobject',
                'verbose_name_plural': 'object-informatieobjecten',
                'unique_together': {('informatieobject', 'object')},
            },
            bases=(vng_api_common.models.APIMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EnkelvoudigInformatieObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificatie', models.CharField(blank=True, default='', help_text='Een binnen een gegeven context ondubbelzinnige referentie naar het INFORMATIEOBJECT.', max_length=40, validators=[vng_api_common.validators.AlphanumericExcludingDiacritic()])),
                ('bronorganisatie', vng_api_common.fields.RSINField(help_text='Het RSIN van de Niet-natuurlijk persoon zijnde de organisatie die het informatieobject heeft gecreëerd of heeft ontvangen en als eerste in een samenwerkingsketen heeft vastgelegd.', max_length=9)),
                ('creatiedatum', models.DateField(help_text='Een datum of een gebeurtenis in de levenscyclus van het INFORMATIEOBJECT.')),
                ('titel', models.CharField(help_text='De naam waaronder het INFORMATIEOBJECT formeel bekend is.', max_length=200)),
                ('vertrouwelijkheidaanduiding', vng_api_common.fields.VertrouwelijkheidsAanduidingField(blank=True, choices=[('openbaar', 'Openbaar'), ('beperkt_openbaar', 'Beperkt openbaar'), ('intern', 'Intern'), ('zaakvertrouwelijk', 'Zaakvertrouwelijk'), ('vertrouwelijk', 'Vertrouwelijk'), ('confidentieel', 'Confidentieel'), ('geheim', 'Geheim'), ('zeer_geheim', 'Zeer geheim')], help_text='Aanduiding van de mate waarin het INFORMATIEOBJECT voor de openbaarheid bestemd is.', max_length=20)),
                ('auteur', models.CharField(help_text='De persoon of organisatie die in de eerste plaats verantwoordelijk is voor het creëren van de inhoud van het INFORMATIEOBJECT.', max_length=200)),
                ('status', models.CharField(blank=True, choices=[('in_bewerking', 'In bewerking'), ('ter_vaststelling', 'Ter vaststelling'), ('definitief', 'Definitief'), ('gearchiveerd', 'Gearchiveerd')], help_text="Aanduiding van de stand van zaken van een INFORMATIEOBJECT. De waarden 'in bewerking' en 'ter vaststelling' komen niet voor als het attribuut `ontvangstdatum` van een waarde is voorzien. Wijziging van de Status in 'gearchiveerd' impliceert dat het informatieobject een duurzaam, niet-wijzigbaar Formaat dient te hebben.", max_length=20, verbose_name='status')),
                ('beschrijving', models.TextField(blank=True, help_text='Een generieke beschrijving van de inhoud van het INFORMATIEOBJECT.', max_length=1000)),
                ('ontvangstdatum', models.DateField(blank=True, help_text='De datum waarop het INFORMATIEOBJECT ontvangen is. Verplicht te registreren voor INFORMATIEOBJECTen die van buiten de zaakbehandelende organisatie(s) ontvangen zijn. Ontvangst en verzending is voorbehouden aan documenten die van of naar andere personen ontvangen of verzonden zijn waarbij die personen niet deel uit maken van de behandeling van de zaak waarin het document een rol speelt.', null=True, verbose_name='ontvangstdatum')),
                ('verzenddatum', models.DateField(blank=True, help_text='De datum waarop het INFORMATIEOBJECT verzonden is, zoals deze op het INFORMATIEOBJECT vermeld is. Dit geldt voor zowel inkomende als uitgaande INFORMATIEOBJECTen. Eenzelfde informatieobject kan niet tegelijk inkomend en uitgaand zijn. Ontvangst en verzending is voorbehouden aan documenten die van of naar andere personen ontvangen of verzonden zijn waarbij die personen niet deel uit maken van de behandeling van de zaak waarin het document een rol speelt.', null=True, verbose_name='verzenddatum')),
                ('indicatie_gebruiksrecht', models.NullBooleanField(default=None, help_text='Indicatie of er beperkingen gelden aangaande het gebruik van het informatieobject anders dan raadpleging. Dit veld mag `null` zijn om aan te geven dat de indicatie nog niet bekend is. Als de indicatie gezet is, dan kan je de gebruiksrechten die van toepassing zijn raadplegen via de GEBRUIKSRECHTen resource.', verbose_name='indicatie gebruiksrecht')),
                ('ondertekening_soort', models.CharField(blank=True, choices=[('analoog', 'Analoog'), ('digitaal', 'Digitaal'), ('pki', 'PKI')], help_text='Aanduiding van de wijze van ondertekening van het INFORMATIEOBJECT', max_length=10, verbose_name='ondertekeningsoort')),
                ('ondertekening_datum', models.DateField(blank=True, help_text='De datum waarop de ondertekening van het INFORMATIEOBJECT heeft plaatsgevonden.', null=True, verbose_name='ondertekeningdatum')),
                ('informatieobjecttype', models.URLField(help_text='URL-referentie naar het INFORMATIEOBJECTTYPE (in de Catalogi API).')),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Unieke resource identifier (UUID4)')),
                ('formaat', models.CharField(blank=True, help_text='Het "Media Type" (voorheen "MIME type") voor de wijze waaropde inhoud van het INFORMATIEOBJECT is vastgelegd in een computerbestand. Voorbeeld: `application/msword`. Zie: https://www.iana.org/assignments/media-types/media-types.xhtml', max_length=255)),
                ('taal', models.CharField(help_text='Een ISO 639-2/B taalcode waarin de inhoud van het INFORMATIEOBJECT is vastgelegd. Voorbeeld: `nld`. Zie: https://www.iso.org/standard/4767.html', max_length=3)),
                ('bestandsnaam', models.CharField(blank=True, help_text='De naam van het fysieke bestand waarin de inhoud van het informatieobject is vastgelegd, inclusief extensie.', max_length=255, verbose_name='bestandsnaam')),
                ('inhoud', privates.fields.PrivateMediaFileField(storage=privates.storages.PrivateMediaFileSystemStorage(), upload_to='uploads/%Y/%m/')),
                ('link', models.URLField(blank=True, help_text='De URL waarmee de inhoud van het INFORMATIEOBJECT op te vragen is.')),
                ('integriteit_algoritme', models.CharField(blank=True, choices=[('crc_16', 'CRC-16'), ('crc_32', 'CRC-32'), ('crc_64', 'CRC-64'), ('fletcher_4', 'Fletcher-4'), ('fletcher_8', 'Fletcher-8'), ('fletcher_16', 'Fletcher-16'), ('fletcher_32', 'Fletcher-32'), ('hmac', 'HMAC'), ('md5', 'MD5'), ('sha_1', 'SHA-1'), ('sha_256', 'SHA-256'), ('sha_512', 'SHA-512'), ('sha_3', 'SHA-3')], help_text='Aanduiding van algoritme, gebruikt om de checksum te maken.', max_length=20, verbose_name='integriteit algoritme')),
                ('integriteit_waarde', models.CharField(blank=True, help_text='De waarde van de checksum.', max_length=128, verbose_name='integriteit waarde')),
                ('integriteit_datum', models.DateField(blank=True, help_text='Datum waarop de checksum is gemaakt.', null=True, verbose_name='integriteit datum')),
                ('versie', models.PositiveIntegerField(default=1, help_text='Het (automatische) versienummer van het INFORMATIEOBJECT. Deze begint bij 1 als het INFORMATIEOBJECT aangemaakt wordt.')),
                ('begin_registratie', models.DateTimeField(auto_now=True, help_text='Een datumtijd in ISO8601 formaat waarop deze versie van het INFORMATIEOBJECT is aangemaakt of gewijzigd.')),
                ('canonical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documenten.EnkelvoudigInformatieObjectCanonical')),
            ],
            options={
                'unique_together': {('uuid', 'versie')},
            },
            bases=(vng_api_common.models.APIMixin, models.Model),
        ),
    ]
