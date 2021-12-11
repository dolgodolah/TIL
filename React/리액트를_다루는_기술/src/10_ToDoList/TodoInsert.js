import React from "react";
import './TodoInsert.scss'
import { MdAdd } from 'react-icons/md';
const TodoInsert = () => {
    return (
        <form className="TodoInsert">
            <input placeholder="할 일을 입력하세요" />
            <button type="submit">
                <MdAdd />
            </button>
        </form>
    )
}

export default TodoInsert