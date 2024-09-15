
import { useState, useContext, useEffect } from 'react';
import { appcontext } from '../support/context.jsx';
import { useFetchData } from '../support/fetch';
import { JsonDataDisplay } from '../support/displayjson';
import { useLocation } from 'react-router-dom';

const Showjson = ({ data }) => {
    const positionsData = data;
    var recurse = false;
    var k, o;
        Object.entries(positionsData).map(([key, obj]) => {

            if (typeof obj === 'object' && obj !== null && !Array.isArray(obj)) {
                recurse = true;
                k = key;
                o = obj;
            }
            if (recurse)
                return (<li key={k}>
                    {k}:
                    <Showjson data={o} />
                </li>)

            else
                return (<li key={k}>
                    {k}: {JSON.stringify({ o })}
                </li>)
        })
   
    } 

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
            <div>
               <p>Last Fetch Time: {currentTime} &nbsp;

                   <button onClick={fetchAgain}> Refresh!</button></p>
                <JsonDataDisplay jsonData={data} />

           </div>
        );
    }

export default DataFetch;