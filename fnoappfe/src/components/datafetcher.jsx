
import { useState, useContext, useEffect } from 'react';
import { useFetchData } from '../support/fetch';
import { JsonDataDisplay } from '../support/displayjson';

function DataFetch() {
  
    const [refreshTrigger, setRefreshTrigger] = useState(0); // Initialize to 0
   
    
    const { data, loading, error } = useFetchData('', refreshTrigger)
    let currentTime = new Date().toLocaleTimeString();

    function fetchAgain() {
        setRefreshTrigger(refreshTrigger => refreshTrigger + 1);
    }
 
   if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}, Are you logged in?</p>;

       return (
            <table><thead><tr>
               <p>Last Fetch Time: {currentTime} &nbsp;    <button onClick={fetchAgain}> Refresh!</button></p>

           </tr></thead><tbody>
                   <JsonDataDisplay jsonData={data} showkey={true} />

           </tbody></table>
        );
    }

export default DataFetch;