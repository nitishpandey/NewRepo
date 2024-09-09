import logo from './logo.svg';
import './App.css';
import { ChakraProvider } from '@chakra-ui/react'
import { useState, useContext, useEffect } from 'react';
import Homepage from './pages/homepage';
import EmailForm from './pages/loginform';
import TradingPage from './pages/trading';

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { bebaseurl, Useremail } from './support/context.jsx';

import {
    ChakraBaseProvider,
    extendBaseTheme,
    theme as chakraTheme,
} from '@chakra-ui/react'

const { Button } = chakraTheme.components

const theme = extendBaseTheme({
    components: {
        Button,
    },
})
function AboutUsPage() {

    return (
        <div>
            <h1>About Us</h1>
            <p>Learn more about our company and team.</p>
            <Link to="/">Go to Landing Page</Link>
        </div>
    );
}

function App() {
   //set up cookies for csrf
     const bebaseurl1 = useContext(bebaseurl);
   
    useEffect(() => {
        fetch(bebaseurl1 + '', {
            credentials: 'include',  // Include cookies in the request
        })
            .then(response => response.json())
            .then(data => {
                localStorage.setItem('csrfToken', data.csrfToken);
                // Or store it in your app's state if you prefer
            });
    }, []);
    useEffect(() => {
        fetch(bebaseurl1 + '', {
            credentials: 'include',  // Include cookies in the request
        }).then(response => {
       if (!response.ok) {
           throw new Error('Network response was not ok');
       }
       try {
            response.json();
       } catch (error) {
           throw new Error('Invalid JSON response');
       }
   }
   )
        .then(data => {
            localStorage.setItem('csrfToken', data.csrfToken);
            // Or store it in your app's state if you prefer
        }).catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            // Display an error message to the user (e.g., "Unable to connect to the server")
        });
}, []);

        return (
            <BrowserRouter>
                <ChakraBaseProvider theme={theme}>
                  <nav>
                    <ul>
                        <li><Link to="/">Landing Page</Link></li>
                        <li><Link to="/about">About Us</Link></li>
                    </ul>
                </nav>

                    <Routes>
                        <Route path="/" element={<Layout />}>
                            <Route index element={<Homepage />} />
                     
                    <Route path="funds" element={<TradingPage />} />
                    <Route path="about" element={<AboutUsPage />} />
                            <Route path="*" element={<NoPage />} />
                        </Route>
                    </Routes>
          </ChakraBaseProvider>

            </BrowserRouter>
        );
    }

   
export default App;
