import React, { useState ,useEffect } from 'react';
import { useContext } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import { appcontext } from '../support/context.jsx';

/*
 * displays form to collect client id and secret.
 * then submits the same to the back end. The back-end must save it in the session.
 * after that redirects to upstxo login dialog
 
*/


function APICredentialsForm() {
     
    const [message, setMessage] = useState(''); // For displaying success/error messages
    const navigate = useNavigate(); // Get the navigate function
    const [bebaseurl, upstoxloginurl] = useContext(appcontext);

    

    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent default form submission behavior

        try {
            const response = await fetch(bebaseurl + '/apicredentials', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': localStorage.getItem('csrfToken')
                },
                body: JSON.stringify({  }),
                credentials: 'include',  // Include cookies in the request
            });

            if (response.ok) {
                setMessage('Credentials submitted successfully!');
                
               
                window.location.href = upstoxloginurl; //change this based on context

            } else {
                setMessage('Error submitting credentials. Please try again.');
            }
        } catch (error) {
            setMessage('An error occurred. Please check your connection.');
            console.error('Error:', error);
        }
    };
   return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="secret">Secret:</label>
                <input
                    type="text"
                    id="secret"
                   
                    required
                />
            </div>
            <div>
                <label htmlFor="key">API Key:</label>
                <input
                     id="key"
                    required
                />
            </div>
            <button type="submit">Submit</button>
            {message && <p>{message}</p>}
        </form>
    );
}

export default APICredentialsForm;