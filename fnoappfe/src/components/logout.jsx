
import {  useContext} from 'react';
import { appcontext } from '../support/context.jsx';
import { useFetchData } from '../support/fetch';
import { JsonDataDisplay } from '../support/displayjson';
import { useLocation } from 'react-router-dom';

function Logout() {
    //we build the backend api from the url search path. This is tight binding and we could go for a mapping as well
    

    const { data, loading, error } = useFetchData('', '');
   
   

   if (loading) return <p>Loading...</p>;
   if (error) return <p>Error: {error.message}</p>;
   return <p>Logged Out</p>;
       return (
           <script>
               window.location.href = '/homepage';
           </script>
        );
    }

export default Logout;