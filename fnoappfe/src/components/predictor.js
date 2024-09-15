
import { useState, useContext, useEffect } from 'react';
import { appcontext } from '../support/context.jsx';
import { useFetchData } from '../support/fetch';
import { JsonDataDisplay } from '../support/displayjson';
import { useLocation } from 'react-router-dom';


/*
 
  * will work in two stages.
 * 1. Get options data ()
 * 2. Filter it
 * 3. sort it and predict
 
 */
 
function Predictor() {
    const [bebaseurl, upstoxloginurl] = useContext(appcontext);
    const location = useLocation();
    let routeforbe = location.pathname + location.search;

    const [refreshTrigger, setRefreshTrigger] = useState(0); // Initialize to 0
    
    //stage 1
    //routeforbe = 'options_chain' + location.search;
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

export default Predictor;