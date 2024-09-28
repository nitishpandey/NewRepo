import {  useContext, useEffect } from 'react';
import { appcontext } from '../support/context';

export default function CSRFToken() {
    const [bebaseurl, upstoxloginurl] = useContext(appcontext);

    useEffect(() => {
        fetch(bebaseurl + '', {
            credentials: 'include',  // Include cookies in the request
        }).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            try {
                return response.json();

            } catch (error) {
                throw new Error('Invalid JSON response');
            }

        }).then(data => {
            //  console.log(data);
            localStorage.setItem('csrfToken', data.csrfToken);

        }).catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            // Display an error message to the user (e.g., "Unable to connect to the server")
        });
    }, [bebaseurl]);
    return <> </>;
}