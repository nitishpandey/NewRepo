import logo from './logo.svg';
import './App.css';
import { ChakraProvider } from '@chakra-ui/react'
import { useState, useContext, useEffect, createContext } from 'react';
import Layout from './components/layout';

import MyRoutes from './support/routes'
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


function App() {
   //set up cookies for csrf
    /* parameters for both sandbox and prod */
    const credentialsobject = useContext(Appcredentials);

    /* are we on localhost or production? */
    const currentmode = useContext(Mode);

    
    var upstoxdialogurlstem = 'https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id=';

    const bebaseurl = credentialsobject[currentmode]['bebaseurl'];
    const clientid = credentialsobject[currentmode]['clientid'];



    const redirect_uri = bebaseurl + '/authcode&state=' + (currentmode === 'localhost' ? 'sandbox' : 'prod');
    const upstoxloginurl = upstoxdialogurlstem +
        clientid + '&redirect_uri=' + redirect_uri;

    const appcredentials = createContext([bebaseurl, upstoxloginurl])
    

    return (
            <BrowserRouter>
                <ChakraBaseProvider theme={chakraTheme}>
                <header>
                    <Box as="h1" fontSize="2xl" mb={4}>Algorithmic Trades On Upstox</Box>
                    <Box p={4} borderWidth="1px" borderRadius="md">
                
                   
                        </Box>
                </header>
                <div className="container">
                    <Layout />
                <main className="content">
                        <appcontext.Provider value={[bebaseurl, upstoxloginurl]} >
                            <CSRFToken />
                            <MyRoutes />

                        </appcontext.Provider>
                  
                    </main>
                    </div>
                <footer>
                    <Box as="p" textAlign="center" mt={8}>&copy; 2024 My Upstox Algo Trading Website</Box>
                </footer>
          </ChakraBaseProvider>

            </BrowserRouter> 
        );
    }

   
export default App;
