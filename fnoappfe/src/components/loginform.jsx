import React, { useState ,useEffect } from 'react';
import { useContext } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import {  appcontext } from '../support/context.jsx';
import {
    Box,
    ChakraBaseProvider,
    extendBaseTheme,
    theme as chakraTheme,
} from '@chakra-ui/react'
const { Button } = chakraTheme.components


function EmailForm({screen}) {
    const [email, setEmail] = useState('');
    const [bebaseurl, upstoxloginurl] = useContext(appcontext);
    
 const [message, setMessage] = useState(''); // For displaying success/error messages
    const navigate = useNavigate(); // Get the navigate function

    console.log("BEbaseurl" + bebaseurl);
    console.log("upstoxloginurl" + upstoxloginurl);

    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent default form submission behavior

        try {
            const response = await fetch(bebaseurl + '/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': localStorage.getItem('csrfToken')
                },
                body: JSON.stringify({ email }),
                credentials: 'include',  // Include cookies in the request
            });

            if (response.ok) {
                setMessage('Email submitted successfully!');
                console.log(upstoxloginurl);
                window.location.href = upstoxloginurl;

            } else {
                setMessage('Error submitting email. Please try again. ' + response.statusText+".");
            }
        } catch (error) {
            setMessage('An error occurred. Please check your connection.');
            console.error('Error:', error);
        }
    };
    let email2 = email;
    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="email">Email:</label>
                 <input
                    type="email"
                    id="email"
                    value={email2}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </div>
            <input type="submit" value="Submit"/>
            {message && <p>{message}</p>}
        </form>
    );
}

export default EmailForm;