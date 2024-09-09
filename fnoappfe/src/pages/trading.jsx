
import { useState, useContext, useEffect } from 'react';
import { bebaseurl, Useremail } from '../support/context.jsx';

function TradingPage() {
        const [currentTime, setCurrentTime] = useState(new Date().toLocaleTimeString());
    const [positionsData, setPositionsData] = useState();

    const baseurl = useContext(bebaseurl);
    useEffect(() => {
        fetchPositions();

            // Fetch time every second (as before)
           const timeIntervalId = setInterval(fetchPositions, 11000);

            // Fetch news data on initial load
          //one time and on click function  fetchPositions();

            return () => {
                clearInterval(timeIntervalId);
            };
        }, []);

        const fetchPositions = () => {
            fetch(baseurl + '/trades')  // Replace with your actual news API endpoint
                .then(response => response.json())
                .then(data => setPositionsData(data));
        };
       return (
            <div>
                <h1>Welcome to Our Landing Page!</h1>
                <p>This is the main landing page of your application.</p>
                <p>Current Time: {currentTime}</p>

                <button onClick={fetchPositions}>Refresh News</button>

                {positionsData && (
                    <div>
                        <h2>Latest News</h2>
                        <ul>
                            {positionsData.articles.map(article => (
                                <li key={article.title}>
                                    <h3>{article.title}</h3>
                                    <p>{article.description}</p>
                                </li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        );
    }

export default TradingPage;