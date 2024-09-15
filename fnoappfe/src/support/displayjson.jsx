import React from 'react';

export function JsonDataDisplay({ jsonData }) {
    if (typeof jsonData === 'object' && !Array.isArray(jsonData))
    return ( <> {jsonData ? (
                <div>
                    
                    <ul>
                {Object.entries(jsonData).map(([key, value]) =>
                    (
                    (key !== 'status') ? (
                        (typeof value === 'object' && value !== null && !Array.isArray(value))

                            ? (
                                <ul><li>  {key.toUpperCase()}: <JsonDataDisplay jsonData={value} />
                            </li></ul>
                            ) : (<li key={key}>
                                {key.toUpperCase()}: {JSON.stringify(value, null, 2)}
                        </li>)
                       ) : ('')
                    )
                )

                }
            </ul>
          
                </div>
            ) : (
                <p>No data available</p>
            )}
        </>

    );
    if (Array.isArray(jsonData))
        return (<> {jsonData ? (
            <div>

                <ul>
                    {jsonData.map(([key, value]) =>
                    (
                        
                            <li key={key}>
                                    {key.toUpperCase()}: {JSON.stringify(value, null, 2)}
                                </li>
                        
                    )
                    )

                    }
                </ul>

            </div>
        ) : (
            <p>No data available</p>
        )}
        </>

        );
}

