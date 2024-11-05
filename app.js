function App() {
    const [state, setState] = React.useState({
        num1: Math.floor(Math.random() * 10) + 1, 
        num2: Math.floor(Math.random() * 10) + 1,  
        response: "",
        score: 0,
        incorrect: false
    });

    function inputKeyPress(event) {
        if (event.key === "Enter") {
            const userAnswer = parseInt(state.response, 10);

            if (userAnswer === state.num1 + state.num2) {
                setState({
                    num1: Math.floor(Math.random() * 10) + 1,  
                    num2: Math.floor(Math.random() * 10) + 1,  
                    score: state.score + 1 , 
                    response: "",
                    incorrect: false
                });
            } else {
                setState({
                    ...state,
                    score: state.score - 1,
                    response: ""  ,
                    incorrect: true
                });
            }
        }
    }

    function updateResponse(event) {
        setState({
            ...state,
            response: event.target.value
        });
    }
    if (state.score === 10) {
        return (
            <div id="won">
                You Won 
            </div>
        )
    }

    return (
        <div>
            <h1>Math Quiz</h1>
            <div className={state.incorrect ? "incorrect" : ""} id="problem">{state.num1} + {state.num2}</div>
            <input
                type="number"
                onKeyPress={inputKeyPress}
                onChange={updateResponse}
                value={state.response}
            />
            <div className="score">Score: {state.score}</div>
        </div>
    );
}

ReactDOM.render(<App />, document.querySelector("#app"));
