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
                                 <JsonDataDisplay jsonData={value} />
                           
                            ) : (<> &nbsp; 
                                {key.toUpperCase()}:<JsonDataDisplay jsonData={value} />
                                
                        </>)
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
    
        return (<> {Array.isArray(jsonData) ? (
            <>

                
                    {jsonData.map(key =>
                    (
                        
                        (typeof jsonData === 'object' && !Array.isArray(key))
                            ?
                            (<> <JsonDataDisplay jsonData={key} /> </>):('<>Hi</>')
                        
                    )
                    )

                    }
            
            </>
        ) : (
                <>{jsonData}</>
        )}
        </>

        );
}

