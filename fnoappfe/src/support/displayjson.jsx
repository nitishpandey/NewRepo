import React from 'react';

export function JsonDataDisplay({ jsonData, showkey = true }) {

        var childshowKey = false;

    if (typeof jsonData === 'object' && !Array.isArray(jsonData))
        return (<>

        

            {jsonData ? (
                    
                   <>
                {Object.entries(jsonData).map(([key, value]) =>
                    (
                    (key !== 'status') ? (
                        (typeof value === 'object' && value !== null && !Array.isArray(value))

                            ? (
                                <tr>
                                    <JsonDataDisplay jsonData={value} />
                                </tr>
                           
                            ) : (<td> &nbsp; 
                                <b>{key.toUpperCase()}</b><JsonDataDisplay jsonData={value} />
                                
                        </td>)
                       ) : ('')
                    )
                )

                }
          
          </>
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
                <td>{jsonData}</td>
        )}
        </>

        );
}

