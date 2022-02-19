import logo from './logo.svg';
import './App.css';
import {Component, useCallback, useRef, useState} from "react";
import MyComponent from "./03_Component/MyComponent";
import Counter from "./03_Component/Counter";
import Say from "./03_Component/Say";
import EventPractice from "./04_Event Handling/EventPractice";
import ValidationSample from "./05_ref/ValidationSample";
import IterationSample from "./06_Multiple Components/IterationSample";
import LifeCycleSample from "./07_Component Life Cycle/LifeCycleSample";
import ErrorBoundary from "./07_Component Life Cycle/ErrorBoundary";
import Info from "./08_Hooks/Info";
import Counter2 from "./08_Hooks/Counter";
import Average from "./08_Hooks/Average";
import TodoTemplate from "./10_ToDoList/TodoTemplate";
import TodoInsert from "./10_ToDoList/TodoInsert";
import TodoList from "./10_ToDoList/TodoList";

function getRandomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
}

const App = () => {
    const [todos, setTodos] = useState([
        {
            id: 1,
            text: 'ㄹㅣ액트 기초 알아보기',
            checked: true,
        },
        {
            id: 2,
            text: '컴포넌트 스타일링해 보기',
            checked: true
        },
        {
            id: 3,
            text: '일정 관리 앱 만들어 보기',
            checked: false
        },
    ]);

    const nextId = useRef(4);

    const onInsert = useCallback(
        text => {
            const todo = {
                id: nextId.current,
                text: text,
                checked: false,
            };
            setTodos(todos.concat(todo));
            nextId.current += 1;
        },
        [todos]
    );
    return (
        <TodoTemplate>
            <TodoInsert onInsert={onInsert}/>
            <TodoList todos={todos} />
        </TodoTemplate>
    );

    /*
    08_Hooks
     */
    // return <Average />;
    // return <Info />;
    // return <Counter2 />;
    // const [visible, setVisible] = useState(false);
    // return (
    //     <div>
    //         <button onClick={() => setVisible(!visible) }>
    //             {visible ? '숨기기' : '보이기'}
    //         </button>
    //         <hr />
    //         {visible && <Info />}
    //     </div>
    // );

    /*
    07_Component Life Cycle
     */
    // const [color, setColor] = useState('#000000');
    //
    // const handleClick = () => {
    //     setColor(getRandomColor());
    // }
    // return (
    //     <div>
    //         <button onClick={handleClick}>랜덤 색상</button>
    //         <ErrorBoundary>
    //             <LifeCycleSample color={color} />
    //         </ErrorBoundary>
    //
    //     </div>
    //
    // )

    /*
    06_Multiple Components
     */
    // return <IterationSample />;

    /*
    05_ref
     */
    // return <ValidationSample />;

    /*
    04_Event Handling
     */
    // return <EventPractice />;

    /*
    03_Component
     */
    // return (
    //     <div>
    //         <MyComponent name="홍길동" favoriteNumber={7}>리액트</MyComponent>
    //         <Counter />
    //         <Say />
    //     </div>
    // )
}

// 클래스 컴포넌트
// class App extends Component {
//   render() {
//     const name = 'react';
//     return (
//         <div className="react">
//           {name}
//         </div>
//     )
//   }
// }

// 함수형 컴포넌트
// function App() {
//   const name = '리액트';
//   return (
//     <div className="react">
//       {name}
//     </div>
//   );
// }

export default App;
