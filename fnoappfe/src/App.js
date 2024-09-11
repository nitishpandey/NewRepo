import logo from './logo.svg';
import './App.css';
import { ChakraProvider } from '@chakra-ui/react'
import { useState, useContext, useEffect, createContext } from 'react';
import Homepage from './pages/homepage';
import Layout from './pages/layout';
import NoPage from './pages/404';
import EmailForm from './pages/loginform';
import TradingPage from './pages/trading';
import APICredentialsForm from './pages/apiform';
import { Appcredentials, Mode, appcontext } from './support/context.jsx';
import CSRFToken from './support/csrf.jsx';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { Box, 
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
           
        </div>
    );
}

function App() {
   //set up cookies for csrf
    /* parameters for both sandbox and prod */
    const credentialsobject = useContext(Appcredentials);

    /* are we on localhost or production? */
    const currentmode = useContext(Mode);

    
    var upstoxdialogurlstem = 'https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id=';

    const bebaseurl = credentialsobject[currentmode]['bebaseurl'];
    const clientid = credentialsobject[currentmode]['clientid'];



    const redirect_uri = bebaseurl + '/polls&state=' + (currentmode === 'localhost' ? 'sandbox' : 'prod');
    const upstoxloginurl = upstoxdialogurlstem +
        clientid + '&redirect_uri=' + redirect_uri;

    const appcredentials = createContext([bebaseurl, upstoxloginurl])
    

    return (<>
            <BrowserRouter>
                <ChakraBaseProvider theme={theme}>
                <header>
                    <Box as="h1" fontSize="2xl" mb={4}>Algorithmic Trades On Upstox</Box>
                    <Box p={4} borderWidth="1px" borderRadius="md">
                  <nav>
                    <ul>
                        <li><Link to="/">Landing Page</Link></li>
                        <li><Link to="/about">About Us</Link></li>
                    </ul>
                    </nav>
                    <appcontext.Provider value={[bebaseurl, upstoxloginurl]} >
                        <CSRFToken />
                        <Routes>
                            <Route path="/" element={<Layout />}>
                                <Route index element={<Homepage />} />
                                <Route path="loginform" element={<EmailForm />} />
                                <Route path="upstox-credentials" element={<APICredentialsForm />} />
                                <Route path="funds" element={<TradingPage />} />
                                <Route path="about" element={<AboutUsPage />} />
                                <Route path="*" element={<NoPage />} />
                            </Route>
                        </Routes>
                        </appcontext.Provider>
                        </Box>
               </header>
                <main style={{}}>
                    <Box p={4} borderWidth="1px" borderRadius="md">
                 
                    </Box>
                </main>
                <footer>
                    <Box as="p" textAlign="center" mt={8}>&copy; 2024 My Website</Box>
                </footer>
          </ChakraBaseProvider>

            </BrowserRouter> </>
        );
    }

   
export default App;
