import { useNavigate } from 'react-router-dom'; // Import useNavigate


function Homepage({ logo }) {
    const navigate = useNavigate();

  const  loginpage = (nextpage) => {
        navigate('/');
        return;
    }
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />


                <p>
                    Your Personal Algo Trading Platform Is Here.
                </p>
                <a
                    className="App-link"
                    href=""
                    onClick={loginpage('loginform')}
                    rel="noopener noreferrer"
                >
                    Start Trading on Upstox For Options.
                </a>
            </header>
        </div>);
}

export default Homepage;