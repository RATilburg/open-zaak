"""
Integrations of selectielijst API into Django admin.
"""
from typing import Optional

from django import forms
from django.db.models import Field
from django.http import HttpRequest

from .api import get_procestypen, get_resultaattype_omschrijvingen, get_resultaten


def get_procestype_field(
    db_field: Field, request: HttpRequest, **kwargs
) -> forms.ChoiceField:
    choices = (
        (procestype["url"], f"{procestype['nummer']} - {procestype['naam']}",)
        for procestype in get_procestypen()
    )

    return forms.ChoiceField(
        label=db_field.verbose_name.capitalize(),
        choices=choices,
        required=False,
        help_text=db_field.help_text,
    )


def get_selectielijst_resultaat_choices(proces_type: Optional[str] = None):
    choices = (
        (resultaat["url"], f"{resultaat['volledigNummer']} - {resultaat['naam']}")
        for resultaat in get_resultaten(proces_type)
    )
    return choices


def get_selectielijstklasse_field(
    db_field: Field, request: HttpRequest, **kwargs
) -> forms.ChoiceField:
    return forms.ChoiceField(
        label=db_field.verbose_name.capitalize(),
        choices=get_selectielijst_resultaat_choices,
        required=not db_field.blank,
        help_text=db_field.help_text,
    )


def get_resultaattype_omschrijving_field(
    db_field: Field, request: HttpRequest, **kwargs
) -> forms.ChoiceField:
    choices = (
        (omschrijving["url"], omschrijving["omschrijving"])
        for omschrijving in get_resultaattype_omschrijvingen()
    )
    return forms.ChoiceField(
        label=db_field.verbose_name.capitalize(),
        choices=choices,
        required=not db_field.blank,
        help_text=db_field.help_text,
    )
