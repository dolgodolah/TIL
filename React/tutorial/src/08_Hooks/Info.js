import {useEffect, useReducer, useState} from "react";

function reducer(state, action) {
    return {
        ...state,
        [action.name]: action.value
    };
}

const Info = () => {
    const [state, dispatch] = useReducer(reducer, {
        name: '',
        nickname: ''
    });
    const { name, nickname } = state;
    const onChange = e => {
        dispatch(e.target);
    };

    useEffect(() => {
        console.log("렌더링 완료!");
        console.log({
            name,
            nickname
        });
        return () => {
            console.log('cleanup');
            console.log(name);
        }
    }, [name]);

    return (
        <div>
            <div>
                <input name="name" value={name} onChange={onChange} />
                <input name="nickname" value={nickname} onChange={onChange} />
            </div>
            <div>
                <div>
                    <b>이름: </b>{name}
                </div>
                <div>
                    <b>닉네임: </b>{nickname}
                </div>
            </div>
        </div>
    );
}

export default Info;