//import logo from '../../public/logo.svg';
import logo from '../logo.svg';
import Homepage from '../components/homepage';
import Logout from '../components/logout';
import NoPage from '../components/404';
import EmailForm from '../components/loginform';
import Datafetchnshow from '../components/datafetcher';
import Predictor from '../components/predictor';

import { Routes, Route,Outlet } from 'react-router-dom';

function AboutUsPage() {

    return (
        <div>
            <h1>About Us</h1>
            <p>Learn more about our company and team.</p>

        </div>
    );
}

function MyRoutes() {
    return (<>
    <Routes>
    <Route path="/"  element={<Outlet />} >
               
                <Route path="loginform" element={<EmailForm />} />
                <Route path="funds" element={<Datafetchnshow />} />
                <Route path="trades" element={<Datafetchnshow />} />
                <Route path="positions" element={<Datafetchnshow />} />
                <Route path="options_chain" element={<Datafetchnshow />} />
                <Route path="predict" element={<Predictor />} />
                <Route path="logout" element={<Logout />} />
                <Route path="about" element={<AboutUsPage />} />
        <Route path="*" element={<NoPage />} />
    </Route>
        </Routes>
         <Outlet />
        </>
        )
}
export default MyRoutes;