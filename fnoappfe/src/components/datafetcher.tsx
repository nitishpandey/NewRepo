
import { useState, useContext } from 'react';
import { useFetchData, Refreshheader } from '../support/fetch';
import { JsonDataDisplay } from '../support/displayjson';
import { useCallback } from 'react';

function Datafetchnshow() {
  
    const [refreshTrigger, setRefreshTrigger] = useState(0); // Initialize to 0
    const { data, loading, error,title } = useFetchData('', refreshTrigger)

    let currentTime = new Date().toLocaleTimeString();

    const fetchAgain= useCallback(() => {
        setRefreshTrigger(refreshTrigger => refreshTrigger + 1);
        console.log('called trigger');
    },[])
 
   if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error.message}, Are you logged in? {currentTime}</p>;

    return (
        <div>
            <Refreshheader refreshTrigger={fetchAgain} title={title} />
            <table><thead><tr>
              
           </tr></thead><tbody>
                   <JsonDataDisplay jsonData={data} showkey={true} />

                </tbody></table>
            </div>
        );
    }

export default Datafetchnshow;