import {useState} from "react";

const EventPractice = () => {
    const [message, setMessage] = useState('')
    const [username, setUsername] = useState('')
    const onChangeUsername = (e) => setUsername(e.target.value)
    const onChangeMessage = (e) => setMessage(e.target.value)
    const onKeyPress = (e) => {
        if (e.key === 'Enter') {
            onClick();
        }
    }
    const onClick = () => {
        alert(username + ' : ' + message)
        setMessage('');
        setUsername('');
    }
    return (
        <div>
            <h1>이벤트 연습</h1>
            <input
                type="text"
                name="username"
                placeholder="사용자명"
                value={username}
                onChange={ onChangeUsername }/>
            <input
                type="text"
                name="message"
                placeholder="아무거나 입력해 보세요"
                value={message}
                onChange={ onChangeMessage }
                onKeyPress={ onKeyPress }
            />
            <button onClick={ onClick }>확인</button>
        </div>
    );
}

export default EventPractice;

