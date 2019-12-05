import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";

import { COMPONENT_CHOICES } from './constants';

const Choice = PropTypes.arrayOf(PropTypes.string);


const RadioInput = (props) => {
    const { name, value, label, i, checked, onChange } = props;
    const id = `id_${name}_${i}`;
    return (
        <label htmlFor={id}>
            <input
                type="radio"
                name={name}
                value={value}
                id={id}
                checked={checked}
                onChange={ () => onChange(value) }
            />
            {label}
        </label>
    );
};

RadioInput.propTypes = {
    name: PropTypes.string.isRequired,
    value: PropTypes.string.isRequired,
    label: PropTypes.string.isRequired,
    i: PropTypes.number.isRequired,
    checked: PropTypes.bool.isRequired,
    onChange: PropTypes.func,
};


const RadioSelect = (props) => {
    const { choices, prefix, name } = props;

    const [currentValue, setCurrentValue] = useState(null);

    const radios = choices.map( ([value, label], index) => {
        const _name = `${prefix}-${index}-${name}`;
        return (
            <li key={index}>
                <RadioInput
                    name={_name}
                    value={value}
                    label={label}
                    i={index}
                    checked={value == currentValue}
                    onChange={setCurrentValue}
                />
            </li>
        );
    });

    return (
        <ul>
            { radios }
        </ul>
    )
}

RadioSelect.propTypes = {
    choices: PropTypes.arrayOf(Choice),
    prefix: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    helpText: PropTypes.string,
};



const AutorisatieForm = (props) => {
    return (
        <div className="autorisatie-form">
            <div className="autorisatie-form__component">
                <RadioSelect choices={COMPONENT_CHOICES} prefix="form" name="component" />
            </div>

            <div className="autorisatie-form__scopes">
                TODO: scopes
            </div>
        </div>
    );
};

export { AutorisatieForm };
