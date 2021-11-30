import logo from './logo.svg';
import './App.css';
import {Component} from "react";
import MyComponent from "./03_Component/MyComponent";
import Counter from "./03_Component/Counter";
import Say from "./03_Component/Say";
import EventPractice from "./04_Event Handling/EventPractice";

const App = () => {
    return <EventPractice />;
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
