
import { useState, useEffect } from 'react';

export const useFetchData = (url,srt) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    let currentTime = new Date().toLocaleTimeString();

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
                    
                    return res.json();
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