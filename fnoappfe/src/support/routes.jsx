import logo from '../logo.svg';
import Homepage from '../components/homepage';
import Logout from '../components/logout.jsx';
import NoPage from '../components/404';
import EmailForm from '../components/loginform';
import DataFetch from '../components/datafetcher';
import Predictor from '../components/predictor';
import APICredentialsForm from '../components/apiform';
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
                <Route index element={<Homepage logo={logo}/>} />
                <Route path="loginform" element={<EmailForm />} />
                <Route path="upstox-credentials" element={<APICredentialsForm />} />
                <Route path="funds" element={<DataFetch />} />
                <Route path="trades" element={<DataFetch />} />
                <Route path="positions" element={<DataFetch />} />
                <Route path="options_chain" element={<DataFetch />} />
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