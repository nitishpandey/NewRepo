import React, { useState ,useEffect } from 'react';
import { useContext } from 'react';
import { bebaseurl, Useremail } from '../support/context.jsx';
import { useNavigate } from 'react-router-dom'; // Import useNavigate


function EmailForm({screen}) {
    const [email, setEmail] = useState('');
    const bebaseurl1 = useContext(bebaseurl);
    const [message, setMessage] = useState(''); // For displaying success/error messages
    const navigate = useNavigate(); // Get the navigate function

   
    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent default form submission behavior

        try {
            const response = await fetch(bebaseurl1 + '/login', {
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
                <Useremail.Provider value={email}>


                </Useremail.Provider >
                navigate('/upstox-login');

            } else {
                setMessage('Error submitting email. Please try again.');
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
            <button type="submit">Submit</button>
            {message && <p>{message}</p>}
        </form>
    );
}

export default EmailForm;