
import { useState, useContext, useEffect } from 'react';
import { appcontext } from '../support/context.jsx';
import { useFetchData } from '../support/fetch';
import { JsonDataDisplay } from '../support/displayjson';
import { useLocation } from 'react-router-dom';

function DataFetch() {
    const [bebaseurl, upstoxloginurl] = useContext(appcontext);
    const location = useLocation();
    const routeforbe = location.pathname + location.search;

    const [refreshTrigger, setRefreshTrigger] = useState(0); // Initialize to 0
    if (location.pathname === '/about') {
        var k = 1;
    }
    
    const { data, loading, error } = useFetchData(bebaseurl + routeforbe, refreshTrigger)
    let currentTime = new Date().toLocaleTimeString();

    function fetchAgain() {
        setRefreshTrigger(refreshTrigger => refreshTrigger + 1);
    }
 
   if (loading) return <p>Loading...</p>;
   if (error) return <p>Error: {error.message}</p>;

       return (
            <table><thead><tr>
               <p>Last Fetch Time: {currentTime} &nbsp;    <button onClick={fetchAgain}> Refresh!</button></p>

           </tr></thead><tbody>
                   <JsonDataDisplay jsonData={data} showkey={true} />

           </tbody></table>
        );
    }

export default DataFetch;