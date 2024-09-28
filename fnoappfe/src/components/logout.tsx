
import { useFetchData } from '../support/fetch';


function Logout() {
    //we build the backend api from the url search path. This is tight binding and we could go for a mapping as well
    

    const {  loading, error } = useFetchData('', 0);
   
   

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