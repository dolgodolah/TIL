import React, {useCallback, useState} from "react";
import './TodoInsert.scss'
import { MdAdd } from 'react-icons/md';
const TodoInsert = ( {onInsert} ) => {
    const [value, setValue] = useState('');

    const onChange = useCallback(e => {
        setValue(e.target.value);
    }, []);

    const onSubmit = useCallback(
        e => {
            onInsert(value);
            setValue('');

            // submit 이벤트 브라우저에서 새로고침을 발생시키기 때문에 이를 방지하기 위해 이 함수를 호출한다.
            e.preventDefault();
        },
        [onInsert, value],
    );

    return (
        <form className="TodoInsert" onSubmit={onSubmit}>
            <input placeholder="할 일을 입력하세요" value={value} onChange={onChange} />
            <button type="submit">
                <MdAdd />
            </button>
        </form>
    )
}

export default TodoInsert