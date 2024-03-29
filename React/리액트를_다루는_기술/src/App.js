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

function createBulkTodos() {
    const array = [];
    for (let i = 1; i <= 2500; i++) {
        array.push({
            id: i,
            text: `할 일 ${i}`,
            checked: false
        });
    }
    return array;
}

const App = () => {
    const [todos, setTodos] = useState(
        createBulkTodos
    );

    const nextId = useRef(2501);

    const onInsert = useCallback(
        text => {
            const todo = {
                id: nextId.current,
                text: text,
                checked: false,
            };
            setTodos(todos => todos.concat(todo));
            nextId.current += 1;
        }, []);

    const onRemove = useCallback(
        id => {
            setTodos(todos => todos.filter(todo => todo.id !== id));
        }, []);

    const onToggle = useCallback(
        id => {
            setTodos(todos =>
                todos.map(todo =>
                    todo.id === id ? { ...todo, checked: !todo.checked } : todo,
                ),
            );
        }, []);

    return (
        <TodoTemplate>
            <TodoInsert onInsert={onInsert}/>
            <TodoList todos={todos} onRemove={onRemove} onToggle={onToggle} />
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
