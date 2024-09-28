
import { useState, useContext, useEffect } from 'react';
import { appcontext } from '../support/context';
import { useLocation } from 'react-router-dom';

interface apidatatype {
    name: string,
    data: 
    Map<string, any[]> | Map<string, object> | object;
};
interface UseFetchDataType {
    data: apidatatype | any;
    loading: boolean;
    error: Error | null;
    title: string;
}
type Refreshheaderprops = {
    refreshTrigger: (event: React.MouseEvent<HTMLButtonElement>) => void;
    title: string;
};

export const Refreshheader = ({ refreshTrigger, title }: Refreshheaderprops) => {
    let currentTime = new Date().toLocaleTimeString();

    return <p>Showing {title}. <br />Last Fetch Time: {currentTime} &nbsp;  Click To  <button onClick={refreshTrigger}> Refresh!</button></p>;

}
//returns json
export const useFetchData = (urlargument: string,srt:number): UseFetchDataType => {
    const [data, setData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    let currentTime = new Date().toLocaleTimeString();
    const [bebaseurl] = useContext(appcontext);
    const location = useLocation();
    useEffect(() => {
        // Clear the error state whenever the location (route) changes
        setError(null);
    }, [location]);
    var url = bebaseurl + location.pathname + location.search;
    var title = location.pathname;
    if (urlargument !== '')
        url = bebaseurl + urlargument;

    let xcsrftoken:any ;

    xcsrftoken = localStorage.getItem('csrfToken');

    
    useEffect(() => {
        fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': xcsrftoken
            },
            credentials: 'include',  // Include cookies in the request
        })
          .then(res => {
             if (!res.ok)
                { // Check if the status code is not in the 200-299 range
                    throw new Error('Network response was not ok. Got code: ' + res.status+ ' for '+ url +' at ' + currentTime +".");
                }
                if (res.status !== 204)
                    return res.json();
                else
                    return;
                    }
                    )
            .then(data => {
                setData(data);
                setLoading(false);
            })
            .catch(error => {
                setError(error);
                setLoading(false);
            });
    }, [url,srt,currentTime]);
   
    return { data, loading, error,title };
};