import { createContext } from 'react';



export const Mode = createContext('localhost'); //other values based on environment can be mixed, prod
export const appcontext = createContext([]); // this value is updated in app.js


export const Appcredentials = createContext({
    'localhost': {
        'bebaseurl': 'http://127.0.0.1:8000',
        'febaseurl': 'http://127.0.0.1:3000',
        'clientid': '2f21b28b-6251-4c8e-861f-6218bdf7e4b6',
       },
    'mixed': {}, 'prod': {
        'bebaseurl': 'https://upstox-app.azurewebsites.net',
        'febaseurl': 'http://127.0.0.1:3000',
        'clientid': 'cc982509-6fa9-4046-939d-41b190aa9252',
           },
});
