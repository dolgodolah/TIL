import {Component} from "react";

class ErrorBoundary extends Component {
    state = {
        error: false
    };

    componentDidCatch(error, errorInfo) {
        this.setState({
            error: true
        });
        console.log({ error, errorInfo });
    }
    render() {
        if (this.state.error) return <div>에러 발생</div>;
        return this.props.children;
    }
}

export default ErrorBoundary;