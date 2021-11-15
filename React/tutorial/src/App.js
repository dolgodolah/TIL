import logo from './logo.svg';
import './App.css';
import {Component} from "react";
import MyComponent from "./03_Component/MyComponent";

const App = () => {
  return <MyComponent>리액트</MyComponent>
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
