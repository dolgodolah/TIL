import './ValidationSample.css'
import {useState} from "react";

const ValidationSample = () => {
    const [ state, setState ] = useState({
        password: '',
        clicked: false,
        validated: false
    });
    const { password, clicked, validated } = state;

    const onChange = (e) => {
        const nextState = {
            ...state,
            password: e.target.value
        };
        setState(nextState)
    }

    const onClick = () => {
        const nextState = {
            ...state,
            clicked: true,
            validated: state.password === '0000'
        };
        setState(nextState)
    }

    return (
        <div>
            <input
                type="password"
                value={ password }
                onChange={ onChange }
                className={ clicked ? (validated ? 'success' : 'failure') : '' }
            />
            <button onClick={ onClick }>검증하기</button>
        </div>
    )
}

export default ValidationSample;