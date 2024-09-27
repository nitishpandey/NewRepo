import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
      <>
          <nav className="menu">
        <ul>
          <li> 
               <Link to="/">Home</Link>
                  </li>
               

                  <li>
                    <Link to="/funds">Funds</Link>
                  </li>
                  <li>
                      <Link to="/positions">Positions</Link>
                  </li>
                  <li>
                      <Link to="/trades">Trades</Link>
                  </li>
                  <li>
                      <Link to="/options_chain?index=Nifty50">Nifty Options Data</Link>
                  </li>
                  <li>
                      <Link to="/options_chain?index=BN">BN Options Data</Link>
                  </li>
                  <li>
                      <Link to="/predict?index=BN">BN Options Trade?</Link>
                  </li>
                  <li>
                      <Link to="/predict?index=Nifty50">Nifty Options Trade?</Link>
                  </li>
                  <li>
                      <Link to="/profile">Your Upstox App Client id</Link>
                  </li>
                  <li>
                      <Link to="/logout">Logout</Link>
                  </li>
                  <li>
                      <Link to="/about">About This Platform</Link>
                  </li>

        </ul>
      </nav>


    </>
  )
};

export default Layout;