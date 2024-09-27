
import { useState, useContext, useEffect } from 'react';
import { appcontext } from '../support/context.jsx';
import { useLocation } from 'react-router-dom';

export const useFetchData = (urlargument,srt) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    let currentTime = new Date().toLocaleTimeString();
    const [bebaseurl, upstoxloginurl] = useContext(appcontext);
    const location = useLocation();

    var url = bebaseurl+ location.pathname + location.search;

    if (urlargument !== '')
        url = bebaseurl + urlargument;
    useEffect(() => {
        fetch(url, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': localStorage.getItem('csrfToken')
            },
            credentials: 'include',  // Include cookies in the request
        })
            .then(res => {
                             if (!res.ok) { // Check if the status code is not in the 200-299 range
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
    console.log(data);
    return { data, loading, error };
};