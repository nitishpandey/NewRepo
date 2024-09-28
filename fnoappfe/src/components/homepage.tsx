import { SVGAttributes } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import { useFetchData } from '../support/fetch';

type HomepageType ={
    Logo: React.FunctionComponent <React.SVGAttributes<SVGElement>>;
}
function Homepage({ Logo }: HomepageType) {
    const navigate = useNavigate();

  const  loginpage = (nextpage:string) => {
        navigate('/'+ nextpage);
        return;
    }

    const { data, loading, error } = useFetchData('/profile', 0);
    if (loading) return <p>Loading ...</p>;
    if (error) return <p> {error.message} </p>;
    console.log(JSON.stringify(data, null, 2));
    if (data.name)
        return <p> {data.name} is logged in </p>;
    return (
        <div className="App">
            <header className="App-header">
                 <Logo className="App-logo" />

                <p>
                    Your Personal Algo Trading Platform Is Here.
                </p>
                <a
                    className="App-link"
                    href=""
                    onClick={() => loginpage('loginform')}
                    rel="noopener noreferrer"
                >
                    Start Trading on Upstox For Options.
                </a>
            </header>
        </div>);
}

export default Homepage;